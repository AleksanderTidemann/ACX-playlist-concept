import os
import random
import pandas as pd

os.chdir('C:\\Users\\aleks\\Documents\\GitHub\\acoustix\\code\\python\\\generate_spoof_dataset\\tracks')
path_to_csv = os.path.dirname(os.path.abspath(__file__))
emo_list_length = 5
emo_int_range = 9

spoof_data = pd.DataFrame()

def convert(x): 
    string_list = [str(i) for i in x] 
    list_merged = int("".join(string_list))   
    return(list_merged) 

for f in os.listdir():
    emo_tags = []
    file_name, file_ext = os.path.splitext(f)
    for i in range(emo_list_length):
        emo_tags.append(random.randint(1, emo_int_range))

    #Merge the emo tags list to one integer, and add it to a new row in the dataframe.
    #For instance, a tag of 31209 is actually [3, 1, 2, 9]
    new_row = {'track_name': file_name, 'tags': convert(emo_tags)}
    spoof_data = spoof_data.append(new_row, ignore_index=True)

spoof_data.to_csv(path_to_csv + '\\spoof_data.csv', index=False)