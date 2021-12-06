import sys
input1FileName = sys.argv[1]
input2FileName = sys.argv[2]
input2FileName += ".bin"
input1File = open(input1FileName, "r")
input2File = open(input2FileName, "rb")
text1 = input1File.read()
i = 0
textfin = ""
while True:
    letter = input2File.read(1)
    if not letter:
        break
    letter = letter[0]
    letter = letter ^ ord(text1[i])
    tf = textfin + chr(letter)
    i += 1
print(textfin)
input1File.close()
input2File.close()
