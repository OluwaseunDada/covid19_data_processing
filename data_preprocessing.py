import json
import os
from pathlib import Path

directory = "{path}/data_january"

def read_tweeter_file(tweets_file):
    file1 = open(tweets_file, 'r')
    Lines = file1.readlines()
    r = Lines[2]
    print(r)
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
for filename in os.listdir(directory):
    if filename.endswith(".jsonl"):
        tweets_file = os.path.join(directory, filename)
        print("tweets_file: " + tweets_file)

        thelist = read_tweeter_file(tweets_file)

        # Serializing json
        json_object = json.dumps(thelist, indent = 4)

        # Writing the results
        f = Path(tweets_file).stem     # the original filename e.g. coronavirus-tweet-id-2020-01-31-23
        result_file = f.replace("coronavirus", "result") # result-tweet-id-2020-01-31-23
        print("result_file: " + result_file)
        with open(result_file, "w") as outfile:
            outfile.write(json_object)