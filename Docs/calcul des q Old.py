#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:57:43 2021

@author: warwax
"""

import math

d2=0.145
a3=0.253
d5=0.375

#Modèles Geometrique Direct
dQ1=0
dQ2=0
dQ3=0
dQ4=0
dQ4+=-90

Q1=math.radians(dQ1)         
Q2=math.radians(dQ2)
Q3=math.radians(dQ3)
Q4=math.radians(dQ4)

M11=math.cos(Q1+Q2)*math.cos(Q3+Q4)
M21=math.sin(Q1+Q2)*math.cos(Q3+Q4)
M31=-math.sin(Q3+Q4)

M12=math.sin(Q1+Q2)
M22=-math.cos(Q1+Q2)
M32=0

M13=-math.cos(Q1+Q2)*math.sin(Q3+Q4)
M23=-math.sin(Q1+Q2)*math.sin(Q3+Q4)
M33=-math.cos(Q3+Q4)

M14=math.cos(Q1+Q2)*(a3*math.cos(Q3)-d5*math.sin(Q3+Q4))
M24=math.sin(Q1+Q2)*(a3*math.cos(Q3)-d5*math.sin(Q3+Q4))
M34=d2-a3*math.sin(Q3)-d5*math.cos(Q3+Q4)


MGD=[[round(M11,4),round(M12,4),round(M13,4),round(M14,4)],
     [round(M21,4),round(M22,4),round(M23,4),round(M24,4)],
     [round(M31,4),round(M32,4),round(M33,4),round(M34,4)],
     [0,0,0,1]]

print(MGD[0])
print(MGD[1])
print(MGD[2])
print(MGD[3])




#Modèles Geometrique Inverse

#Position
w1=M14
w2=M24
w3=M34
#Orientation
w4=math.exp(Q4/math.pi)*M13
w5=math.exp(Q4/math.pi)*M23
w6=math.exp(Q4/math.pi)*M33

"""

#Position
w1=0
w2=0
w3=0.267
#Orientation
w4=0
w5=0
w6=-math.exp(Q4/math.pi)

"""


q12=math.atan2(w2, w1)

C12=math.cos(q12)
S12=math.sin(q12)
q34=math.atan2((C12*w4+S12*w5),w6)

rac=math.sqrt(w4**2+w5**2+w6**2)
q4=math.pi*math.log(rac, math.e)

q3=q34-q4


dq12=round(math.degrees(q12),2)
if dq12<0:
    dq12+=180
dq3=round(math.degrees(q3),2)
if dq3<0:
    dq3+=180
dq4=round(math.degrees(q4),2)
if dq4<0:
    dq4+=180

print("Beginning")
print("Q12= ", dQ1+dQ2)
print("Q3= ", dQ3)
print("Q4= ", dQ4)

print("\nEnd")
print("q12= ", dq12)
print("q3= ", dq3)
print("q4= ", dq4)