import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ratings_small.csv')
movie_data = pd.read_csv('links_small.csv')

df = df.drop('timestamp',axis=1)
# print(df.shape)
# print(movie_data.shape)

data = pd.merge(df,movie_data,on="movieId")
# print(data.head())
# print(data.shape)

ratings = pd.DataFrame(data.groupby('imdbId')['rating'].mean())
ratings['num of ratings'] = data.groupby('imdbId')['rating'].count()
print(ratings.sort_values(by = 'num of ratings',ascending=False))

# plt.figure(figsize=(10,4))
# ratings['num of ratings'].hist(bins=7)
# plt.show()
# print(ratings)
# # print(ratings['num of ratings'].value_counts()[2])
# plt.figure(figsize=(10,4))
# ratings['rating'].hist(bins=70)
# plt.show()
# print(data)
moviemat = data.pivot_table(index = "userId",columns="imdbId",values="rating")
print(moviemat.head())