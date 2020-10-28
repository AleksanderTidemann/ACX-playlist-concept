#import numpy as np
import Acoustix


#Create users. first, last and age.
user1 = Acoustix.User('aleks', 'tidemann', 28)

user1.log_in(6)
user_input = {40: ["amazement"]}
user1.set_track(user_input)

user_input = {20: ["tension", "sadness"]}
user1.set_track(user_input)
#user1.log_out()

from_state = ["tension"]
to_state = ["amazement"]

tracks = user1.get_tracks(from_state, to_state)
print("user1:", tracks)