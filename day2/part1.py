def main():
    rules = {
        "A": "C",
        "B": "A",
        "C": "B"
    }

    guide = {
        "Y": "B",
        "X": "A",
        "Z": "C"
    }

    points = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    with open("input.txt", "r", encoding="utf-8") as file:
        data = [x.rstrip() for x in file.readlines()]

    score = 0
    for row in data:
        choice = guide[row[2]]
        if row[0] == choice:
            score += points[choice] + 3
        elif rules[row[0]] == choice:
            score += points[choice] + 0
        else:
            score += points[choice] + 6

    print(score)


main()