import threading
import time
from serverUDP import serveurUDP
import math

class Control:
    def __init__(self,motors_dico):
        self.MD=motors_dico
        self.UDP=serveurUDP()
    
    def mot_thread(self,motor_name,value):
        self.MD[motor_name].goto(value)
    def geomot_thread(self,motor_name,value):
        self.MD[motor_name].geomove(value)
    
    def modele_geo(self,x,y,z):
        d1=145
        a2=253
        d4=375
        
        x=abs(x)
        y=abs(y)
        z=abs(z)
        
        x2=math.sqrt(x**2+z**2)
        y2=y-d1
        
        
        q1=math.atan2(-z, x)
        q3=math.acos((x2**2+y2**2-a2**2-d4**2)/(2*a2*d4))
        q2=math.atan2(y2,x2)-math.atan2(d4*math.sin(q3),a2+d4*math.cos(q3))
        
        return q1,q2,q3
    
    def mover(self):
        try:
            while True:
                x1=input("enter the angle 1 :\n")
                x1=int(x1)
                x2=input("enter the angle 2 :\n")
                x2=int(x2)
                x3=input("enter the angle 3 :\n")
                x3=int(x3)
                x4=input("enter the angle 4 :\n")
                x4=int(x4)
                
                x1=x1*60/180 +12
                x2=x2*60/180 +12
                x3=x3*60/180 +12
                x4=x4*60/180 +12
                x1=round(x1)
                x2=round(x2)
                x3=round(x3)
                x4=round(x4)
                
                t1=threading.Thread(target=self.mot_thread, args=("motor_base",x1,))
                t2=threading.Thread(target=self.mot_thread, args=("motor_art_1",x2,))
                t3=threading.Thread(target=self.mot_thread, args=("motor_art_2",x3,))
                t4=threading.Thread(target=self.mot_thread, args=("motor_pince",x4,))
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
    
    
    def move_all(self):
        i=0
        try:
            while True:
                posx,posy,posz=self.UDP.transf_data()
                
                """
                modele Géometrique
                """
                
                q1,q2,q3=self.modele_geo(posx,posy,posz)
                
                q4=0
                
                q1=q1+90
                q3=q3+90
                q4=q4+90
                
                print(q1)
                print(q2)
                print(q3)
                print(q4)
                
                q1=q1*60/180 +12
                q2=q2*60/180 +12
                q3=q3*60/180 +12
                q4=q4*60/180 +12
                q1=round(q1)
                q2=round(q2)
                q3=round(q3)
                q4=round(q4)
                
                
                t1=threading.Thread(target=self.geomot_thread, args=("motor_base",q1,))
                t2=threading.Thread(target=self.geomot_thread, args=("motor_art_1",q2,))
                t3=threading.Thread(target=self.geomot_thread, args=("motor_art_2",q3,))
                t4=threading.Thread(target=self.geomot_thread, args=("motor_pince",q4,))
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
        
                
