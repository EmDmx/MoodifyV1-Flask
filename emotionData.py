# Function to gather happy songs and recoomend them



import pandas as pd


def happylist(sp, art_id):

    artresults = sp.current_user_top_artists(limit=100, time_range="medium_term")
    artist = []

    for i, item in enumerate(artresults["items"]):
        artist.append(item["id"])

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
    playlist = sp.user_playlist("spotify", "37i9dQZF1DX0UrRvztWcAU")
    tracks = playlist["tracks"]
    track_items = tracks["items"]

    track_id = []
    # Gelen json response dan şarkıların id lerini alıyor
    for i in range(len(track_items)):
        # print (i, item['id'], '//', item['artists'][0]['name'],'//',item['name'])
        track_id.append(track_items[i]["track"]["id"])

    print("track id:", len(track_id))
    list_features = sp.audio_features(track_id)

    frame_features = pd.DataFrame(list_features)
    frame_features = frame_features[features]

    valence = frame_features["valence"].mean()
    print("valence:", valence)
    energy = frame_features["energy"].mean()
    print("energy:", energy)
    danceability = frame_features["danceability"].mean()
    print("danceability:", danceability)
    acousticness = frame_features["acousticness"].mean()
    print("acousticness:", acousticness)
    # tempo=frame_features['tempo'].mean()
    # print("tempo:",tempo)

    recs = sp.recommendations(
        limit=20,
        seed_artists=artist[:1],
        seed_tracks=track_id[:5],
        country="TR",
        target_danceability=danceability,
        target_valence=valence,
        target_energy=energy,
    )

    # print(recs)

    happy_id = []
    for track in recs["tracks"]:
        happy_id.append(track["id"])
    happy_list = sp.audio_features(happy_id)
    print("recs:", len(happy_list))

    return happy_list


# Function to gather sad songs and recommend them




def sadlist(sp, art_id):

    artresults = sp.current_user_top_artists(limit=100, time_range="medium_term")
    artist = []

    for i, item in enumerate(artresults["items"]):
        artist.append(item["id"])

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
    playlist = sp.user_playlist("spotify", "37i9dQZF1DX7qK8ma5wgG1")
    tracks = playlist["tracks"]
    track_items = tracks["items"]

    track_id = []
    # Gelen json response dan şarkıların id lerini alıyor
    for i in range(len(track_items)):
        # print (i, item['id'], '//', item['artists'][0]['name'],'//',item['name'])
        track_id.append(track_items[i]["track"]["id"])

    print("track id:", len(track_id))
    list_features = sp.audio_features(track_id)

    frame_features = pd.DataFrame(list_features)
    frame_features = frame_features[features]

    valence = frame_features["valence"].mean()
    print("valence:", valence)
    energy = frame_features["energy"].mean()
    print("energy:", energy)
    danceability = frame_features["danceability"].mean()
    print("danceability:", danceability)
    acousticness = frame_features["acousticness"].mean()
    print("acousticness:", acousticness)
    # tempo=frame_features['tempo'].mean()
    # print("tempo:",tempo)

    recs = sp.recommendations(
        limit=20,
        seed_artists=artist[:1],
        seed_tracks=track_id[:5],
        country="TR",
        target_danceability=danceability,
        target_valence=valence,
        target_energy=energy,
    )

    # print(recs)

    sad_id = []
    for track in recs["tracks"]:
        sad_id.append(track["id"])
    sad_list = sp.audio_features(sad_id)
    print("recs:", len(sad_list))

    return sad_list


# relaxlist i toparlar
def relaxlist(sp, art_id):

    artresults = sp.current_user_top_artists(limit=100, time_range="medium_term")
    artist = []

    for i, item in enumerate(artresults["items"]):
        artist.append(item["id"])

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
    playlist = sp.user_playlist("spotify", "37i9dQZF1DWU0ScTcjJBdj")
    tracks = playlist["tracks"]
    track_items = tracks["items"]

    track_id = []
    # Gelen json response dan şarkıların id lerini alıyor
    for i in range(len(track_items)):
        # print (i, item['id'], '//', item['artists'][0]['name'],'//',item['name'])
        track_id.append(track_items[i]["track"]["id"])

    print("track id:", len(track_id))
    list_features = sp.audio_features(track_id)

    frame_features = pd.DataFrame(list_features)
    frame_features = frame_features[features]

    valence = frame_features["valence"].mean()
    print("valence:", valence)
    energy = frame_features["energy"].mean()
    print("energy:", energy)
    danceability = frame_features["danceability"].mean()
    print("danceability:", danceability)
    acousticness = frame_features["acousticness"].mean()
    print("acousticness:", acousticness)
    # tempo=frame_features['tempo'].mean()
    # print("tempo:",tempo)

    recs = sp.recommendations(
        limit=20,
        seed_artists=artist[:1],
        seed_tracks=track_id[:5],
        country="TR",
        target_danceability=danceability,
        target_valence=valence,
        target_energy=energy,
    )

    # print(recs)

    relax_id = []
    for track in recs["tracks"]:
        relax_id.append(track["id"])
    relax_list = sp.audio_features(relax_id)
    print("recs:", len(relax_list))

    return relax_list


# angrylist i toparlar
def angrylist(sp, art_id):

    artresults = sp.current_user_top_artists(limit=100, time_range="medium_term")
    artist = []

    for i, item in enumerate(artresults["items"]):
        artist.append(item["id"])

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
    playlist = sp.user_playlist("a.c.alex", "5c5NfSIO6bMrUSoCZKMudz")
    tracks = playlist["tracks"]
    track_items = tracks["items"]

    track_id = []
    # Gelen json response dan şarkıların id lerini alıyor
    for i in range(len(track_items)):

        track_id.append(track_items[i]["track"]["id"])

    print("track id:", len(track_id))
    list_features = sp.audio_features(track_id)

    frame_features = pd.DataFrame(list_features)
    frame_features = frame_features[features]

    valence = frame_features["valence"].mean()
    print("valence:", valence)
    energy = frame_features["energy"].mean()
    print("energy:", energy)
    danceability = frame_features["danceability"].mean()
    print("danceability:", danceability)
    acousticness = frame_features["acousticness"].mean()
    print("acousticness:", acousticness)
    # tempo=frame_features['tempo'].mean()
    # print("tempo:",tempo)

    recs = sp.recommendations(
        limit=20,
        seed_artists=artist[:1],
        seed_tracks=track_id[:5],
        country="TR",
        target_danceability=danceability,
        target_valence=valence,
        target_energy=energy,
    )

    # print(recs)

    angry_id = []
    for track in recs["tracks"]:
        angry_id.append(track["id"])
    angry_list = sp.audio_features(angry_id)
    print("recs:", len(angry_list))

    return angry_list
