import numpy as np

arr = np.array([1.0, 2.5, np.nan, 4.0, np.nan, 6.0])
print(arr)

print(np.count_nonzero(np.isnan(arr)))

print(arr[~np.isnan(arr)])

print(np.nan_to_num(arr, nan=0.0))
print(np.nanmean(arr))  # Mean ignoring NaN values