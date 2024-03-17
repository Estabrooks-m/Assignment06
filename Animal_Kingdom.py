# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:07:23 2024

@author: Estabrooks
"""
class animal:
    #Generic animal funtions 
    def eat(self):
        eat=("The animal is eating")
        return(eat)
    def sleep(self):
        sleep=("The animal is sleeping")
        print(sleep)
        
#Subclass of animal
class mammal(animal):
    def __init__(self):
        None

class bird(animal):
    def __init__(self):
        None

class fish(animal):
    def __init__(self):
        None

#Subclass of mammals        
class dog(mammal):
    #overrides the animals eat method 
    def eat(self):
        super().eat()
        eat=("The dog is eating")
        return(eat)

class cat(mammal):
    def eat(self):
        eat=("The cat is eating")
        return(eat)

#subclass of birds
class falcon(bird):
    #overrides the animals eat method 
    def eat(self):
        eat=("The falcon is eating")
        return(eat)
    
#subclass of fish
class tuna(fish):
    #overrides the animals eat method 
    def eat(self):
        eat=("The tuna is eating")
        return(eat)
        
        
    


    
    
def main():
    #
    animal= dog()
    print(animal.eat())
    print("")
    
    animal= falcon()
    print(animal.eat())
    print("")
    
    animal= tuna()
    print(animal.eat())
    print("")   
    
main()
        

        
