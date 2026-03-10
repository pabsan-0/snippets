#! /usr/bin/env -S tmuxinator start -p
# chmod +x me!

# Install dependencies:
# sudo apt install tmux tmuxinator ffmpeg 
# # requires docker too!
#
# Run:
# chmod +x videostream.tmux
# ./videostream.tmux
#
# Tune me via env variables: 
# export VIDEO_LOOP_SRC="video.mp4"
# export VIDEO_LOOP_DST="stream"
#
# Consume output video:
# Raw stream:       rtsp://127.0.0.1:8554/stream
# Watch on browser: http://127.0.0.1:8889/stream

name: video_looper
windows:
  - main:
      layout: even-vertical 
      panes:
          - docker run --network host bluenviron/mediamtx
          - sleep 1; ffmpeg -re -stream_loop -1 -i "${VIDEO_LOOP_SRC-video.mp4}" -c:v libx264 -x264-params bframes=0 -f rtsp rtsp://localhost:8554/"${VIDEO_LOOP_DST-stream}"
