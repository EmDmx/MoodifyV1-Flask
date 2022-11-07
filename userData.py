# Function to get Id's of the tracks which are the user listens the most

import pandas as pd


def topTrackId(sp):
    # User top track bilgilerini alıyor
    results = sp.current_user_top_tracks(
        limit=50,
        time_range="medium_term",
    )

    track_id = []

    # Gelen json response dan şarkıların id lerini alıyor
    for i, item in enumerate(results["items"]):
        # print (i, item['id'], '//', item['artists'][0]['name'],'//',item['name'])
        track_id.append(item["id"])
    return track_id


# Getting Features of the most listened tracks


def topTrackFeatures(sp, track_id):

    # gelen şarkı id lerinin feature larını alıyor
    top_analysis = sp.audio_features(track_id)
    return top_analysis


# Getting the Id's of most listened songs of user's favorite Artists


def topArtistTrackId(sp):

    # User top artist bilgilerini alıyor
    artresults = sp.current_user_top_artists(limit=100, time_range="medium_term")

    artanalysis = []
    # kullanıcının en çok dinlediği müzisyenlerin şarkı bilgisi
    for i, item in enumerate(artresults["items"]):

        artanalysis.append(sp.artist_top_tracks(item["id"], country="TR"))

    # müzisyenlerinin en ünlü şarkılarının id'lerinin bir listeye atılması
    art_track = []
    for i in range(len(artanalysis)):
        for k in range(len(artanalysis[i]["tracks"])):
            # print (artanalysis[i]['tracks'][k]['id'])
            art_track.append(artanalysis[i]["tracks"][k]["id"])

    # Liste duplicate veri içeriyor mu kontrolü
    # print("art_track1",len(art_track))
    art_track = list(set(art_track))
    return art_track


# Getting the Features of most famous songs of Artists


def topArtistTrackFeatures(sp, art_track):

    # isteği yaparken array çok uzun bir url oluşturduğu için array i bölmek zorundayız
    # list'de genelde 400 den fazla şarkı bulunacağı için ve maksimum istek miktarı 100 olduğu için 5 e böldük
    total_list = []

    # listenin bölünmesi
    list0 = art_track[0:100]
    list1 = art_track[100:200]
    list2 = art_track[200:300]
    list3 = art_track[300:400]
    list4 = art_track[400:]
    # her liste için ayrı ayrı istek atılması ve birleştirilmesi
    total_list = total_list + sp.audio_features(list0)
    total_list = total_list + sp.audio_features(list1)
    total_list = total_list + sp.audio_features(list2)
    total_list = total_list + sp.audio_features(list3)
    total_list = total_list + sp.audio_features(list4)

    return total_list


def newdata(sp, top_analysis, art_id):

    features = [
        "danceability",
        "loudness",
        "valence",
        "energy",
        "instrumentalness",
        "acousticness",
        "key",
        "speechiness",
        "duration_ms",
    ]

    top_data = pd.DataFrame(top_analysis)
    top_id = top_data["id"]
    top_data = top_data[features]
    # top listesine relevance değerleri atıyor
    fifty = list(range(1, 51))
    top_data["relevance"] = fifty[::-1]

    top_data["r_valence"] = top_data["valence"] * top_data["relevance"]
    top_data["r_energy"] = top_data["energy"] * top_data["relevance"]
    top_data["r_danceability"] = top_data["danceability"] * top_data["relevance"]
    top_data["r_speechiness"] = top_data["speechiness"] * top_data["relevance"]
    # top_data['r_tempo']=top_data['tempo']*top_data['relevance']
    top_data["r_acousticness"] = top_data["acousticness"] * top_data["relevance"]

    # 1275'e böleriz çünkü (n*n+1)/2 50 tane item var
    top_mean_valence = (top_data["r_valence"].sum()) / 1275
    # print("top valence:",top_mean_valence)
    top_mean_energy = (top_data["r_energy"].sum()) / 1275
    # print("top energy:",top_mean_energy)
    top_mean_danceability = (top_data["r_danceability"].sum()) / 1275
    # print("top_danceability:",top_mean_danceability)
    top_mean_speechiness = (top_data["r_speechiness"].sum()) / 1275
    # print("top_speechiness:",top_mean_speechiness)
    # top_mean_tempo=(top_data['r_tempo'].sum())/1275
    # print("top_tempo:",top_mean_tempo)
    top_mean_acousticness = (top_data["r_acousticness"].sum()) / 1275
    # print("top_acousticness:",top_mean_acousticness)

    artresults = sp.current_user_top_artists(limit=100, time_range="medium_term")
    artist = []

    for i, item in enumerate(artresults["items"]):
        artist.append(item["id"])

    seed_track = top_id.tolist()
    # recommend şarkı almak için kurallar
    # rules for song recommendations
    # for valence
    if top_mean_valence > 0.3:
        max_valence = 3
        min_valence = None
    else:
        max_valence = None
        min_valence = 3
    # for energy
    if top_mean_energy > 0.5:
        max_energy = 0.5
        min_energy = None
    else:
        max_energy = None
        min_energy = 0.5
    # for danceability
    if top_mean_danceability > 0.5:
        max_danceability = 0.5
        min_danceability = None
    else:
        max_danceability = None
        min_danceability = 0.5
    # for acousticness
    if top_mean_acousticness > 0.5:
        max_acousticness = 0.5
        min_acousticness = None
    else:
        max_acousticness = None
        min_acousticness = 0.5
    # for tempo
    """if top_mean_tempo>110:
        max_tempo=110
        min_tempo=None
    else:
        max_tempo=None
        min_tempo=110"""

    #!!!KENDİNE HATIRLATMA !!! bunu çalıştırmak için kütüphanenin client.py dosyasındaki seed_artist kısmında virgül eklenen kısmı sildin.
    recs = sp.recommendations(
        limit=100,
        seed_artists=artist[45:],
        seed_tracks=seed_track[-3:],
        country="TR",
        max_valence=max_valence,
        min_valence=min_valence,
        max_energy=max_energy,
        min_energy=min_energy,
        max_danceability=max_danceability,
        min_danceability=min_danceability,
    )
    bad_id = []
    for track in recs["tracks"]:
        bad_id.append(track["id"])
    bad_list = sp.audio_features(bad_id)
    # bad_list=pd.DataFrame(bad_list)
    print(len(bad_list))
    return bad_list
