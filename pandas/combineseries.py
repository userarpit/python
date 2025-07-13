# importing pandas module 
import pandas as pd 
import math

# creating first series 
first =[1, 2, 5, 6, 3, 7, 11, 0, 4] 

# creating second series 
second =[5, 3, 2, 1, 3, 9, 21, 3, 1] 

# making series 
first = pd.Series(first) 

# making seriesa 
second = pd.Series(second) 

# calling .combine() method 
result = first.combine(second, (lambda x1, x2: math.pow(x1,x2))) 

# display 
print(result)
