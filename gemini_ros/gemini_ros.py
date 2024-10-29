import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import os
import google.generativeai as genai

class GeminiNode(Node):

    def __init__(self):
        
        super().__init__("gemini_node")

        genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

        self.model = genai.GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat(history=[])

        self.output_msg = String()

        self.text_publisher = self.create_publisher(String, "/gemini/output_text", 10)
        self.text_subscriber = self.create_subscription(String, "/gemini/input_text", self.gemini_callback, 10)
    
    def gemini_callback(self, msg):

        self.get_logger().info(f"Subscribed /gemini/input_text: {msg.data}")
        self.prompt = msg.data

        self.res = self.chat.send_message(self.prompt)

        self.output_msg.data = self.res.text
        self.text_publisher.publish(self.output_msg)

        self.get_logger().info(f"Published /gemini/output_text: {self.output_msg.data}")

def main(args=None):

    rclpy.init(args=args)
    node = GeminiNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
