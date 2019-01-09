from flask import Flask,render_template,request,jsonify
from spotipy import oauth2

import spotipy
import pandas as pd
#scripts I wrote
import userData as ud
import learner as learner
import emotionData as emotion

app=Flask(__name__)


# Necessary Credential Variables

SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
SCOPE = "user-top-read"
CACHE = 'spotipyoauthcache'


features = ["danceability", "loudness", "valence", "energy", "instrumentalness", "acousticness", "key", "speechiness","duration_ms"]

# This function is setting up all the things for oauth2 authentication

sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )
@app.route("/")
def index():

    access_token = ""

    token_info =sp_oauth.get_cached_token()

    if token_info:
        print ("Found cached token!")
        access_token = token_info['access_token']
    else:
        url = request.url
        print(url)
        code = sp_oauth.parse_response_code(url)
        if code:
            print ("Found spotify auth code in Request URL! Trying to get valid access token...")
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']

    if access_token:
        print ("Access token available! Trying to get user information...")

        #geri gelen listenin json a dönüştürülmesi
        #j_total_list=json.dumps(art_analysis,indent=4)
        #print(len(art_analysis))
        #index.ada=learning(art_analysis,top_analysis,bad)
        #print(a)

        #Parts for the happy list

        index.sp = spotipy.Spotify(access_token)

        top_id=ud.topTrackId(index.sp)

        top_analysis=ud.topTrackFeatures(index.sp,top_id)

        index.art_id=ud.topArtistTrackId(index.sp)

        #müzisyenlerin en ünlü şarkılarından kişinin en çok dinlendiği şarkıları çıkartma işlemi
        index.art_id=list(set(index.art_id)-set(top_id))

        art_analysis=ud.topArtistTrackFeatures(index.sp,index.art_id)
        print(len(art_analysis))

        bad=ud.newdata(index.sp,top_analysis,index.art_id)
        index.ada=learner.learning(art_analysis,top_analysis,bad)


        return render_template('index.html')
    else:
        return htmlForLoginButton()

@app.route('/happy',methods=['POST'])
def happy():
    sp=index.sp
    ada=index.ada
    art_id=index.art_id
    recs=emotion.happylist(sp,art_id)
    happys=pd.DataFrame(recs)
    ids=happys['id']

    happys=happys[features]
    prediction=ada.predict(happys)
    id_list=ids.tolist()
    song_name=[]
    names=sp.tracks(id_list)
    for track in names['tracks']:
        song_name.append(track['name'])
    goodSongsLink=[]
    goodSongsName=[]
    for i in range(len(prediction)):
        if prediction[i] :
            goodSongsLink.append("https://open.spotify.com/track/"+id_list[i])
            goodSongsName.append(song_name[i])
        happyDict=dict(zip(goodSongsName,goodSongsLink))
    return render_template('happy.html',happyDict=happyDict,token=index.sp)

@app.route('/sad',methods=['POST'])
def sad():
    sp=index.sp
    ada=index.ada
    art_id=index.art_id
    recs=emotion.sadlist(sp,art_id)
    sads=pd.DataFrame(recs)
    ids=sads['id']

    sads=sads[features]
    prediction=ada.predict(sads)
    id_list=ids.tolist()
    song_name=[]
    names=sp.tracks(id_list)
    for track in names['tracks']:
        song_name.append(track['name'])
    sadSongsLink=[]
    sadSongsName=[]
    for i in range(len(prediction)):
        if prediction[i] :
            sadSongsLink.append("https://open.spotify.com/track/"+id_list[i])
            sadSongsName.append(song_name[i])
        sadDict=dict(zip(sadSongsName,sadSongsLink))
    return render_template('sad.html',sadDict=sadDict)

@app.route('/relax',methods=['POST'])
def relax():
    sp=index.sp
    ada=index.ada
    art_id=index.art_id
    recs=emotion.relaxlist(sp,art_id)
    relaxes=pd.DataFrame(recs)
    ids=relaxes['id']

    relaxes=relaxes[features]
    prediction=ada.predict(relaxes)
    id_list=ids.tolist()
    song_name=[]
    names=sp.tracks(id_list)
    for track in names['tracks']:
        song_name.append(track['name'])
    relaxSongsLink=[]
    relaxSongsName=[]
    for i in range(len(prediction)):
        if prediction[i] :
            relaxSongsLink.append("https://open.spotify.com/track/"+id_list[i])
            relaxSongsName.append(song_name[i])
        relaxDict=dict(zip(relaxSongsName,relaxSongsLink))
    return render_template('relax.html',relaxDict=relaxDict)

@app.route('/angry',methods=['POST'])
def angry():
    sp=index.sp
    ada=index.ada
    art_id=index.art_id
    recs=emotion.angrylist(sp,art_id)
    angries=pd.DataFrame(recs)
    ids=angries['id']

    angries=angries[features]
    prediction=ada.predict(angries)
    id_list=ids.tolist()
    song_name=[]
    names=sp.tracks(id_list)
    for track in names['tracks']:
        song_name.append(track['name'])
    angrySongsLink=[]
    angrySongsName=[]
    for i in range(len(prediction)):
        if prediction[i] :
            angrySongsLink.append("https://open.spotify.com/track/"+id_list[i])
            angrySongsName.append(song_name[i])
        angryDict=dict(zip(angrySongsName,angrySongsLink))
    return render_template('angry.html',angryDict=angryDict)



def htmlForLoginButton():
    auth_url = getspOauthURI()
    #htmlLoginButton = "<a href='" + auth_url + "'>Login to spotify</a>" 
    return render_template('login.html',login=auth_url)


# Function for authorizing url

def getspOauthURI():
    auth_url = sp_oauth.get_authorize_url()
    return auth_url

if __name__ == "__main__":
    app.run( port=8080)
