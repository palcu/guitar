import random

with open('README.md') as stream:
    songs = [line for line in stream.readlines() if '*' in line]
    print(random.choice(songs))
