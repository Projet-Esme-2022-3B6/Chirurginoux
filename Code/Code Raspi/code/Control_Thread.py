import threading
import time

class Control:
    def __init__(self,motors_dico):
        self.MD=motors_dico
    
    def mot_thread(self,motor_name,value):
        self.MD[motor_name].goto(value)
        
    def move_all(self):
        try:
            while True:
                x=input("enter the angle 1 :\n")
                x=int(x)
                y=input("enter the angle 2 :\n")
                y=int(y)
                t1=threading.Thread(target=self.mot_thread, args=("motor_art_1",x,))
                t2=threading.Thread(target=self.mot_thread, args=("motor_art_2",y,))
                t1.start()
                t2.start()
                t1.join()
                t2.join()
        except KeyboardInterrupt:
            for mot_key in self.MD:
                self.MD[mot_key].Quit()
            print("goodbye")
        
                
