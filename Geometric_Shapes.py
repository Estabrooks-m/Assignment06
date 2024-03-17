# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:40:20 2024

@author: Estabrooks
"""
#parent class
class shape:
    def area(self, height, width):
        area= height*width
        return(area)
    def perimeter(self, height, width):
        per= (2*height)+(2*width)
        return(per)
    
#child classes
class circle(shape):
    
class rectangle(shape):
    
class (triangle):
    
