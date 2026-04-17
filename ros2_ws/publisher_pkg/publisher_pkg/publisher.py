import rclpy
#import the Node module from ROS2 Python library
from rclpy.node import Node
#Importamos los mensajes
from std_msgs.msg import Int16


class PublicadorSimple(Node):
   __contador=0

   def __init__(self):
      super().__init__('Publicador_Roberto')
      #creamos un timer enviando dos parametros
      #La duracion entre dos callbacks (0.2 segundos)
      #definimos el queue size de 10
      self.publisher=self.create_publisher(Int16,'topic_basico',10)
      #La funcion que se llamara cuando se cumpla el tiempo, en este caso timer_callaback
      self.create_timer(1.0,self.timer_callback)
      
      
   def timer_callback(self):
         self.__contador=self.__contador+1
         msg=Int16()
         msg.data=self.__contador
         self.publisher.publish(msg)
         


#no proprocionamos un valor para args, se utiliza None como valor por defecto
def main(args=None):
   rclpy.init()
   node=PublicadorSimple()
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
