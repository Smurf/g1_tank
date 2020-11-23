#Single Camera Version
v4l2-ctl --device=/dev/video0 --set-fmt-video=width=640,height=480,pixelformat=0
v4l2-ctl --device=/dev/video0 -p 30

ffmpeg -framerate 30 -f video4linux2 -i /dev/video0 -f mjpeg -qscale 5 - 2>/dev/null | streameye -l -p 8090
