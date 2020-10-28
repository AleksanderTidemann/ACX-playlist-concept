import numpy as np
np.set_printoptions(suppress=True, formatter={'float_kind':'{:f}'.format})

curr_state = [1, 2, 2, 11, 20]
des_state = [8, 7, 5, 9, 16]
tracks = 8

#curr_state = []
#curr_state.append(int(input('How happy are you now (from 1-10): ')))
#curr_state.append(int(input('How sad are you now (from 1-10): ')))
#curr_state.append(int(input('How melancoly are you now (from 1-10): ')))
#curr_state.append(int(input('How angry are you now (from 1-10): ')))
#print('\n')
#
#des_state = []
#des_state.append(int(input('How happy do you want to be? (from 1-10): ')))
#des_state.append(int(input('How sad do you want to be?  (from 1-10): ')))
#des_state.append(int(input('How melancoly do you want to be?  (from 1-10): ')))
#des_state.append(int(input('How angry do you want to be?  (from 1-10): ')))
#print('\n')
print('Current state: ',curr_state)
print('Desired state: ',des_state)

#print('\n')
#tracks = int(input('How many tracks do you want in the playlist?: '))

output = np.empty((tracks, len(curr_state)), dtype=float)
for col in range(len(curr_state)):
    for row in range(tracks):
        diff = (abs(curr_state[col]-des_state[col]))
        if curr_state[col] < des_state[col]:
            output[row][col] = ((diff/tracks) * (row+1)) + curr_state[col]
        else:
            output[row][col] = ((diff/tracks) * (tracks-(row+1))) + des_state[col]  

print('\n')
print('These are the linear interpolated vectors which will be used to generate the playlists:')
print(output)