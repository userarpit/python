# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 05:42:59 2024

@author: HP
"""
import more_itertools
test =  [[-1, -2], [1,2,3, [4,(5,[6,7])]], (30, 40), [25, 35]]

def unifylist(l_input,l_target):
    for it in l_input:
        if isinstance(it,list):
            unifylist(it,l_target)
        elif isinstance(it,tuple):
            unifylist(list(it), l_target)
        else:
            l_target.append(it)
    return l_target        
    
print(unifylist(test,[]))
print(list(more_itertools.collapse(test)))

for i , value in enumerate(test):
    print(i,value)

print(dir(test))
print(test.__delitem__(2))
print(test.reverse())
print(test)
    