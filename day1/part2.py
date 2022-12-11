def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = [x.rstrip() for x in file.readlines()]

    top_three = [0, 0, 0]

    temp = 0
    for cals in data:
        if cals == "":
            define_top_three(top_three, temp)
            temp = 0
        else:
            temp += int(cals)
    define_top_three(top_three, temp)

    print(sum(top_three))


def define_top_three(top_three, cals):
    if cals > top_three[0]:
        top_three[2] = top_three[1]
        top_three[1] = top_three[0]
        top_three[0] = cals
    elif cals > top_three[1]:
        top_three[2] = top_three[1]
        top_three[1] = cals
    elif cals > top_three[2]:
        top_three[2] = cals


main()