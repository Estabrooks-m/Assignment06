# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:09:49 2024

@author: Estabrooks
"""
#Parent class
class employee:
    def __init__(self, name, position):
        self.name= name
        self.position= position
    def calculate_salary(self):
        sal= f"{self.name}, {self.position}: "
        return(sal)
    
class HourlyEmployee(employee):
    def calculate_salary(self):
        pay= float(input("Hourly pay: "))
        hours= float(input("Hours worked: "))     
        salery= pay*hours
        s= round (salery, 2)
        return(s)
   
class SalariedEmployee(employee):
    def calculate_salary(self):
        pay= float(input("Pay per year: "))
        years= float(input("Years worked: "))    
        tax= .22
        salery= (pay*tax)*years
        s= round (salery, 2)
        return(s)
    
class CommissionEmployee(employee):
    def calculate_salary(self):
        company= float(input("How much did you make in sales: "))
        percent= float(input("What percent do you get to take home: "))  
        p= percent/100
        base= float(input("What is your base pay (if none enter 0)?: "))
        salery= (company*p) + base
        s= round (salery, 2)
        print(super().calculate_salary())
        return(s)


def main():
    name= str(input("Name: "))
    position= str(input("Position: "))
    styp= str(input("How are you payed: Hourly (H), Salaried (S), Commision (C)? "))
    
    if (styp== "H"):
        employee= HourlyEmployee(name, position)
        print("$", employee.calculate_salary())
    elif (styp== "S"):
        employee= SalariedEmployee(name, position)
        print("$", employee.calculate_salary())
    elif (styp== "C"):
        employee= CommissionEmployee(name, position)
        print("$", employee.calculate_salary())
    else:
        while (styp != "H" and styp != "S" and styp != "C"):
            styp= str(input("Invalid Input, try again "))
    
main()
