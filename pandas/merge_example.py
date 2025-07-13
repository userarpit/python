import pandas as pd

left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K0", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "key1": [4,2,1,3]
    }
)

right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K4"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
        "key1": [1,2,5,6]
    }
)
print(left)
print(right)
result = pd.merge(left, right, how="right", on=["key","key1"])

print(result)
print(left.sort_values('key1'))
print(left['key'].value_counts())