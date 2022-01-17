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

w1=0.375
w2=0
w3=0.145+0.253
w4=1
w5=0
w6=0



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


dq1=math.degrees(q1)
dq2=math.degrees(q2)
dq3=math.degrees(q3)
dq4=math.degrees(q4)


print("q1= ", dq1)
print("q2= ", dq2)
print("q3= ", dq3)
print("q4= ", dq4)