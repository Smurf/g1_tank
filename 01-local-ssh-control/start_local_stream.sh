ffmpeg -framerate 30 -input_format mjpeg -i /dev/video0 -f video4linux2 -framerate 30 -input_format mjpeg -s 640x480 -i /dev/video2 -f video4linux2 -s 640x480 \
-filter_complex " \
nullsrc=size=1280x480 [base]; \
[0:v] setpts=PTS-STARTPTS [left]; \
[1:v] setpts=PTS-STARTPTS [right]; \
[base][left] overlay=shortest=1 [tmp1]; \
[tmp1][right] overlay=shortest=1:x=640:y=0" \
-tune zerolatency -f mjpeg -qscale 5 - 2>/dev/null | streameye -l -p 8090


