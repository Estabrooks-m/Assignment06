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
    #Finds area of circle
    def area(self, height, width):
        r= height/2
        area= 3.1415 * (r**2)
        A= round(area, 3)
        return(A)
    #finds perimeter of circle 
    def perimeter(self, height, width):
        r= height/2
        per= 2* 3.1415* r
        P= round (per, 3)
        return(P)
    
class rectangle(shape):
    #Finds area of rectangle
    def area(self, height, width):
        area= height*width
        return(area)
    #finds perimeter of rectangle 
    def perimeter(self, height, width):
        per= (2*height)+(2*width)
        return(per)
    
class triangle(shape):
    #Finds area of triangle
    def area(self, height, width):
        area= (1/2) * height*width
        return(area)
    #finds perimeter of triangle 
    def perimeter(self, height, width):
        hyp= int(input("Enter third side length "))
        per= height + width + hyp
        return(per) 
    
def main(): 
    width= int(input("Width: "))
    height= int(input("Height: "))
    
    calc= int(input("What shape do you want to calculate: Circle (1), REctangel (2) or triangle(3)? "))
    
    
    if (calc == 1):   
        shape= circle()
        print("Area: ", shape.area(height, width))
        print("Perimeter: ", shape.perimeter(height, width))
        
    elif (calc == 2):   
        shape= rectangle()
        print("Area: ", shape.area(height, width))
        print("Perimeter: ", shape.perimeter(height, width))
        
    elif (calc == 3):   
        shape= triangle()
        print("Area: ", shape.area(height, width))
        print("Perimeter: ", shape.perimeter(height, width))
        
    else:
        while (calc != 1 and calc != 2 and calc !=3):
            calc= int(input("Error try again "))     
        
        if (calc == 1):   
            shape= circle()
            print("Area: ", shape.area(height, width))
            print("Perimeter: ", shape.perimeter(height, width))
            
        elif (calc == 2):   
            shape= rectangle()
            print("Area: ", shape.area(height, width))
            print("Perimeter: ", shape.perimeter(height, width))
            
        elif (calc == 3):   
            shape= triangle()
            print("Area: ", shape.area(height, width))
            print("Perimeter: ", shape.perimeter(height, width))

main()


    
