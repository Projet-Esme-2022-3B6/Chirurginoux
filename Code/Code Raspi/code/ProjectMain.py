from Motor_Control import MotorControl
from Control_Thread import Control
import os

def init_all():
    base_motor=MotorControl(gpio_motor=18,initpos=42,pos_min=12,pos_max=72,frequency=300)
    art1_motor=MotorControl(gpio_motor=26,initpos=42,pos_min=12,pos_max=72,frequency=300)
    art2_motor=MotorControl(gpio_motor=13,initpos=42,pos_min=12,pos_max=72,frequency=300)
    pince_motor=MotorControl(gpio_motor=12,initpos=42,pos_min=12,pos_max=72,frequency=300)
    
    motor_dict= {
        "motor_base":base_motor,
        "motor_art_1":art1_motor,
        "motor_art_2":art2_motor,
        "motor_pince":pince_motor,
    }

    MTH=Control(motors_dico=motor_dict)
    MTH.move_all()
    
    
    
if __name__=="__main__":
    init_all()
