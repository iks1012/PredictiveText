import os, sys

# file = open("TextData\\cambp10.txt");
fileNames = os.listdir("TextData\\")
masterFile = open("RefinedData.txt", "a")
for i in range(len(fileNames)):
    file = open("TextData\\"+fileNames[i], "r")
    lines = file.read().split("\n")
    for j in range(len(lines)):
        capitalLetterIndex = 0
        capitalFound = False
        for k in range(len(lines[j])):
            if not capitalFound:
                if lines[j][k].isupper():
                    capitalLetterIndex = k
                    capitalFound = True

        masterFile.write(lines[j][capitalLetterIndex:] + "\n\n")









