import zmq
import cv2
from wrappers import ImageWrapper


def main():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    print("Collecting images from server...")
    socket.connect("tcp://10.0.0.71:5556")

    g_run = True
    num_frames = 0
    topic = "image"
    len_topic = len(topic.encode())
    socket.setsockopt_string(zmq.SUBSCRIBE, topic)

    image_wrapper = ImageWrapper()

    while g_run:

        try:
            data = socket.recv()
            image_bytes = data[len_topic:]

            image_wrapper.image_pb.ParseFromString(image_bytes)

            success, image = image_wrapper.get_open_cv_image()
            if success:
                cv2.imshow("display", image)
                key = cv2.waitKey(1)
                if key == 'q':
                    g_run = False

        except KeyboardInterrupt:
            print("Interrupt received, stopping...")
            g_run = False

    socket.close()
    context.term()


if __name__ == "__main__":
    main()
