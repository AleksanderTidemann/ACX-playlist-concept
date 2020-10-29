#### This code is taking the mean of each emotion tag from each track number from the emotify dataset and 
#### writes it to a new CSV file.                                                

### The code is written by Mari Lesteberg with help and guidance from Thomas Haaland , 27. October 2020 ###

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## rearranging the emotion tags in a meaningful order
#emotions = ["track id", " power", " tension", " joyful_activation", " amazement", " solemnity", " sadness", " nostalgia", " tenderness", " calmness" ] ##uncomment to arrange the emotion tags

## reading the csv file
df = pd.read_csv("data_strip.csv")
#df = df[emotions] ##uncomment to arrange the emotion tags
#print(df.head())

## taking the mean emotion tag from each track
df_vals = df.groupby("track id").agg("mean")

print(df_vals.head())

## converting the track means to binaries
df_bin = df_vals.eq(df_vals.max(axis=1), axis=0).astype(int)
print(df_bin.head())

plt.imshow(df_vals, aspect = "auto")
plt.show()

## making a correlation matrix to see the correlation between the emotion tags
corr = df_vals.corr()
sns.heatmap(corr)
plt.tight_layout()
plt.show()

#writing to new cvs files
df_vals.to_csv("df_vals.csv")
df_bin.to_csv("df_w_mood_age_bin.csv")