INRES="1280x480" # input resolution
OUTRES="1280x480" # output resolution
FPS="30" # target FPS
GOP="60" # i-frame interval, should be double of FPS, 
GOPMIN="30" # min i-frame interval, should be equal to fps, 
THREADS="6" # max 6
CBR="1000k" # constant bitrate (should be between 1000k - 3000k)
QUALITY="ultrafast"  # one of the many FFMPEG preset
AUDIO_RATE="44100"
STREAM_KEY="$1" # use the terminal command Streaming streamkeyhere to stream your video to twitch or justin
SERVER="live-ord03" # twitch server in frankfurt, see https://stream.twitch.tv/ingests/ for list

ffmpeg -re -an -i /dev/video0 -f video4linux2 -framerate 30 -input_format mjpeg -s 640x480 -i /dev/video2 -f video4linux2 -framerate 30 -input_format mjpeg -s 640x480 \
-filter_complex " \
nullsrc=size=1280x480 [base]; \
[0:v] setpts=PTS-STARTPTS [left]; \
[1:v] setpts=PTS-STARTPTS [right]; \
[base][left] overlay=shortest=1 [tmp1]; \
[tmp1][right] overlay=shortest=1:x=640:y=0 [tmp2];
[tmp2] drawtext='
fontfile=media/proggy-clean-ttszbp-1361506269.ttf:
fontsize=40:
fontcolor=white:
x=0:y=0:
textfile=tank_telemetry.txt:reload=1'" \
-f flv \
-vcodec h264_omx -profile:v baseline -level:v 4.0 -g $GOP -keyint_min $GOPMIN -b:v $CBR -minrate $CBR -maxrate $CBR -pix_fmt yuv420p \
-s $OUTRES -threads $THREADS -strict normal \
-bufsize $CBR "rtmp://$SERVER.twitch.tv/app/$1"
