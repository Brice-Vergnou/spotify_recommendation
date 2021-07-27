from yes import yes_ids
from no import no_ids

songs = yes_ids["items"]
songs_ids = ""
for track in songs:
    songs_ids += track["track"]["id"] + ","
songs_ids = songs_ids[:-1]
with open("good.txt","w") as f:
    f.write(songs_ids)

songs = no_ids["items"]
songs_ids = ""
for track in songs:
    songs_ids += track["track"]["id"] + ","
songs_ids = songs_ids[:-1]
with open("dislike.txt","w") as f:
    f.write(songs_ids)
