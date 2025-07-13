import sys

index = 0
sum = 0
for i in range(1,len(sys.argv)):
    sum += int(sys.argv[i])

print(sum)
#sys.exit(0)

#print(sys.path)
print(sys.modules)