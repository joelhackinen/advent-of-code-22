def main():
    rules_win = {
        # {key: value} means "key wins value"
        "A": "C",
        "B": "A",
        "C": "B"
    }

    rules_lose = {
        # {key: value} means "key loses to value"
        "A": "B",
        "B": "C",
        "C": "A"
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
        if row[2] == "Y":
            score += points[row[0]] + 3
        elif row[2] == "X":
            score += points[rules_win[row[0]]] + 0
        else:
            score += points[rules_lose[row[0]]] + 6

    print(score)


main()