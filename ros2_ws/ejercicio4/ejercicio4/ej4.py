import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ChatterSubscriber(Node):
    def __init__(self):
        super().__init__('chatter_subscriber_node')
        # Nos suscribimos al mismo tópico que usa el publicador
        self.subscription = self.create_subscription(
            String,
            '/chatter',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        # Imprimimos el contenido del mensaje recibido
        self.get_logger().info('He escuchado: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = ChatterSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
