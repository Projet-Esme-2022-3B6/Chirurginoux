#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:57:43 2021

@author: warwax
"""

import math

d1=0.145
a2=0.253
d4=0.375

#Modèles Geometrique Direct
dQ1=0
dQ2=45
dQ3=70
dQ4=30


Q1=math.radians(dQ1)
Q2=math.radians(dQ2)
Q3=math.radians(dQ3)
Q4=math.radians(dQ4)

M11=(math.cos(Q1)*math.cos(Q2+Q3)*math.cos(Q4))+(math.sin(Q1)*math.sin(Q4))
M21=(math.sin(Q1)*math.cos(Q2+Q3)*math.cos(Q4))-(math.cos(Q1)*math.sin(Q4))
M31=-math.sin(Q2+Q3)*math.cos(Q4)

M12=(-math.cos(Q1)*math.cos(Q2+Q3)*math.sin(Q4))+(math.sin(Q1)*math.cos(Q4))
M22=(-math.sin(Q1)*math.cos(Q2+Q3)*math.sin(Q4))-(math.cos(Q1)*math.cos(Q4))
M32=-math.sin(Q2+Q3)*math.cos(Q4)

M13=-math.cos(Q1)*math.sin(Q2+Q3)
M23=-math.sin(Q1)*math.sin(Q2+Q3)
M33=-math.cos(Q2+Q3)

M14=math.cos(Q1)*(a2*math.cos(Q2)-d4*math.sin(Q2+Q3))
M24=math.sin(Q1)*(a2*math.cos(Q2)-d4*math.sin(Q2+Q3))
M34=d1-a2*math.sin(Q2)-d4*math.cos(Q2+Q3)


MGD=[[M11,M12,M13,M14],
     [M21,M22,M23,M24],
     [M31,M32,M33,M34],
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
w6=-math.exp(Q4/math.pi)*M33

"""#Position
w1=0
w2=0
w3=0.267
#Orientation
w4=0
w5=0
w6=-math.exp(Q4/math.pi)"""


q1=math.atan2(w2, w1)

C1=math.cos(q1)
S1=math.sin(q1)
q23=math.atan2((C1*w4+S1*w4),w6)

C23=math.cos(q23)
S23=math.sin(q23)
q2=math.atan2((d1-w3-d4*C23),(C1*w1+S1*w2+d4*S23))

q3=q23-q2

rac=math.sqrt(w4**2+w5**2+w6**2)
q4=math.pi*math.log(rac, math.e)


dq1=round(math.degrees(q1),2)
dq2=round(math.degrees(q2),2)
dq3=round(math.degrees(q3),2)
dq4=round(math.degrees(q4),2)


print("q1= ", dq1)
print("q2= ", dq2)
print("q3= ", dq3)
print("q4= ", dq4)