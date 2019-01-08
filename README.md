# protobuf_video

Personal exercise to get a handle on [Google protocol buffers](https://developers.google.com/protocol-buffers/). Protocol buffers defined for Image and Video types in video.proto. video_capture.py defineswrapper classes for the generated protobuf classes. Uses OpenCV for webcam capture and image display.

## Dependencies

* Python 3 with numpy, not tested on Python 2
* [Google protocol
buffers](https://developers.google.com/protocol-buffers/)
* [OpenCV](https://github.com/opencv/opencv.git)

The video_capture_pi.py script is the same thing with a Pi Camera. Make sure the python picamera module is installed and that the protobuf python module is available to python. I found that despite compiling and installing protocol buffers from source on a Pi 3b+, which takes forever, that it was necessary to install protobuf using pip:
<pre>
pip3 install protobuf
</pre>

You will also need a raspberry pi camera module. This script has been tested with Pi Camera Rev 1.3 on a Pi 3b+. Frame rates depend on illumination, getting close to 30 fps in bright light.

## Instructions

* Verify above dependencies are installed 
* Open terminal in containing directory and compile video.proto file
<pre>
protoc -I=. --python_out=. ./video.proto  
</pre>
* Run python script
<pre>
python3 video_capture.py  
  or  
python3 video_capture_pi.py
</pre>

The main script will open whatever camera is considered camera-id 0 by OpenCV, capture frames to a numpy array, resize those frames to 1/4 scale, convert those frames to grayscale, and start writing those frames to the VideoWrapper class. The VideoWrapper class contains a Video protocol buffer as defined in  video.proto. This will continue until a Ctl+C keyboard interrupt.
 
On interrupt the camera is closed, the Video protocol buffer is serialized and written to disk. Default file is "video_out.video_pb2".
 
The serialized video file is then read back in, the video parsed, the frames converted to OpenCV images(numpy arrays in python), and displayed for 33 ms each using the cv2.imshow() command.
 
## Caveats
 
This was written entirely for my own education. The goal is to learn 
protocol buffers because they seem like a simple way to serialize complex data types for storage, retrieval, and transmission over networks.
  
Little effort has been  made for robust exception handling, *e.g.* if you don't have a webcam. It has only been tested on a 2018 Macbook Pro, with Python 3 installed via [Homebrew](https://brew.sh/), numpy installed via [pip3](https://pip.pypa.io/en/stable/), and protocol buffers/OpenCV installed from source. 

 

