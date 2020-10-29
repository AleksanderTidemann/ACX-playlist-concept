import csv
import json
import datetime
import numpy as np

#OBS!! get_database() length must change if data.csv adds or removes rows!!!

class User:
    #class variables
    user_data_template = {
        "amazement": 0, 
        "solemnity": 0, 
        "tenderness": 0, 
        "nostalgia": 0, 
        "calmness": 0,
        "power": 0,
        "joyful_activation": 0,
        "tension": 0,
        "sadness": 0
        }
    login_data_template = {"date/time": "", "mood": 0}
    

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.current_mood = 0
        self.log = 0
        self.log_tracker = False
        self.user_data = {
                            1: {
                                'date/time': '24/10/2020 - 15:00:10', 
                                'mood': 4, 
                                    22: {
                                        "amazement": 0, 
                                        "solemnity": 0, 
                                        "tenderness": 0, 
                                        "nostalgia": 0, 
                                        "calmness": 0,
                                        "power": 0,
                                        "joyful_activation": 0,
                                        "tension": 1,
                                        "sadness": 1
                                        }, 
                                    1: {
                                        "amazement": 0, 
                                        "solemnity": 0, 
                                        "tenderness": 1, 
                                        "nostalgia": 1, 
                                        "calmness": 1,
                                        "power": 0,
                                        "joyful_activation": 0,
                                        "tension": 0,
                                        "sadness": 0
                                    }
                                }, 
                            2: {
                                'date/time': '24/10/2020 - 15:00:10', 
                                'mood': 6, 
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
        self.ext_database = self.get_database()


    def user_info(self): #intended for use
        """
        This functions as a kind of substitute for the __str__ method.
        It will return necessary user info. 
        """

        return "Full name - {}\nAge - {}\nLogins - {}\nTracks rated - {}".format(self.first +" "+ self.last, self.age, self.log, self.count_tracks())

    def log_in(self, mood=None): #intended for use

        """
        mood = integer in range 0 - 10.
        intension = ...

        We need to log in before:
        * setting tracks
        * getting tracks
        * interpolating

        We first check if the mood type and range is correct before
        initializeing the user_data dict and adding the mood and current 
        date and time to the user_data.
        """
        if not self.log_tracker:
            if mood:
                if type(mood) is int:
                    if 0 <= mood <= 10:
                        self.log = len(self.user_data)+1 #here we enable the ability to add some data to "start with" in the self.user_data and for the log to still be correct.

                        self.user_data[self.log] = self.login_data_template.copy()
                        self.user_data[self.log]["mood"] = mood
                        self.user_data[self.log]["date/time"] = self.curr_date_time()

                        self.current_mood = mood #We store this so we can find tracks based on mood if we have more than one option in the get_tracks().
                        self.log_tracker = True
                    else:
                        print("log_in --> !ERROR! Mood var must be between 0 and 10..")
                        return
                else:
                    print("log_in --> !ERROR! Mood var must be integer..")
                    return
            else:
                print("log_in --> !ERROR! Mood is type None, must be integer between 0 and 10.")
        else:
            print("log_in --> !ERROR! You are already logged inn..")

    def log_out(self): #intended for use
        self.log_tracker = False

    def set_track(self, user_input=None): #intended for use
        """
        example: user_input = {40: ["amazement", "sadness"]}

        User must LOGIN to be able to set/add tracks to profile.

        Here we add tracks with their emotional ratings to the users profile.
        We first copy the template (track_data_template), and add the track ID as key.
        Then we "switch on" the emotional parameter from user_input from 0 to 1.

        IF the track has already been rated, we remove the former rating and add the new one.
        """

        user_input = user_input if user_input else {}
  
        if self.log_tracker:

            if len(user_input) == 1 and type(user_input) is dict: #Check the length and type of the input.
                if type(list(user_input.keys())[0]) is int: #Check that the Track_ID is indeed an integer.
                    if 1 <= list(user_input.keys())[0] <= len(self.ext_database): #Make sure the Track_ID is within the range of tracks we have in the database.

                        for k, v in self.user_data.copy().items(): #Here, if the Track_ID has already been rated, we delete the previous rating before moving on.
                            for c, j in v.copy().items():
                                if type(j) is dict:
                                    if c == list(user_input.keys())[0]:
                                        del self.user_data[k][c]

                        #add Track_ID key to the users profile dict.
                        self.user_data[self.log][list(user_input.keys())[0]] = self.user_data_template.copy()

                        #Then check that the emotional parameters inputs are of correct type and content before adding to user_data.
                        for i in range(len(list(user_input.values())[0])):
                            if type(list(user_input.values())[0][i]) is str:
                                if list(user_input.values())[0][i] in self.user_data_template:
                                    #Switch on (set 1) the parameters that are 0 by default.
                                    self.user_data[self.log][list(user_input.keys())[0]][list(user_input.values())[0][i]] = 1
                                
                                else:
                                    print("set_track --> !ERROR! '{}' is not is not a valid parameter that we are mapping..".format(list(user_input.values())[0][i]))
                                    print("avaliable parameters are: {}".format(list(self.user_data_template.copy())))
                                    del self.user_data[self.log][list(user_input.keys())[0]]
                                    break
                            else:
                                print("set_track --> !ERROR! {} must be of type string..".format(list(user_input.values())[0][i]))
                                del self.user_data[self.log][list(user_input.keys())[0]]
                                break
                    else:
                        print("set_track --> !ERROR! Track_ID must be between {} and {}..".format(1, len(self.ext_database)))
                else:
                    print("set_track --> !ERROR! Track_ID must be integer")
            else:
                print("set_track --> !ERROR! Input dict must be size of 1..")
        else:
            print("set_track --> !ERROR! You must LOG IN to begin adding tracks..")

        return
    
    def count_tracks(self):
        """
        Here we count how many tracks (dicts within dicts..) the user has rated so far.
        This is used in the user_info() method.
        """

        if len(self.user_data):
            count = 0
            for key in self.user_data.keys():
                for n in self.user_data[key]:
                    if type(self.user_data[key][n]) is dict:
                        count += 1
            return count
        else:
            print("count_tracks --> !ERROR! user_data dict is empty.")
    

    def get_tracks(self, from_state=None, to_state=None, from_state_rep=None, to_state_rep=None, track_comp=None): #intended for use
        """
        example: 
        from_state = ["calmness", "sadness", "power"]
        to_state = ["amazement", "tension"]

        ignore rest of arguments.

        Here we find tracks that match the users current emotional (from_state) state and his/hers
        desired emotional state (to_state), based on the users existing profile (self.user_data).

        * First we check the input states for any errors. (from/to_state)
        * Then we make a list representation of the input states that are more comparable to the ext_database and user_data.
        * Then we find all tracks in the User_data and compare then to the from/to state list representations.
            * If we find ONE match, simply return it.
            * If we find MORE than one match, we check the current mood of the user and return the track which log-in mood corresponds best.
            * If we find NO matches, we check the external database for matches:
                * If we find ONE match in the database, simply return it.
                * If we find MORE than one match, we check the current mood of the user and return the track which mood corresponds best.
                * If we find NO matches, we check the hamming distance between the desired state and EVRY track in the database.
                    * If more then one match is found, we again look at the users current MOOD to decide which track to choose.

        """
        
        if self.log_tracker:
            from_state = from_state if from_state else []
            to_state = to_state if to_state else []

            track_comp = track_comp if track_comp else [[],[]]

            from_state_rep = from_state_rep if from_state_rep else [0]*len(self.user_data_template)
            to_state_rep = to_state_rep if to_state_rep else [0]*len(self.user_data_template)

            if from_state and to_state:
                if self.get_tracks_errorCheck(from_state, "from_state") and self.get_tracks_errorCheck(to_state, "to_state"): #if both inputs pass the input check
                    #set the correct index to 1 (instead of 0) in the list we want to use further on.
                    for i in range(len(from_state)):
                        from_state_rep[list(self.user_data_template).index(from_state[i])] = 1
                    for y in range(len(to_state)):
                        to_state_rep[list(self.user_data_template).index(to_state[y])] = 1

                    for key in self.user_data.keys(): #search the users profile for matches to the desired from and to_state.
                        for n in self.user_data[key]:
                            if type(self.user_data[key][n]) is dict:
                                if list(self.user_data[key][n].values()) == from_state_rep: #User_data in list form.
                                    track_comp[0].append(n) #N is the Track ID!
                                if list(self.user_data[key][n].values()) == to_state_rep:
                                    track_comp[1].append(n)

                    track_comp[0] = self.get_tracks_matchCheck(track_comp[0], from_state_rep, "from_state")
                    track_comp[1] = self.get_tracks_matchCheck(track_comp[1], to_state_rep, "to_state")

                    return track_comp
                else:
                    return []
            else:
                print("get_tracks --> !ERROR! You must provide from_state and to_state to get tracks..")                           
        else:
            print("get_tracks --> !ERROR! You must log in first to get tracks..")

    def get_tracks_errorCheck(self, state=None, name=None):
        """
        An extensive check to determine that the state have correct TYPE and CONTENT. 
        Should be [] with "" inside.
        """

        state = state if state else []
        name = name if name else "?"

        if len(state): #if there anything there at all..
            if type(state) is list: #check for correct type.
                if len(state) <= len(self.user_data_template): #check the lengths/sizes
                    for i in range(len(state)): #check the contents, make sure its correct.
                        if type(state[i]) is str:
                            if state[i] in self.user_data_template:
                                pass #input is approved!
                            else:
                                print("get_tracks_errorCheck --> !ERROR! {} argument '{}' is not an avaliable parameter...".format(name, state[i]))
                                print("avaliable parameters are: {}".format(list(self.user_data_template.copy())))
                                return False
                        else:
                            print("get_tracks_errorCheck  --> !ERROR! All items in '{}' must be of type string..".format(name))
                            return False
                    return True
                else:
                    print("get_tracks_errorCheck  --> !ERROR! More items in '{}' than avaliable parameters..".format(name))
            else:
                print("get_tracks_errorCheck  --> !ERROR! '{}' must be of type list..".format(name))
        else:
            print("get_tracks_errorCheck --> !ERROR! '{}' is empty..".format(name))
        
        return False

    def get_tracks_matchCheck(self, tracks=None, state=None, name=None, mood_storage=None, closest=None):
        """
        tracks = [] of possible tracks from either from_state or to_state
        state = [] from_state OR to_state from get_tracks()
        name = string of the state name (from or to)

        Check track matches found in the user profiles. (in get_tracks())

        * IF there is more than one match, we check the current mood of the user, and return 
        the track whose associated mood is closest to the current mood.

        * OTHERWISE, IF there is no matches, we call the get_database_track() method and 
        search the external database for possible matches.

        * FINALLY, IF there is only one match, we simply return it to get_tracks()
        """

        tracks = tracks if tracks else []
        mood_storage = mood_storage if mood_storage else []
        closest = closest if closest else 0
        state = state if state else []
        name = name if name else "?"

        if len(tracks):
            if len(tracks) > 1:
                print("get_tracks_matchCheck --> Found more than one '{}' matches in user profile. Checking mood logs to determine closest match.\n".format(name))
                for i in range(len(tracks)): #for every item in tracks.
                    for k, v in self.user_data.items(): #search the user_data for correct Track_ID and get key to get mood
                        for c, j in v.items():
                            if type(j) is dict: #so here i know its a track.
                                if c == tracks[i]: #if it matches the track.
                                    mood_storage.append(self.user_data[k]["mood"]) #add the mood that was logged with the matching track to mood_storage.
                
                #Here we take the mood values and should calculate the track with the closest assosiated MOOD to the current mood.
                closest = min(mood_storage, key=lambda list_value : abs(list_value - self.current_mood))
                return tracks[mood_storage.index(closest)]

            else:
                print("get_tracks_matchCheck --> Found one '{}' match in user profile\n".format(name))
                return tracks[0]
        else:
            print("get_tracks_matchCheck --> No '{}' matches found in user profile. Searching external database..".format(name))
            return self.get_tracks_matchCheck_get_database_track(state, mood_storage, closest)

    def get_tracks_matchCheck_get_database_track(self, state=None, mood_storage=None, closest=None, possible_tracks=None, lowest_hamming_val=None, track_hamming_storage=None):
        """
        state = [0's and/or 1's] with length of self.user_data_template

        Here we search through the external database to find tracks that match
        the desired state requested in the get_tracks() method when we dont find a match
        in the users recorded profile.

        * If there is more then one match, we at the users current mood and select the track from the 
        database that BEST corresponds to the users mood.

        * If we dont find any matches, we find the tracks with the closest hamming distance to the desired 
        state. If more tracks have similar distance, we again look at the users currently logged mood to find the matching
        track.  
        """

        if self.log_tracker:

            state = state if state else []
            mood_storage = mood_storage if mood_storage else []
            possible_tracks = possible_tracks if possible_tracks else []

            lowest_hamming_val = lowest_hamming_val if lowest_hamming_val else len(self.ext_database)
            track_hamming_storage = track_hamming_storage if track_hamming_storage else []
            closest = closest if closest else 0

            for i in range(len(self.ext_database)):
                if list(self.ext_database[i])[1:10] == state:
                    possible_tracks.append(list(self.ext_database[i])[0])

            if len(possible_tracks):
                if len(possible_tracks) > 1:
                    print("get_tracks_matchCheck_get_database_track --> More than one match found in the external database. Checking track associated moods to determine closest match.\n")
                    for item in possible_tracks:
                        #this is moods of the database tracks found that match our state.
                        mood_storage.append(list(self.ext_database[item])[11])
                    
                    #Absolute difference function, which tells us which value in mood_storage is closest to self.current_mood
                    closest = min(mood_storage, key=lambda list_value : abs(list_value - self.current_mood))
                    return possible_tracks[mood_storage.index(closest)]
                              
                else:
                    print("get_tracks_matchCheck_get_database_track --> One match found in external database.\n")
                    return possible_tracks[0]
            else:
                print("get_tracks_matchCheck_get_database_track --> no matches found in database either. Finding Track with closest hamming distance to the desired state.")
                #adds the hamming distance for each track in the database and the desired state. The lower the return the better!
                for i, item in enumerate(self.ext_database):
                    track_hamming_storage.append(len([y for y in filter(lambda x: x[0] != x[1], zip(state, item[1:10]))]))
                    if track_hamming_storage[i] < lowest_hamming_val:
                        lowest_hamming_val = track_hamming_storage[i]

                #Gets the indices/track_ID's which have the lowest hamming distance. w+1 because the track_ID's in the database are 1-based.
                possible_tracks = [w+1 for w, z in enumerate(track_hamming_storage) if z==lowest_hamming_val]
                
                #Finally, if we have more than one option, we look at the current mood of the user and find the possible track with most similar mood.
                if len(possible_tracks) > 1:
                    print("get_tracks_matchCheck_get_database_track --> More tracks with same hamming distance found - '{}'. Choosing track with most similar MOOD to current user mood.\n".format(possible_tracks))
                    for track in possible_tracks:
                        mood_storage.append(self.ext_database[track-1][10])
                
                    closest = min(mood_storage, key=lambda list_value : abs(list_value - self.current_mood))
                    return possible_tracks[mood_storage.index(closest)]
                else:
                    print("get_tracks_matchCheck_get_database_track --> Found one track with lowest hamming distance to desired state.\n")
                    return possible_tracks[0]


    def __repr__(self):
        """
        This should return the information necessary to recreate the object in question,
        so basically:

        >>>user1 = User("first", "last", 18)
        >>>print(user1)
        'User("first, last, 18)'
        """

        return "User({}, {}, {})".format(self.first, self.last, self.age)

    #if you dont access the instance or class, then we should do a static method
    @staticmethod
    def curr_date_time():
        """
        Gets the current time and date when a users logs inn.
        """

        now = datetime.datetime.now()
        return now.strftime("%d/%m/%Y - %H:%M:%S")

    @staticmethod
    def get_database():
        """
        Here we access the database with 12 coloums(!!) from the current dir.
        This happens automatically on initialization of every user.
        We store it as a np array and use it in the get_tracks() method when we dont find any
        track matches in the users profile.
        """

        with open('test_data.csv', newline='') as csvfile:
            data = np.empty((0, 12), int) #12 rows, as our database should be!! might be changed..
            spamreader = csv.reader(csvfile)
            for i, row in enumerate(spamreader):
                if i != 0: #skip header
                    database_test_list = []
                    for y in range(len(row)):
                        database_test_list.append(int(row[y]))
                    data = np.append(data, np.array([database_test_list]), axis=0)
            return data



#print(user1.__dict__)

#print(isinstance(object, class))
#print(issubclass(object, class))