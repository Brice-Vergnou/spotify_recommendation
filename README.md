# Spotify Recommandation

I am basically a HUGE fan of music ( mostly French rap though with some exceptions but I love music ). And someday , while browsing stuff on Internet , I found the [Spotify's API](https://developer.spotify.com/documentation/web-api/) . I knew I had to use it when I found out you could get information like danceability about your favorite songs just with their id's.

![image](https://user-images.githubusercontent.com/86613710/127216769-745ac143-7456-4464-bbe3-adc53872c133.png)

Once I saw that , my machine learning instincts forced me to work on this project.

## 0. Usage

Once the project downloaded , simply run the main.py file in your terminal.
If you don't have a token to access Spotify's API , simply run the file , the instructions to set it up will be prompted.
Make sure to have scikit-learn and python3 on your computer

## 1. Data Collection

### 1.1 Playlist creation
I collected 100 liked songs and 95 disliked songs

For those I like , I made a [playlist](https://open.spotify.com/playlist/2WONKi3eZaR29QaQCRSiAE?si=a2463f1d382f4399) of my favorite 100 songs. It is mainly French Rap , sometimes American rap , rock or electro music.

For those I dislike , I collected songs from various kind of music so the model will have a broader view of what I don't like

There is :
- [25 metal songs ( Cannibal Corps )](https://open.spotify.com/playlist/37i9dQZF1DZ06evO0grpKg?si=3c829a46465d4367)
- [20 " I don't like " rap songs ( PNL )](https://open.spotify.com/playlist/37i9dQZF1DX2fxPY4lXxv8?si=c69f40a2a2014a25)
- [25 classical songs](https://open.spotify.com/playlist/1h0CEZCm6IbFTbxThn6Xcs?si=933db0752a684db0)
- [25 Disco songs](https://open.spotify.com/playlist/2rkU3Aop33atDJoF8LCCjh?si=5e1247ee29284f0a)

I didn't include any Pop song because I'm kinda neutral about it

### 1.2 Getting the ID's

1. From the [Spotify's API "Get a playlist's Items"](https://developer.spotify.com/console/get-playlist-tracks/) , I turned the playlists into json formatted data which cointains the ID and the name of each track ( ids/yes.py and ids/no.py ). NB : on the website , specify "items(track(id,name))" in the fields format , to avoid being overwhelmed by useless data.

2. With a script ( ids/ids_to_data.py ) , I turned the json data into a long string with each ID separated with a comma.

### 1.3 Getting the statistics

Now I just had to enter the strings into the [Spotify API "Get Audio Features from several tracks"](https://developer.spotify.com/console/get-audio-features-several-tracks/) and get my data files ( data/good.json and data/dislike.json )

## 2. Data features

From [Spotify's API documentation](https://developer.spotify.com/documentation/web-api/reference/#object-audiofeaturesobject) :

* **acousticness** : A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
* **danceability** : Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
* **duration_ms** : The duration of the track in milliseconds.
* **energy** : Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
* **instrumentalness** : Predicts whether a track contains no vocals. “Ooh” and “aah” sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly “vocal”. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
* **key** : The key the track is in. Integers map to pitches using standard Pitch Class notation . E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on.
* **liveness** : Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
* **loudness** : The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.
* **mode** : Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
* **speechiness** : Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
* **tempo** : The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
* **time_signature** : An estimated overall time signature of a track. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure).
* **valence** : A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).


And the variable that has to be predicted :

* **liked** : 1 for liked songs , 0 for disliked songs

## 3. Exploratory Data Analysis

As all figures are integers or digits , we're just going to see the correlation between them and the liked column

![image](https://user-images.githubusercontent.com/86613710/127217398-60dd2d01-8cc9-4f29-8b15-574d7e093bac.png)


According to the figures , I'm very likely...
* To like ... songs :
    * danceable
    * high energy
    * loud
    * with many words
    * fast
    * with high amount of beats
    * slightly positive 
* To dislike ... songs :
    * not very accoustic
    * with low instrumentalness
    * short 

## 4. Modelling

I just used a Random Forest Classifier that i tuned to my needs with GridSearchCV
