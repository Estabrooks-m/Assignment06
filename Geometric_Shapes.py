# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:40:20 2024

@author: Estabrooks
"""
#parent class
class shape:
    def area(self, height, width):
        area= print("Area")
        return(area)
    def perimeter(self, height, width):
        per= print("Perimeter")
        return(per)
    
#child classes
class circle(shape):
    None
    
class rectangle(shape):
    def area(self, height, width):
        area= height*width
        return(area)
    def perimeter(self, height, width):
        per= (2*height)+(2*width)
        return(per)
    
class triangle(shape):
    None
    
    
def main(): 
    width= 3
    height= 4
    shape= rectangle()
    print(shape.area(height, width))
    
    
    
    
    
    
    
main()


    
