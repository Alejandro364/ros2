import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelSubscriber(Node):
    def __init__(self):
        super().__init__('vel_subscriber_node')
        # Nos suscribimos al topico /cmd_vel
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        linear_x = msg.linear.x
        # Mostramos la velocidad actual
        self.get_logger().info('Velocidad recibida: "%s" m/s' % linear_x)
        
        # Logica de advertencia: si supera 1.0 m/s
        if linear_x > 1.0:
            self.get_logger().warn('¡CUIDADO! Velocidad superior a 1.0 m/s: %s' % linear_x)

def main(args=None):
    rclpy.init(args=args)
    node = VelSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
