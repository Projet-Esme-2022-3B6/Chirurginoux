import threading
import time

def Moteur1(n):
    for i in range (0,n,1):
        print("le 1er moteur :",i,"\n")
        time.sleep(0.1)

def Moteur2(n):
    for i in range (0,n,1):
        print("le 2eme moteur :",i,"\n")
        time.sleep(0.1)
        
t1=threading.Thread(target=Moteur1, args=(3,))
t2=threading.Thread(target=Moteur2, args=(6,))

t1.start()
t2.start()

t1.join()
t2.join()

print("over")