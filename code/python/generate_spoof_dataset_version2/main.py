# pip install Random-Word-Generator
# source --> http://www2.projects.science.uu.nl/memotion/emotifydata/

import random
import pandas as pd
from RandomWordGenerator import RandomWord

numb_tracks = 10
numb_participants = 4
emo_range = 1
min_age = 20
max_age = 60

rw = RandomWord(max_word_size=10, 
                constant_word_size=False, 
                include_digits=False, 
                special_chars=r"@_!#$%^&*()<>?/\|}{~:",
                include_special_chars=False)

def get_rand_numb(range):
    while True:
        yield random.randint(0, range)

random_emo_numb = get_rand_numb(emo_range)

pd_dataset = pd.DataFrame()

emo_params = {
    0: "amazement",
    1: "solemnity",
    2: "tenderness",
    3: "nostalgia",
    4: "calmness",
    5: "power",
    6: "joyful activation",
    7: "tension",
    8: "sadness",
}

other_params = {
    0: "mood",
    1: "liked/disliked",
    2: "age",
}

genre = {
    0 : "classical",
    1 : "rock",
    2 : "metal",
    3 : "pop",
}

#for every track
for i in range(numb_tracks):
    track_id = i
    #we add an equal number of tracks in each of the genres. 
    track_genre = genre[int((i/numb_tracks)*len(genre))]
    #Create a random track name
    track_name = rw.generate()

    #for every user
    for x in range(numb_participants):
        #add the basic track details
        track_dets = {
            'track_id' : track_id, 
            'track_genre' : track_genre,
            'track_name' : track_name,
        }

        #add the emotional ratings from a user on the track
        track_params = {}
        for y in range(len(emo_params)):
            track_params[emo_params[y]] = next(random_emo_numb)

        #finally add the "other params"
        track_params_2 = {
            other_params[0] : random.randint(1, 10),
            other_params[1] : next(random_emo_numb),
            other_params[2] : random.randint(min_age, max_age),
        }

        merged = {**track_dets, **track_params, **track_params_2}
        pd_dataset = pd_dataset.append(merged, ignore_index=True)

#print(pd_dataset)
pd_dataset.to_csv('.\\generert_dataset.csv', index=False)

