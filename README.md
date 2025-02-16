# Wyoming MLX Whisper Server

[Wyoming protocol](https://github.com/rhasspy/wyoming) server
for the [mlx-whisper](https://pypi.org/project/mlx-whisper) speech to text system.

## Local Install

Clone the repository and set up Python virtual environment:

```sh
git clone https://github.com/vincent861223/wyoming-mlx-whisper.git
cd wyoming-mlx-whisper
script/setup
```

Run a server anyone can connect to:

```sh
./script/run --uri tcp://0.0.0.0:7891 --debug 
```

# Acknowledgements

1. It's a rewrite of ᎠᎡ. Ѕϵrgϵ Ѵictor's wyoming-whisper-api-client.
2. Tests are not functioning as there is no public Whisper API service to test it out.