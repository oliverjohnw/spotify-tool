import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# TODO: add check for JSON
def playlist_load(authorize_json, uri_json):
    """
    Function that loads spotify playlist using spotipy tool

    Parameters
    ----------
    authorize_json : json
        client ID (client_id) and secret key (client_secret)
    uri_json : json
        uri information from spotify
    """
    credentials = json.load(open(authorize_json))
    playlists = json.load(open(uri_json))

    credential_manager = SpotifyClientCredentials(
        client_id = credentials['client_id'],
        client_secret = credentials['client_secret']
    )

    sp = spotipy.Spotify(credential_manager)

    return sp


def playlist_info_format(sp, uri_json):
    """
    Function that formats information from spotify playlist

    Parameters
    ----------
    sp : spotipy object
        loaded spotify playlist infmation
    uri_json : json
        uri information from spotify
    """
    track_info = sp.user_playlist(
        username = uri_json.split(':')[2],
        playlist_id = uri_json.split(':')[4],
        'tracks')

