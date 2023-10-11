ranking = {
    "A":100,
    "B":80,
    "C":90
}

print(ranking)
print(ranking["A"])
print(sorted(ranking))
print(sorted(ranking, key=ranking.get))

print(ranking.items())

