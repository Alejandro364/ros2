import rclpy

from rclpy.node import Node

def main(args=None):
	rclpy.init()
	print("hola, esto funciona")
	rclpy.shutdown()

if __name__=="__main__":
	main()
