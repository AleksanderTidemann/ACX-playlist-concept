#### Modified to include mood and age

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


## reading the csv file
df = pd.read_csv("C:\\Users\\aleks\\Documents\\GitHub\\acoustix\\code\\python\\track_mean_emotion_dataset\\data_strip_w_mood_age.csv")

emotions = ["amazement", "solemnity", "tenderness", "nostalgia", "calmness", "power", "joyful_activation", "tension", "sadness"]
other = ["mood", "age"]

## taking the mean emotion tag from each track
df_vals = df.groupby("track id").agg("mean")

## converting the track means to binaries
df_emo = df_vals[emotions].eq(df_vals[emotions].max(axis=1), axis=0).astype(int)
## rounding mood and age to nearest int.
df_other = df_vals[other].round().astype(int)
## merge
df_bin = pd.concat([df_emo, df_other], axis=1, sort=False)

print(df_bin.head())

#writing to new cvs files
df_vals.to_csv("C:\\Users\\aleks\\Documents\\GitHub\\acoustix\\code\\python\\track_mean_emotion_dataset\\df_vals_w_mood_age.csv")
df_bin.to_csv("C:\\Users\\aleks\\Documents\\GitHub\\acoustix\\code\\python\\track_mean_emotion_dataset\\df_bin_w_mood_age.csv")