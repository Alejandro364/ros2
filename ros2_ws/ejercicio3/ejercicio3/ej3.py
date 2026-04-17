import rclpy
from rclpy.node import Node
from std_msgs.msg import String # Importamos el tipo String

class ChatterPublisher(Node):
    def __init__(self):
        super().__init__('chatter_publisher_node')
        # Publicamos en el tópico /chatter
        self.publisher_ = self.create_publisher(String, '/chatter', 10)
        
        # Inicializamos el contador en 0
        self.i = 0
        
        # Timer para publicar cada 0.5 segundos
        timer_period = 0.5 
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        # Creamos el texto con el valor actual del contador
        msg.data = 'Hola ROS2, contador: %d' % self.i
        
        # Publicamos el mensaje
        self.publisher_.publish(msg)
        
        # (Opcional) Si quieres ver en tu terminal que está funcionando:
        # self.get_logger().info('Publicando: "%s"' % msg.data)
        
        # Incrementamos el contador para la próxima vez
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = ChatterPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
