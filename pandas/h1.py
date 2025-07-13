import numpy as np
import pandas as pd
from collections import namedtuple
# # print(pd.read_html("diff.html"))

# arr = np.random.randn(5)

# print(arr)
# s = pd.Series(arr,index = ['a',"b", "c", "d", "e"])
# print(s)

d = {"b": 1, "a": 0, "c": 2}
s1 = pd.Series(d,index=["a","b","c","d"],name="something")
# print(s1)

# print(s1.iloc[:3])
# print(s1[s1 > s1.median()])

# print(s1.array)
# print(s1.to_numpy())
# print(s1)
# print(s1["b"])
# print('c' in s1)
# print(s1.b)
# print(s1[:2] + s1[2:])
# print(s1)
# s2 = s1.rename("different")
# print(s2)
# s2.b = 99
# print(s1)
# print(s2)


# data frame
d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
    "three": s1
}
df = pd.DataFrame(d,columns=["two","three","four"])
print(df)
print(df.index)
print(df.columns)

d = {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}
df1 = pd.DataFrame(d, index=["a", "b", "c", "d"],columns=["two","three"])
print(df1)

data = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "S10")])
# print(data)
data[:] = [(1,1.0,"abc"),(2,2.0,"def")]
print(pd.DataFrame(data))

# from series
arr = np.array([1,2,3])
s = pd.Series(arr,index=["a","b","c"],name="ser")
df=pd.DataFrame(s)
print(df)

point3d = namedtuple("Point3D","x y z")
df = pd.DataFrame([point3d(0,0,0),point3d(1,1,1)])
print(df)

df = pd.DataFrame.from_dict(dict([("A", [1, 2, 3]), ("B", [4, 5, 6])]),orient="index",
    columns=["one", "two", "three"],)

df["four"] = df["one"] + df["two"] + df["three"]
print(df)
df.insert(1,"foo",df["three"])
print(df)

df11 = df.assign(five=df["four"] / df["three"])
print(df11)

print(df11.query("two == 2").assign(ten=lambda x: x.five * 2,twenty=lambda x:x['ten'] * 2))
print(df11.loc['B'])

arr1_df = pd.DataFrame(np.random.randint(1,10,(2,2)),columns=['A','B'])
arr2_df = pd.DataFrame(np.random.randint(1,10,(2,2)),columns=['A','B'])
print(arr1_df)
print(arr2_df)
print(arr1_df + arr2_df)
print(arr1_df - arr1_df.iloc[0])
print(arr2_df * 5 + 10)
print(arr1_df)
print(arr1_df.add(arr1_df.iloc[0],axis=1))

print(type(np.exp(df)))

ser = pd.Series([1, 2, 3, 4])

print(type(np.exp(ser)))

idx = pd.Index([4, 5, 6])
print(idx)

print(pd.DataFrame(np.random.randn(3, 110)))
pd.set_option("display.width", 20)
pd.set_option("display.max_colwidth", 1)
print(pd.DataFrame(np.random.randn(3, 110)))

dates = pd.date_range("20160326", periods=6)
print(dates)
print(list(pd.RangeIndex(0, 10, 2)))
print(arr1_df.dtypes)
print(arr1_df.info())

print(arr1_df)
print(arr1_df.describe())
print(arr1_df.T)
print(arr1_df.sort_index(axis=0))
print(arr1_df.sort_index(axis=1))

print(arr1_df.sort_index(axis=0,ascending=False))
print(arr1_df.sort_index(axis=1,ascending=False))
print("******************")
print(arr1_df)
print(arr1_df.sort_values(by="B",ascending=False))

print(arr1_df.at[1,'A'])
print(arr1_df.iat[1,1])
print(arr1_df.loc[:,['A']])
print(arr1_df.loc[0,'A'])


print("*" * 100)

df = pd.DataFrame(np.random.randint(1,10,(5,5)),columns=['A','B','C','D','E'])
print(df)
print(df.iloc[:2,2:4])
print(df.iloc[list(range(0,5,2)), [0, 3]])
print(len(df[df["B"] > 4]))
df.loc[:,"F"] = np.random.randint(5, size=len(df))
print(df)
print(df[0:4])
df[df["B"] > 4] = -df
print(df)

df1 = df.reindex(index=[1,10,11,12],method='ffill')
print(df1)

df2 = df.reindex(index=[1,10,11,12])
# df2.fillna(value=5,inplace=True)
print(df2.isna())

print(df)
print(df.mean())
print(df.mean(axis=1))
print(df.sub([1] * len(df),axis="index"))
print(df)
print(df.agg(['sum','min']))
print(df.agg({'A':['sum','min'],'B':['max']}))
print(df['A'].value_counts())
print(df.mode())
print(df)
print(df.mode(axis=1))

df = pd.DataFrame(np.random.randn(10, 4))
print(df)

print(pd.concat([df,df[:4]]))
print("*" * 100)
left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
print(left)
print(right)
print(pd.merge(left,right,on="key"))
