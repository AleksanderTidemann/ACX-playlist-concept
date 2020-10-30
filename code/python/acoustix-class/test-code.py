import json
import os
import numpy as np

q = {
        1: {
            'date/time': '24/10/2020 - 15:00:10', 
            'mood': 4, 
                22: {
                    "amazement": 0, 
                    "solemnity": 0, 
                    "tenderness": 0, 
                    "nostalgia": 0, 
                    "calmness": 1,
                    "power": 0,
                    "joyful_activation": 0,
                    "tension": 0,
                    "sadness": 0
                    }, 
                1: {
                    "amazement": 1, 
                    "solemnity": 0, 
                    "tenderness": 0, 
                    "nostalgia": 0, 
                    "calmness": 0,
                    "power": 1,
                    "joyful_activation": 0,
                    "tension": 0,
                    "sadness": 0
                }
            }, 
        2: {
            'date/time': '24/10/2020 - 15:00:10', 
            'mood': 8, 
                17: {
                    "amazement": 0, 
                    "solemnity": 1, 
                    "tenderness": 1, 
                    "nostalgia": 0, 
                    "calmness": 0,
                    "power": 0,
                    "joyful_activation": 0,
                    "tension": 1,
                    "sadness": 1
                    }, 
                30: {
                    "amazement": 0, 
                    "solemnity": 0, 
                    "tenderness": 0, 
                    "nostalgia": 0, 
                    "calmness": 0,
                    "power": 1,
                    "joyful_activation": 0,
                    "tension": 0,
                    "sadness": 1
                    }
            }
    }

current_mood = 3

db = np.array([[1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 7, 25],
                [2, 1, 1, 1, 1, 1, 0, 0, 1, 1, 4, 17],
                [3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 28],
                [4, 0, 0, 0, 0, 0, 0, 1, 1, 1, 8, 29],
                [5, 0, 1, 0, 1, 0, 1, 0, 0, 1, 3, 56],
                [6, 0, 0, 0, 1, 0, 0, 0, 1, 0, 6, 23],
                [7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 8, 89],
                [8, 1, 0, 1, 1, 1, 1, 1, 0, 0, 5, 52]])


test = list(db[5][1:10])

test[0] = 7

print(db)
print(test)


#def hamming_distance(seq1, seq2):
#    return len([i for i in filter(lambda x: x[0] != x[1], zip(seq1, seq2))])


#possible_tracks = []
#mood_storage = []
#state = [ 1, 0, 0, 1, 0, 0, 0, 0]
#lowest_val = len(db)
#adds the hamming distance for each track in the database and the desired state. The lower the return the better!
#for i in range(len(db)):
#    possible_tracks.append(len([y for y in filter(lambda x: x[0] != x[1], zip(state, list(db[i])[1:10]))]))
#    if possible_tracks[i] < lowest_val:
#        lowest_val = possible_tracks[i]
#
##Gets the indices/track_ID's which have the lowest hamming distance. w+1 because the track_ID's in the database are 1-based.
#possible_tracks = [w+1 for w, z in enumerate(possible_tracks) if z == lowest_val]
#
#print("lowest value:", lowest_val)
#print("possible track IDs:", possible_tracks)
#
##Finally, if we have more than one option, we look at the current mood of the user and find the possible track with most similar mood.
#if len(possible_tracks) > 1:
#    print("get_tracks_matchCheck_get_database_track --> More tracks with same hamming distance found. Choosing track with most similar MOOD to current user mood.")
#    for track in possible_tracks:
#        mood_storage.append(db[track-1][10])
#
#    closest = min(mood_storage, key=lambda list_value : abs(list_value - current_mood))
#    print("closest mood in mood_storage:", closest)
#    print("At what index in that closest mood located in mood_storage?", mood_storage.index(closest))
#    print("the closest possible Track_ID based on Mood:", possible_tracks[mood_storage.index(closest)])
#else:
#    print("closest track is", possible_tracks[0])
