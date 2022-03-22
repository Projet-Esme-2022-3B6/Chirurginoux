import threading
import time
from serverUDP import serveurUDP

class Control:
    def __init__(self,motors_dico):
        self.MD=motors_dico
        self.UDP=serveurUDP()
    
    def mot_thread(self,motor_name,value):
        self.MD[motor_name].goto(value)
        
    def move_all(self):
        try:
            while True:
                x=input("enter the angle 1 :\n")
                x=int(x)
                y=input("enter the angle 2 :\n")
                y=int(y)
                x=x*60/180 +12
                y=y*60/180 +12
                x=round(x)
                y=round(y)
                print(y)
                print(x)
                
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
    
    
    def mover(self):
        i=0
        try:
            while True:
                posx,posy,posz=self.UDP.transf_data()
                
                """
                modele Géometrique
                """
                
                q1,q2,q3,q4=...
                
                q1=q1*60/180 +12
                q2=q2*60/180 +12
                q3=q3*60/180 +12
                q4=q4*60/180 +12
                q1=round(q1)
                q2=round(q2)
                q3=round(q3)
                q4=round(q4)
                print(q1)
                print(q2)
                print(q3)
                print(q4)
                
                t1=threading.Thread(target=self.mot_thread, args=("motor_base",q1,))
                t2=threading.Thread(target=self.mot_thread, args=("motor_art_1",q2,))
                t3=threading.Thread(target=self.mot_thread, args=("motor_art_2",q3,))
                t4=threading.Thread(target=self.mot_thread, args=("motor_pince",q4,))
                t1.start()
                t2.start()
                t3.start()
                t4.start()
                t1.join()
                t2.join()
                t3.join()
                t4.join()
                
                
        except KeyboardInterrupt:
            for mot_key in self.MD:
                self.MD[mot_key].Quit()
            print("goodbye")
        
                
