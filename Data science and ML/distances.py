# importing the library
from scipy.spatial import distance

# defining the points
point_1 = (1, 2)
point_2 = (4, 5)
# point_1, point_2

# computing the euclidean distance
euclidean_distance = distance.euclidean(point_1, point_2)
print('Euclidean Distance b/w', point_1, 'and', point_2, 'is: ', euclidean_distance)

manhattan_distance = distance.cityblock(point_1,point_2)
print('Manhattan Distance b/w', point_1, 'and', point_2, 'is: ', manhattan_distance)

# computing the minkowski distance
minkowski_distance = distance.minkowski(point_1, point_2, p=2)
print('Minkowski Distance b/w', point_1, 'and', point_2, 'is: ', minkowski_distance)

# defining two strings
string_1 = 'muclidean'
string_2 = 'manhattan'

# computing the hamming distance

hamming_distance = distance.hamming(list(string_1), list(string_2)) * len(string_1)
print('Hamming Distance b/w', string_1, 'and', string_2, 'is: ', hamming_distance)