import json
import os
from pathlib import Path

directory = "{path}/data_january"

def read_tweeter_file(tweets_file):
    file1 = open(tweets_file, 'r')
    Lines = file1.readlines()
    r = Lines[2]
    my_list = []
    for one_line in Lines:
        mydict = json.loads(one_line)

        creation_date = mydict['created_at']
        id = str(mydict['id'])
        e = str(mydict['entities'])
        retweet = str(mydict['retweet_count'])
        fav = str(mydict['favorite_count'])
        language = mydict['lang']
        full_text = mydict['full_text']

        mydata = {
            "id": id,
            "created_at": creation_date,
            "lang": language,
            "entities": e,
            "retweeted_count": retweet,
            "favourites_count": fav,
            "full_text": full_text
        }

        my_list.append(mydata)
    return my_list


# loop through tweet_files in the folder

all_files_in_folder = []
flag_set = set()
for filename in os.listdir(directory):
    if filename.endswith(".jsonl"):
         tweets_file = os.path.join(directory, filename)
         all_files_in_folder.append(tweets_file)

         f = Path(tweets_file).stem     # the original filename e.g. coronavirus-tweet-id-2020-01-31-23
         flag = f[:-3] # drop the last 3 characters e.g. coronavirus-tweet-id-2020-01-31
         flag_set.add(flag)


# loop through the flagset and fetch corresponding files
for x in flag_set:
    # from all files in the folder, find those matching the flag
    flag_list = []
    for aFile in all_files_in_folder:
        if x in aFile:
            someList = read_tweeter_file(aFile)
            flag_list.append(someList)
        else:
            continue

    # for each date, write the content of the flag_list to a file
    json_object = json.dumps(flag_list, indent=4)  # Serializing json

    # Writing the results
    result_file = x.replace("coronavirus", "result")  # result-tweet-id-2020-01-31
    with open(result_file, "w") as outfile:
        outfile.write(json_object)




