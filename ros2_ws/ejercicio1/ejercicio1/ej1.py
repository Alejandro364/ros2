import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist # Importamos el tipo de mensaje Twist

class VelPublisher(Node):
    def __init__(self):
        super().__init__('vel_publisher_node')
        # Publicamos en /cmd_vel con un histórico (queue size) de 10
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Timer para publicar cada 0.1 segundos (10 Hz)
        timer_period = 0.1 
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        
        # Velocidad LINEAL constante en eje X (hacia adelante)
        msg.linear.x = 0.5 
        
        # Velocidad ANGULAR constante en eje Z (giro sobre sí mismo)
        msg.angular.z = 0.2 
        
        self.publisher_.publish(msg)
	#self.get_logger().info('Publicando velocidad: Lineal=%0.1f, Angular=%0.1f' % (msg.linear.x, msg.angular.z))

def main(args=None):
    rclpy.init(args=args)
    node = VelPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
