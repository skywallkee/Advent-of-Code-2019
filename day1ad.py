if __name__ == "__main__":
    file = "day1ad.txt"
    f = open(file, "r")
    sum = 0
    for number in f:
        number = int(number)
        while number//3-2 > 0:
            number = number//3-2
            sum = sum + number
    print(sum)