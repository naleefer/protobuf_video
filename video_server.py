import zmq
import cv2
from wrappers import ImageWrapper

def main():
    video = cv2.VideoCapture(0)

    if not video.isOpened():
        video.open(0)

    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://10.0.0.17:5556")

    read = True
    num_frames = 0
    topic = "image".encode()

    while read:

        try:
            success, image = video.read()

            if success:
                num_frames += 1

                # Convert to gray scale image
                image = cv2.resize(image, dsize=(0, 0),
                                   fx=0.25, fy=0.25)
                image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # initialize new protobuf image
                image_wrapper = ImageWrapper()
                image_wrapper.copy_from_cv_image(image_gray, fmt='g')

                # serial to string, pack into message
                msg = topic+image_wrapper.image_pb.SerializeToString()

                # Send message
                socket.send(msg)

        except KeyboardInterrupt:
            print("Interrupt received, stopping...")
            read = False

    video.release()
    socket.close()
    context.term()

if __name__ == "__main__":
    main()
