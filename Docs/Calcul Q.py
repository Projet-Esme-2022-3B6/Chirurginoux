#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:57:43 2021
@author: warwax
"""
import math


def Modele_Geom(Q1,Q2,Q3,Q4):
    
    
    
    S1=math.cos(Q2)*math.sin(Q1)*math.sin(Q3) + math.cos(Q3)*math.sin(Q1)*math.sin(Q2)
    S2=math.cos(Q1)*math.cos(Q2)*math.sin(Q3) + math.cos(Q1)*math.cos(Q3)*math.sin(Q2)
    S3=d4*math.cos(Q2+Q3) + a2*math.cos(Q2)
    
    M11=(math.cos(Q4)*S2)-(math.sin(Q1)*math.sin(Q4)) 
    M21=-math.cos(Q2+Q3)*math.cos(Q4)
    M31=-math.cos(Q1)*math.sin(Q4)-(math.cos(Q4)*S1)                                     
    
    M12=-math.cos(Q4)*math.sin(Q1)-(math.sin(Q4)*S2)   
    M22=math.cos(Q2+Q3)*math.sin(Q4)    
    M32=math.sin(Q4)*S1-(math.cos(Q1)*math.cos(Q4))                                         
    
    M13=math.cos(Q2+Q3)*math.cos(Q1)
    M23=math.sin(Q2+Q3)
    M33=-math.cos(Q2+Q3)*math.sin(Q1)
    
    M14=math.cos(Q1)*S3
    M24=d1+(d4*math.sin(Q2+Q3))+(a2*math.sin(Q2))
    M34=-math.sin(Q1)*S3  
    
    MGD=[[M11,M12,M13,M14],
         [M21,M22,M23,M24],
         [M31,M32,M33,M34],
         [0,0,0,1]]
    
    print(MGD[0])
    print(MGD[1])
    print(MGD[2])
    print(MGD[3])

    return MGD

def Modele_inverse (w1,w2,w3,w4,w5,w6):
    q1=math.atan2(w2, w1)
    q23=math.atan2((math.cos(q1)*w4+math.sin(q1)*w5), w6)
    q2=math.atan2((d1-w3-d4*math.cos(q23)),(math.cos(q1)*w1+math.sin(q1)*w2+d4*math.sin(q23)))
    q3=q23-q2
    rac=math.sqrt(w4**2+w5**2+w6**2)
    q4=math.pi*math.log(rac, math.e)
    
    return q1,q2,q3,q4



d1=0.145
a2=0.253
d4=0.375

#Modèles Geometrique Direct
dQ1=0
dQ2=90
dQ3=0
dQ4=0


Q1=math.radians(dQ1)
Q2=math.radians(dQ2)
Q3=math.radians(dQ3)
Q4=math.radians(dQ4)


MGD=Modele_Geom(Q1,Q2,Q3,Q4)

#Modèles Geometrique Inverse


#Position
w1=M14=MGD[0][3]
w2=M24=MGD[1][3]
w3=M34=MGD[2][3]
#Orientation
M13=MGD[0][2]
M23=MGD[1][2]
M33=MGD[2][2]

w4=math.exp(Q4/math.pi)*M13
w5=math.exp(Q4/math.pi)*M23
w6=-math.exp(Q4/math.pi)*M33




q1,q2,q3,q4= Modele_inverse (w1,w2,w3,w4,w5,w6)


dq1=math.degrees(q1)
dq2=math.degrees(q2)
dq3=math.degrees(q3)
dq4=math.degrees(q4)
dq1=round(dq1,2)
dq2=round(dq2,2)
dq3=round(dq3,2)
dq4=round(dq4,2)


print("q1= ", dq1)

print("q2= ", dq2)
print("q3= ", dq3)
print("q4= ", dq4)

MGD=Modele_Geom(q1,q2,q3,q4)