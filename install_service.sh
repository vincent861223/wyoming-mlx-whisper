#!/bin/bash
cp com.wyoming_mlx_whisper.plist ~/Library/LaunchAgents

# replace <PWD-VARIABLE>
sed -i '' -e 's|<PWD-VARIABLE>|'"$PWD"'|g' ~/Library/LaunchAgents/com.wyoming_mlx_whisper.plist

launchctl load ~/Library/LaunchAgents/com.wyoming_mlx_whisper.plist
