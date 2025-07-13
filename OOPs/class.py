# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:11:14 2024

@author: HP
"""

class Vehicle:
    
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    
    def display(self):
        print(f"{self.color} worth ${self.price} with a name of {self.name}")
        
car1 = Vehicle("Fer","Red convertible",60000)
car2 = Vehicle("Jump","Blue van",10000)

car1.display()
car2.display()