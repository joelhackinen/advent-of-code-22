def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = [x.rstrip() for x in file.readlines()]

    most_calories = 0
    temp = 0
    for cals in data:
        if cals == "":
            if temp > most_calories:
                most_calories = temp
            temp = 0
        else:
            temp += int(cals)
    if temp > most_calories:
        most_calories = temp


    print(most_calories)


main()