import numpy as np
import zmq
import cv2
import time
from picamera import PiCamera

from wrappers import ImageWrapper

def main():
    video = PiCamera(resolution=(640, 480), framerate=10)
    time.sleep(2)

    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://10.0.0.71:5556")

    read = True
    num_frames = 0
    image = np.ndarray((480,640,3), dtype='uint8')
    topic = "image".encode()

    while read:

        try:
            video.capture(image, 'bgr', use_video_port=True)

            num_frames += 1

            # Convert to gray scale image
            image_array = cv2.resize(image, dsize=(0, 0),
                               fx=1.0, fy=1.0)
            image_gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)

            # initialize new protobuf image
            image_wrapper = ImageWrapper()
            image_wrapper.copy_from_cv_image(image_gray, fmt='bgr')

            # serial to string, pack into message
            msg = topic+image_wrapper.image_pb.SerializeToString()

            # Send message
            socket.send(msg)

        except KeyboardInterrupt:
            print("Interrupt received, stopping...")
            read = False

    video.close()
    socket.close()
    context.term()

if __name__ == "__main__":
    main()
