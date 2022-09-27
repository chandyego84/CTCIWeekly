setA = set()
for i in [-3, -2, -1, 1, 2, 3]:
    for j in [-3, -2, -1, 1, 2, 3]:
        if ((1/i - 1/j) in [-3, -2, -1, 0, 1, 2, 3]):
            setA.add((i, j))

print(len((setA)))