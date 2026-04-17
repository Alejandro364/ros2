import rclpy
#import the Node module from ROS2 Python library
from rclpy.node import Node
#Importamos los mensajes
from std_msgs.msg import Int16
#Hay que importar la libreria de calidad de servicio, para establecer el perfil adecuado para leer los datos
from rclpy.qos import ReliabilityPolicy,QoSProfile


class SuscriptorSimple(Node):
   
   def __init__(self):
      super().__init__('Suscriptor_Roberto')
      #creamos el suscriptor, ojo que la definicion de calidad de servicio es un parametro nuevo
      self.subscriber=self.create_subscription(Int16,'topic_basico',self.listener_callback,QoSProfile(depth=10,reliability=ReliabilityPolicy.RELIABLE)) 
      
      
   def listener_callback(self,msg):
         print ("mensaje recibido ",msg.data)
         


#no proprocionamos un valor para args, se utiliza None como valor por defecto
def main(args=None):
   rclpy.init()
   node=SuscriptorSimple()
   #mantiene ejecuandose el nodo hasta que se haga un control+C
   try:
   	rclpy.spin(node)
   except KeyboardInterrupt:
   	print("Nodo detenido por el usuario (Ctrl+C)")
   	#Cuando presionas Ctrl+C, se lanza KeyboardInterrupt, lo que detiene el bucle spin. ROS2 no atrapa esa excepción por defecto en tu main()
   	#Puedes envolver el spin dentro de un bloque try/except para atrapar la interrupción y cerrar el nodo de forma limpia
   finally: #El bloque finally se ejecuta siempre, sin importar si hubo un error o no dentro del try
   	node.destroy_node()
   	#se podría estar intentando llamar a rclpy.shutdown() dos veces. 
   	#Esto sucede porque ROS2 internamente ya invoca el shutdown() automáticamente cuando haces Ctrl+C  
   	# y aquí también lo estamos llamando explícitamente en el bloque finally.
   	# rclpy.ok() nos dice si el sistema está todavía activo.
   	if rclpy.ok():
   		rclpy.shutdown()



#comprobamos que este script python se esta ejecutando como main y no como modulo importado en otro script
if __name__=='__main__':
   main()
