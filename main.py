import pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import os
import json
import urllib.parse

data = pd.read_csv("data/data.csv")
X , y = data.drop("liked",axis=1) , data.liked

try :
    model = pickle.load(open("model/model.sav", 'rb'))
except:
    model = RandomForestClassifier(n_jobs=-1,
                                  max_depth=15,
                                  min_samples_leaf=1,
                                  min_samples_split=4,
                                  n_estimators=42)

    model.fit(X,y)

    pickle.dump(model, open("model/model.sav", 'wb'))
try :
    with open("token.txt","r") as f:
        token = f.read()
        query = input("\n\n\nName of the track and artist ( be careful the database is somewhat capricious ) : ")

    query = urllib.parse.quote(query)
    stream = os.popen(f'curl -X "GET" "https://api.spotify.com/v1/search?q={query}&type=track" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer {token}"')
    data = stream.read()
    try :
        data = json.loads(data)["tracks"]["items"][0]
        song_id = data["id"]
        artist = data["artists"][0]["name"]
        title = data["name"]
        stream = os.popen(f'curl -X "GET" "https://api.spotify.com/v1/audio-features/{song_id}" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer {token}"')
        data = stream.read()
        data = json.loads(data)
        data = pd.DataFrame(data,index=[0])
        data.drop(["type","id","uri","track_href","analysis_url"],axis=1,inplace=True)
        print(f"\n\n\n\nThere is {list(model.predict_proba(data)[0])[1]*100:.2f}% chance that Brice likes \"{title}\" by {artist}\n\n\n")
    except KeyError:
        print("\n\n\nYour token has expired , create a new one : https://developer.spotify.com/console/get-several-tracks/\n\n\n")
    except IndexError:
        print("\n\n\nWe didn't find the song you were looking for\n\n\n")
except FileNotFoundError:
    print("""
          FileNotFoundError : There is no token file
          
          To create one , visit this page : https://developer.spotify.com/console/get-several-tracks/
          
          Log in to your spotify Account , and then copy what's in "OAuth Token" field 
          into a file called "token" in the root directory of the project
          """)