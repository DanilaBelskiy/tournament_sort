from TournamentSort import tournament
import random


for j in range(6):

    arr = []
    for i in range(10):
        arr.append(random.randint(0, 9))

    arr.sort()
    print(arr)

