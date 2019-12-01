if __name__ == "__main__":
    file = "day1.txt"
    f = open(file, "r")
    sum = 0
    for number in f:
        number = int(number)
        sum += number//3-2
    print(sum)