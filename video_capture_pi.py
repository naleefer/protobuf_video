import numpy as np
import video_pb2

import time
from picamera import PiCamera
import picamera.array

import cv2

# Define wrapper class that contains image_pb2 formats
class ImageWrapper(object):

    def __init__(self, input_image=None):

        self.image_pb = video_pb2.Image()
        if input_image is not None:
            self.copy_from(input_image)

    def copy_from(self, input_image):

        if input_image.IsInitialized():
            self.image_pb.CopyFrom(input_image)

    def copy_from_cv_image(self, input_image, timestamp=0, fmt='bgr'):

        self.image_pb.timestamp = timestamp

        shape = input_image.shape

        self.image_pb.cols = shape[1]
        self.image_pb.rows = shape[0]
        if len(shape) > 2:
            self.image_pb.channels = shape[2]
        else:
            self.image_pb.channels = 1

        self.image_pb.format = fmt

        self.image_pb.image_bytes = input_image.tobytes()

    def write_to_file(self, file_path):

        try:
            f = open(file_path, 'wb')

        except OSError:
            print("Could not open file path %s." % file_path)
            return

        if self.image_pb.IsInitialized():
            f.write(self.image_pb.SerializeToString())
        else:
            print("image_pb is not fully initialized.")

        f.close()
        return

    def read_from_file(self, file_path):

        try:
            f = open(file_path, 'rb')
            self.image_pb.Clear()
            self.image_pb.ParseFromString(f.read())
            f.close()
        except IOError:
            print("Could not open file path %s." % file_path)

    def get_open_cv_image(self):
        if self.image_pb.IsInitialized():
            image_cv = np.fromstring(self.image_pb.image_bytes, dtype='uint8')
            image_cv = np.reshape(image_cv, (self.image_pb.rows,
                                             self.image_pb.cols,
                                             self.image_pb.channels))
            return True, image_cv
        else:
            return False, None


class VideoWrapper(object):

    def __init__(self, input_video=None):
        self.video_pb = video_pb2.Video()
        if input_video is not None:
            self.video_pb.copy_from(input_video)

    def copy_from(self, input_video):
        if input_video.IsInitialized():
            self.video_pb.CopyFrom(input_video)

    def add_frame(self, input_image_wrapper):
        if input_image_wrapper.image_pb.IsInitialized():
            new_frame = self.video_pb.frames.add()
            new_frame.CopyFrom(input_image_wrapper.image_pb)
        else:
            print("Tried to add uninitialized frame!")

    def write_to_file(self, file_path):

        try:
            f = open(file_path, 'wb')

        except OSError:
            print("Could not open file path %s." % file_path)
            return

        if self.video_pb.IsInitialized():
            f.write(self.video_pb.SerializeToString())
        else:
            print("image_pb is not fully initialized.")

        f.close()
        return

    def read_from_file(self, file_path):

        try:
            f = open(file_path, 'rb')
            self.video_pb.Clear()
            self.video_pb.ParseFromString(f.read())
            f.close()
        except IOError:
            print("Could not open file path %s." % file_path)

    def get_image_wrapper_frames(self):

        if self.video_pb.IsInitialized():
            return True, [ImageWrapper(x) for x in self.video_pb.frames]
        else:
            print("Video protobuf not initialized!")
            return False, None


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
