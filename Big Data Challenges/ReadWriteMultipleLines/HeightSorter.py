from ReadWrite import *

operate = FileOperations()

print("Clearing Output...")
operate.FileWrite("heights_filtered.csv", "")

print("Reading Data...")
textIn = open("more_heights.csv", "r", encoding="utf8")
textList = operate.FileFindLines(textIn)
textIn.close()

print("Beginning Sorting...")
printOut = ""
maximum_height = 0

for object in textList:
    if float(object) > 200:
        print(object)
        printOut += object + "/n"
    if float(object) > maximum_height:
        maximum_height = float(object)

operate.FileAppend("heights_filtered.csv", printOut + str(maximum_height))
