import rclpy
from rclpy.node import Node
import numpy as np
from sensor_msgs.msg import Image, CompressedImage
import cv2
from cv_bridge import CvBridge

class CameraSubscriberNode(Node):

    def __init__(self):
        super().__init__("process")
        self.pub_debug_img = self.create_publisher(CompressedImage, "processed", 10)
        # self.hsv_img = self.create_publisher(Image, "hsv", 10)
        self.sub_image_feed = self.create_subscription(
            Image,
            "image_raw",
            self.image_feed_callback,
            10)
        self.bridge = CvBridge()

    def image_feed_callback(self, msg):

        image = self.bridge.imgmsg_to_cv2(msg)
        # hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # hsv_msg = self.bridge.cv2_to_imgmsg(hsv, encoding="bgr8") 
        # self.hsv_img.publish(hsv_msg)
        # gray = cv2.cvtCOlor(msg, cv2.COLOR_BGR2GRAY)
        final_msg = self.bridge.cv2_to_compressed_imgmsg(image) 

        self.pub_debug_img.publish(final_msg)


        
def main(args=None):
    rclpy.init(args=args)
    subscriber = CameraSubscriberNode()
    rclpy.spin(subscriber)

    # Below lines are not strictly necessary
    subscriber.destroy_node()
    rclpy.shutdown()
        
if __name__=='__main__':
    main()
