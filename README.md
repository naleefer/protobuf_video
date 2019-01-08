# protobuf_video

Personal exercise to get a handle on [Google protocol
buffers](https://developers.google.com/protocol-buffers/). Protocol buffers 
defined for Image and Video types in video.proto. video_capture.py defines
wrapper classes for the generated protobuf classes. Uses OpenCV for webcam
capture and image display.

## Dependencies

* Python 3 with numpy, not tested on Python 2
* [Google protocol
buffers](https://developers.google.com/protocol-buffers/)
* [OpenCV](https://github.com/opencv/opencv.git)

## Instructions

* Verify above dependencies are installed 
* Open terminal in containing directory and compile video.proto file
<pre>
protoc -I=. --python_out=. ./video.proto  
</pre>
* Run python script
<pre>
python3 video_capture.py  
</pre>

The script will open whatever camera is considered camera-id 0 by OpenCV, 
capture frames to a numpy array, resize those frames to 1/4 scale, 
convert those frames to grayscale, and start writing those frames to the 
VideoWrapper class. The VideoWrapper class contains a Video protocol buffer 
as defined in  video.proto. The frames are converted to grayscale and 
downsized by 1/4  before saving. This will continue until a Ctl+C keyboard 
interrupt.
 
On interrupt the camera is closed, the Video protocol buffer is serialized 
and written to disk. Default is "video_out.video_pb2" file name.
 
The serialized video file is then read back in, the video parsed, the 
frames converted to OpenCV images, and displayed for 33 ms each using the
cv2.imshow() command.
 
## Caveats
 
This was written entirely for my own education. The goal is to learn 
protocol buffers because they seem like a simple way to serialize complex data 
types for storage, retrieval, and transmission over networks.
  
Little effort has been  made for robust exception handling, *e.g.* if you 
don't have a webcam. It has only been tested on a 2018 Macbook Pro, with 
Python 3 installed via [Homebrew](https://brew.sh/), numpy installed via 
[pip3](https://pip.pypa.io/en/stable/), and protocol buffers/OpenCV installed 
from source. 

 

