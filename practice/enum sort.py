from enum import Enum, unique
@unique
class Sort(Enum):
    ascending = 1
    descending = 2
    def __call__(self,values):
        return sorted(values,reverse=self is Sort.descending)
    
numbers = [1,2,3,4,6,3,5,2,6,7,8]
print(Sort.ascending(numbers))
print(Sort.descending(numbers))