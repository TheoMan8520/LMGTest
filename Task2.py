iFile = open("Input2.txt", "r")
oFile = open("Output2.txt", "w")

for line in iFile:
    count = 0
    for a in line:
        if a == "(":
            count += 1
        elif a == ")":
            count -= 1
    if count == 0:
        oFile.write("1\n")
    else:
        oFile.write("0\n")

oFile.close()