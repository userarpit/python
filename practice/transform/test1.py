import numpy as np
temp = [20, 25, 30, 15]

# b = [float(i) for i in a]
# print(b)
# print(type(b[0]))

# min_temp = min(temp)
# max_temp = max(temp)
# # print(min_temp)
# min_max_scaling = [round((num - min_temp) / (max_temp - min_temp), 2) for num in temp]
# print(min_max_scaling)

mean = np.mean(temp)
print(mean)
std_dev = np.std(temp)
print(std_dev)
x_standardized = [round((num - mean) / std_dev, 2) for num in temp]
print(x_standardized)