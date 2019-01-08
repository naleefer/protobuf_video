import video_pb2
import numpy as np

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
