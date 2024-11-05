def heie(ordbok):
    if ordbok["Brann"] <= 3:
        return "Brann"
    else:
        for lag in ordbok:
            if ordbok[lag] == 1:
                return lag
