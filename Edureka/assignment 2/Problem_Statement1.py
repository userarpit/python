import numpy as np
import pandas as pd

df = pd.read_csv('top50spotify.csv')

df.drop('SerialNo.',axis='columns',inplace=True)
df.rename(columns={'Track.Name':'Track Name',
                   'Artist.Name':'Artist Name',
                   'Genre':'Genre',
                   'Beats.Per.Minute':'Beats per Minute',
                   'Energy':'Energy',
                   'Danceability':'Danceability',
                   'Loudness..dB..':'Loudness(dB)',
                   'Liveness':'Liveness',
                   'Valence.':'Valence',
                   'Length.':'Length',
                   'Acousticness..':'Acousticness',
                   'Speechiness.':'Speechiness',
                   'Popularity':'Popularity'}, inplace=True)
print(df.head())
df.to_csv('top50.csv')

print(df.loc[0:9,'Energy'].mean())
print(df.loc[0:9,'Length'].mean())

genre_df = df.groupby('Genre')
print(genre_df['Length'].sum())

print("******" * 20)
name_genre_df = df.groupby(['Genre','Artist Name'])


