import numpy as np
import time
from picamera import PiCamera

import cv2

from wrappers import ImageWrapper, VideoWrapper


def capture_video(path="video_out.video_pb2"):
    video = PiCamera(resolution=(640,480), framerate=30)
    time.sleep(2)
    
    video_wrapper = VideoWrapper()

    read = True
    num_frames = 0
    image = np.ndarray((480,640,3), dtype='uint8')
    while read:

        try:
            video.capture(image, 'bgr', use_video_port=True)

            num_frames += 1

            # resize and convert to gray scale image
            image_array = cv2.resize(image, dsize=(0, 0),
                                   fx=0.5, fy=0.5)
            image_gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)

            # initialize new protobuf image
            image_wrapper = ImageWrapper()
            image_wrapper.copy_from_cv_image(image_gray, fmt='g')

            # write image protobuf to video protobuf
            video_wrapper.add_frame(image_wrapper)

            print("Added %d frames." % num_frames)

        except KeyboardInterrupt:
            read = False

    video_wrapper.write_to_file(path)

    video.close()


def read_video(path="video_out.video_pb2"):
    video_wrapper = VideoWrapper()
    video_wrapper.read_from_file(path)
    return video_wrapper


def play_video(video_wrapper):
    success, video = video_wrapper.get_image_wrapper_frames()

    if success:
        for frame in video:
            success, image = frame.get_open_cv_image()
            if success:
                cv2.imshow("video", image)
                cv2.waitKey(33)


def main():
    capture_path = "video_out.video_pb2"

    capture_video(capture_path)
    video_wrapper = read_video(capture_path)
    play_video(video_wrapper)


if __name__ == "__main__":
    main()
