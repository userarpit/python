# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 05:18:23 2024

@author: HP
"""

class Example3() :
    __slots__=["slot_0"]
    
    def set_0(self,_value):
        self.__slots__[0] = _value
        
    def get_0(self):
        return self.__slots__[0]

a = Example3()
b = Example3()

a.set_0(10)

print(a.get_0())
b.set_0(20)
print(a.get_0())
print(Example3.__slots__[0])
print(a.__slots__)