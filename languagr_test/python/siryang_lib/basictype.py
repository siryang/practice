# -*- coding: cp936 -*-
#!/usr/bin/python
# BasicType.py
# define basic type 
   
import sys

class Point:
    
    def __init__(self, x=0, y=0):
        self.m_x = x
        self.m_y = y
    
    def __del__(self):
        #destruct
        pass
        
    def show(self):
        print "(%d, %d)" % (self.m_x, self.m_y)
        
    def sub(self, right):
        delt = Point()
        delt.m_x = self.m_x - right.m_x
        delt.m_y = self.m_y - right.m_y
        return delt;

import convert84And02 
class PointArray:
    def __init__(self, array):
        self.m_array = array
        
    def sub(self, right):
        leftLen = len(self.m_array)
        rightLen = len(right.m_array)
        
        if leftLen != rightLen:
            return;
        
        for i in range(leftLen):
            delt = self.m_array[i].sub(right.m_array[i])
            delt.show();
            
    def convert(self):
        posNum = len(self.m_array)
        for i in range(0, posNum):
            self.m_array[i] = convert84And02.conver02to84(self.m_array[i]);
            
class Rect:
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        print "hi"
    
    def boundPoint(self, p):
        if self.left > p.x:
            self.left = p.x
            
        if self.right < p.x:
            self.right = p.x
        
        if self.top > p.y:
            self.top= p.y
            
        if self.bottom < p.y:
            self.bottom = p.y
            
            