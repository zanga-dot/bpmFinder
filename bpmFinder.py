import json

print("""Welcome to bpmFinder. You need bpmDatabase.json for working with this tool!
Type your tempo (BPM)""")
tempo = float(input("> "))

with open("bpmDatabase.json") as f: bpmDB = json.load(f)

for song in list(bpmDB):
    if (int(bpmDB[song]) == tempo): print(song + " can be fitted. Tempo: " + str(bpmDB[song]))
input()