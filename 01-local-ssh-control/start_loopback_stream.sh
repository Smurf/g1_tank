INRES="1280x480" # input resolution
OUTRES="1280x480" # output resolution
FPS="20" # target FPS
GOP="40" # i-frame interval, should be double of FPS, 
GOPMIN="20" # min i-frame interval, should be equal to fps, 
THREADS="6" # max 6
CBR="750K" # constant bitrate (should be between 1000k - 3000k)
QUALITY="ultrafast"  # one of the many FFMPEG preset
AUDIO_RATE="44100"
STREAM_KEY="$1" # use the terminal command Streaming streamkeyhere to stream your video to twitch or justin
SERVER="live-ord03" # twitch server in frankfurt, see https://stream.twitch.tv/ingests/ for list
sudo modprobe v4l2loopback
v4l2-ctl --device=/dev/video4 --set-fmt-video=width=1280,height=480

v4l2-ctl --device=/dev/video0 --set-fmt-video=width=640,height=480,pixelformat=1
v4l2-ctl --device=/dev/video2 --set-fmt-video=width=640,height=480,pixelformat=1
v4l2-ctl --device=/dev/video2 -p 20

ffmpeg -re -an -thread_queue_size 16 -framerate 20 -input_format mjpeg -i /dev/video0 -f video4linux2 -s 640x480 -framerate 20 -input_format mjpeg -i /dev/video2 -f video4linux2 -s 640x480 \
-filter_complex " \
nullsrc=size=1280x480,framerate=20 [base]; \
[0:v] setpts=PTS-STARTPTS [left]; \
[1:v] setpts=PTS-STARTPTS [right]; \
[base][left] overlay=shortest=1 [tmp1]; \
[tmp1][right] overlay=shortest=1:x=640:y=0,format=yuv420p,framerate=20" \
-tune zerolatency -f v4l2 -bufsize 1000k \
/dev/video4
