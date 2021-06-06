import requests, json

print("""Welcome to bpmDBMaker! You need your Spotify token
If you do not have, then generate this here (https://developer.spotify.com/console/get-audio-features-several-tracks/)
Type your token here!""")
oauth2 = input("> ")

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + oauth2
}

list_ = {}

nowDB = requests.get("https://ire-prod-api.justdancenow.com/v1/songs/published").json()
for song in nowDB:
    try:
        searchQuery = song["name"] + " " + song["artist"]
        search = requests.get("https://api.spotify.com/v1/search?q=" + searchQuery + "&type=track&limit=1&offset=1", headers = headers).json()["tracks"]["items"]
        tempo = requests.get("https://api.spotify.com/v1/audio-features/" + search[0]["id"], headers = headers).json()["tempo"]
        _object = {song["id"]: tempo}
        list_.update(_object)
        print(_object)
    except Exception: pass

json.dump(list_, open("bpmDatabase.json", "w"))