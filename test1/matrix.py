from numpy import *

a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])

m = reshape(a,(7,5))
# print(a)
# print(a.shape)

# m_c = insert(m, [5],[[1],[2],[3],[4],[5],[6],[7]],1)
# print(m_c)
m = delete(m,[1],1)
print(m)