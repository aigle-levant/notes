arr = np.array([["Shame", "Hangin'", "Glory", "My Blood"],["Riptide","The Nights", "Warmth", "Of The Night"]])
for i in np.nditer(arr[:, ::2]):
    print(i)