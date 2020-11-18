import pandas as pd
import numpy as np


#avaliable emoji tagas, this is what the user tags when hearing tracks
emotions = [":)", ":|", ":/", ":(", ":$"]

#Avaliable features, these are the features we extract from each track in the database
features = ["110-120bpm", "moll", "dur", "akustisk", "instrumental", "dansbar"]

#This is how our full database looks like
database = {
    1 : ["110-120bpm", "moll", "akustisk", "instrumental"],
    2 : ["moll", "akustisk"],
    3 : ["dur", "akustisk", "instrumental"],
    4 : ["110-120bpm", "dur", "akustisk", "instrumental"],
    5 : ["110-120bpm", "moll", "instrumental", "dansbar"],
    6 : ["dansbar"],
    7 : ["moll"],
    8 : ["110-120bpm", "instrumental",],
    9 : ["akustisk", "dur"]
}

#Here we create the "user_profile"
zero = np.zeros(shape=(len(features),len(emotions)))
user_emo_chart = pd.DataFrame(zero, index=features, columns=emotions)
print("Here we see the empty user profile:")
print(user_emo_chart, "\n")

#This function adds a rating (+1) to the user profile where needed
def add_track(track_id, emo):
    for item in database[track_id]: 
        user_emo_chart[emo][item] += 1


#Here the user adds emojis to tracks they listen to
add_track(4, ":)")

add_track(6, ":(")

add_track(9, ":/")

add_track(1, ":)")

add_track(2, ":)")

print("Here we see the user profile with ratings from 5 tracks:")
print(user_emo_chart)