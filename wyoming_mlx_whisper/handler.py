"""Event handler for clients of the server."""
import argparse
import logging
import time
import wave
from io import BytesIO

import librosa
import mlx_whisper
from wyoming.asr import Transcribe, Transcript
from wyoming.audio import AudioChunk, AudioChunkConverter, AudioStop
from wyoming.event import Event
from wyoming.info import Describe, Info
from wyoming.server import AsyncEventHandler

_LOGGER = logging.getLogger(__name__)


class WhisperAPIEventHandler(AsyncEventHandler):
    """Event handler for clients."""

    def __init__(
        self,
        wyoming_info: Info,
        cli_args: argparse.Namespace,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)

        self.cli_args = cli_args
        self._model = cli_args.model
        self.wyoming_info_event = wyoming_info.event()
        self.audio = bytes()
        self.audio_converter = AudioChunkConverter(
            rate=16000,
            width=2,
            channels=1,
        )

    async def handle_event(self, event: Event) -> bool:
        if AudioChunk.is_type(event.type):
            if not self.audio:
                _LOGGER.debug("Receiving audio")

            chunk = AudioChunk.from_event(event)
            chunk = self.audio_converter.convert(chunk)
            self.audio += chunk.audio

            return True

        if AudioStop.is_type(event.type):
            _LOGGER.debug("Audio stopped")
            with BytesIO() as tmpfile:
                with wave.open(tmpfile, "wb") as wavfile:
                    wavfile.setparams((1, 2, 16000, 0, "NONE", "NONE"))
                    wavfile.writeframes(self.audio)
                    audio, sr = librosa.load(
                        BytesIO(tmpfile.getvalue()), sr=16000, mono=True
                    )
                    start_time = time.time()
                    text = mlx_whisper.transcribe(audio, path_or_hf_repo=self._model)[
                        "text"
                    ]
                    end_time = time.time()
            _LOGGER.debug(f"Speech recognition time: {end_time - start_time} seconds")

            _LOGGER.info(text)

            await self.write_event(Transcript(text=text).event())
            _LOGGER.debug("Completed request")

            # Reset
            self.audio = bytes()

            return False

        if Transcribe.is_type(event.type):
            _LOGGER.debug("Transcibe event")
            return True

        if Describe.is_type(event.type):
            await self.write_event(self.wyoming_info_event)
            _LOGGER.debug("Sent info")
            return True

        return True
