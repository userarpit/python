# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:27:58 2024

@author: HP
"""

import operator

test = [(11, 52, 83), (61, 20, 40), (93, 72, 51)]

test.sort(key=operator.itemgetter(0))
print(test)
test.sort(key=operator.itemgetter(1))
print(test)
test.sort(key=operator.itemgetter(2))
print(test)