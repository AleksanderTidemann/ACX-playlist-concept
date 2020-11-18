import Acoustix


#Create users. first, last and age.
user1 = Acoustix.User('aleks', 'tidemann', 28)

#First we log in and set out current MOOD (0 - 10). additionally, the system logs the current date and time of the log in.
user1.log_in(6)

#Here the user adds their FEEDBACK on the tracks they're listening to.
#Underneath the user rates track number 40 and 20 in the dataset to be "amazement" and "tension", "sadness".

user_input = {40: ["amazement"]}

user1.set_track(user_input)



user_input = {20: ["tension", "sadness"]}

user1.set_track(user_input)



#We can log out using this code 
#user1.log_out()

#We can also monitor our users profile by doing this:
#print(user1.user_info())

#When the user REQUESTS a playlist, they put in they're desired from_state (where they emotionally are currently)
#and where they would like to be (to_state).
from_state = ["sadness"]
to_state = ["amazement", "joyful_activation"]

tracks = user1.get_tracks(from_state, to_state)

print(tracks)

#We then pass these tracks to an interpolation method... which is coming...