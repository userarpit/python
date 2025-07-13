import array

arr = array.array("f", [1.0,1.5,2.0])

arr.append(23.0)
print(arr)

arrbytes = bytes((1,2))
print(arrbytes[1])
# arrbytes[2]=3