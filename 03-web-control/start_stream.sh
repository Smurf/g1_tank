#Single Camera Version
v4l2-ctl --device=/dev/video0 --set-fmt-video=width=640,height=480,pixelformat=0
v4l2-ctl --device=/dev/video2 --set-fmt-video=width=640,height=480,pixelformat=0
v4l2-ctl --device=/dev/video2 -p 20
v4l2-ctl --device=/dev/video0 -p 30

#ffmpeg -framerate 20 -f video4linux2 -i /dev/video0 -f mjpeg -qscale 5 - 2>/dev/null | streameye -l -p 8090



ffmpeg -framerate 30 -f video4linux2 -i /dev/video0 -f video4linux2 -framerate 20 -s 640x480 -i /dev/video2 -f mjpeg \
-filter_complex " \
nullsrc=size=1280x480 [base]; \
[0:v] setpts=PTS-STARTPTS [left]; \
[1:v] setpts=PTS-STARTPTS [right]; \
[base][left] overlay=shortest=1 [tmp1]; \
[tmp1][right] overlay=shortest=1:x=640:y=0" \
-tune zerolatency -framerate 20 -f mjpeg -qscale 3 - 2>/dev/null | streameye -l -p 8090


