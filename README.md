# MusicMood
MusicMood is a web application which recommends Songs for User depending on Choosen Mood! 

# Installation
To use the project completely you need software modules in requirements txt. Then, you can upload it to your own server. 
You need your own Spotify CLIENT ID and CLIENT SECRET. You can get it from Spotify SDK's website.  https://developer.spotify.com/

After getting those credentials you should write them to CLIENT_ID and CLIENT SECRET fields in appv2.py. 
# Usage
After you do everything in installation part correct, you can use it by just running it via "python appv2.py" command. 

If you would like to use project in your server (which is different than localhost)
you should update "SPOTIPY_REDIRECT_URI = 'http://localhost:8080'" part in appv2.py and also " app.run( port=8080)" in the last function. 
These changes should be made according to your own configuration. 
## To get better GUI try MusicMood V2 version.

# How it works  ?

## Data Structure
1) User’s top track data: Firstly, it gathers the id’s of user’s 50 most listened tracks  through  Spotify API. Then, it also gather the features of those 50 tracks and put them into a pandas dataframe. With doing this it gathers the feature data of top 50 songs. 

2) User’s top artist data: Secondly, it gathers the Spotify id’s of most listened artists by the user through Spotify API. Then, it gathers the id’s of most listened songs from the user’s most listened artists. Lastly, it gathers the features of those most famous songs of artist’s. Approximately, it gathers feature data around 400-500 songs in this process.

3) Song’s that User doesn’t like: it gathers this data by using the opposite feature values user’s top listened tracks. It will be explained more in methodology part. 

4) Emotion data: it gathers this data using the officially approved playlists which responds to certain type of emotion. It gathers the id’s of the songs in certain playlist. Then, it  gathers the features of those songs in playlist. For this part, approximately it gathers data feature for 80-120 songs. 

## Methodology

As mentioned in the data part, it gathers data of the songs that user doesn’t like by gathering the songs which have opposite feature values.
 
For instance, features which are important in mood declaration has values between 1 and 0. If user’s general taste got valence value more than 0.3 we gather the songs with smaller valence than 0.3.

To get the user’s general listening taste in features, it queries the top listened songs according to their relevance and  get their mean values. 

For instance, if we got 45 top listened song’s from the user’s most listened data. Then, it multiplies the feature values of most listened song with 45. Following this formula we multiply the last song’s value with 1. 

## Weighted Sum of Features
Then, we get the mean of this feature values with using the formula: 

SUM of All Feature Values / ((N*(N+1))/2)

## Machine Learning 
After the gathering of all data, it puts this data into a learning algorithm with using sklearn library of python. 

It separates the data as test and training data. Size of the test data is 0.15 to reach better accuracy. 
Then it uses those features mentioned below to create a classifier.

"danceability", "loudness", "valence", "energy", "instrumentalness", "acousticness", "key", "speechiness","duration_ms"

As a training algorithm I choose Adaboot classifier. I got the best results with this algorithm. 

After it gave our data as an input to Adaboost I created a classifier which is special to user. 

 
To gather the songs depending on emotion, it calculates the mean feature values of songs which belong to certain emotion type. Then, it gathers new songs closer to those  values. 

Lastly, it gives the feature values of those new songs to our classifier to decide. It chooses best songs for the user’s taste. Those songs will be shown to the user.  



# Technologies
It uses machine learning methods. 
It uses Python's Flask, Pandas and sklearn modules.
# Important Note
User's should be Spotify Premium account owners. Due to API rules for gathering user information.
