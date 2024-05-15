iFile = open("Input1.txt", "r")
oFile = open("Output1.txt", "w")

for line in iFile:
    result = ""
    i = 0
    while i < len(line):
        if i+1 > len(line)-1: 
            result += line[i]
            break
        if line[i] != line[i+1]:
            result += line[i]
        else:
            i += 2
        i += 1
    oFile.write(result)

oFile.close()
