import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import re

load_dotenv()

client_credentials_manager = SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
)

sp = spotipy.Spotify(client_credentials_manager = 
                    client_credentials_manager)

playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]

track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

# print(track_uris)

# for track in sp.playlist_tracks(playlist_URI)["items"]:
    
#     # URI 
#     track_uri = track["track"]["uri"]
#     print(track_uri)

#     # Track Name
#     track_name = track["track"]["name"]
#     print(track_name)

#     # Main Artist
#     artist_uri = track["track"]["artists"][0]["uri"]
#     artist_info = sp.artist(artist_uri)
#     print(artist_uri)
#     print(artist_info)

#     # name, popularity, genres
#     artist_name = track["track"]["artists"][0]["name"]
#     artist_pop = artist_info["popularity"]
#     artist_genres = artist_info["genres"]

#     print(artist_name)
#     print(artist_pop)
#     print(artist_genres)

#     # Album
#     album = track["track"]["album"]["name"]
#     print(album)

#     # Popularity of the track
#     track_pop = track["track"]["popularity"]
#     print(track_pop)

#     print("-"* 50)
    

def uri_to_features(uri):
    features = sp.audio_features(uri)[0]
    
    #Artist of the track, for genres and popularity
    artist = sp.track(uri)["artists"][0]["id"]
    artist_pop = sp.artist(artist)["popularity"]
    artist_genres = sp.artist(artist)["genres"]
    
    #Track popularity
    track_pop = sp.track(uri)["popularity"]
    
    #Add in extra features
    features["artist_pop"] = artist_pop
    if artist_genres:
        features["genres"] = " ".join([re.sub(' ','_',i) for i in artist_genres])
    else:
        features["genres"] = "unknown"
    features["track_pop"] = track_pop
    
    return features

if __name__ == "__main__":
    
    result = uri_to_features("1o0nAjgZwMDK9TI4TTUSNn")
    print(result)