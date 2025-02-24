# Wyoming MLX Whisper Server

[Wyoming protocol](https://github.com/rhasspy/wyoming) server
for the [mlx-whisper](https://pypi.org/project/mlx-whisper) speech to text system.

This runs `mlx-community/whisper-large-v3-turbo` by default, which gives a pretty good result and runs nearly real-time on a M1 Pro MacBook Pro.


## Install dependencies
```sh
brew install ffmpeg
```

## Running Wyoming MLX Whisper as service
### Install the service
The Wyoming MLX Whisper server will start at tcp://localhost:7891 by default.
```sh
cd ~
git clone https://github.com/vincent861223/wyoming-mlx-whisper.git
cd wyoming-mlx-whisper
./install_service.sh
```
The first speech recognition might take longer to process because it needs to download the model and load the weight. 

### Uninstall the service
```sh
./uninstall_service.sh
```

## Running as script 

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