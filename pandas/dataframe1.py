import pandas as pd
import numpy as np

my_list = [['Alex',10],['Bob',12],['Clark',13]]

a = pd.DataFrame(my_list,index=np.arange(100,103),columns=['Name','Age'])
print(a)

my_dict = {"Name":['Tom','Jack','Arpit'],"Age":[10,20,30]}

print(pd.DataFrame(my_dict,index=np.arange(1,4,1)))


