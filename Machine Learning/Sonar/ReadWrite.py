class FileOperations:
    def FileWrite(self, file, text):
        file = open(str(file), "w", encoding="utf8")
        file.write(text)
        file.close()

    def FileRead(self, file, count = 1):
        file = open(str(file), "r", encoding="utf8")
        for i in range(0, count):
            outputvar = file.readline()
        file.close()
        return outputvar

    def FileAppend(self, file, text):
        file = open(str(file), "a", encoding="utf8")
        file.write(text)
        file.close()

    def FileFindLines(self, file):
        Filecontence = file.read()
        outputlist = Filecontence.split("\n")
        return outputlist

"""
operate = FileOperations()
Name = input("What is your name? ")

operate.FileWrite("File", Name)
out = operate.FileRead("File")

print("Hello " + out)
"""
