#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:47:30 2017

@author: marc
"""

from tkinter import *
from time import *

def enregistrement(time,delta_t):
    
    pos=[]
    t=0
    conteur=int((time/delta_t)+1)
    root=Tk()
    
    while t<=time:
        
        x=root.winfo_pointerx()
        y=root.winfo_pointery()
        pos.append((t,x,y))
        
        sleep(delta_t)
        t+=delta_t
    
    result=open("Data_mouse.txt","w")
    
    for i in range(0,conteur):
        
        result.write(str(pos[i][0])+" "+str(pos[i][1])+" "+str(pos[i][2])+"\n")
        
    result.close()

enregistrement(600,1)