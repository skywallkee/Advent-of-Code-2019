if __name__ == "__main__":
    f = "day2.txt"
    file = open(f, "r")
    line = file.readline()
    line = line.strip("\n").split(",")
    for index in range(0, len(line)):
        line[index] = int(line[index])
    # Adding one to position 1 will add 230400 at the final result
    line[1] = 82
    # Adding one to position 1 will add 1 at the final result
    line[2] = 98
    index = 0
    while index < len(line):
        line[index] = int(line[index])
        if line[index] == 99:
            break
        else:
            op1 = line[index + 1]
            op2 = line[index + 2]
            position = line[index + 3]
            nr1 = line[op1]
            nr2 = line[op2]
            if line[index] == 1:
                line[position] = nr1 + nr2
            elif line[index] == 2:
                line[position] = nr1 * nr2
        index += 4
    print(line[0])