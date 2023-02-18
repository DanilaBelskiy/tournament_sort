from TournamentSort import tournament_sort
import random

arr = []

for i in range(1000):
    arr.append(random.randint(0, 900))

print(arr)
print(tournament_sort(arr))
