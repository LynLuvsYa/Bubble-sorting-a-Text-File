def strippingline(): # after each line in the text file, it gets rid of the \n and just stores it in lines
    data = textfile.readline()
    data = data.rstrip()
    while data != "":
        lines.append(data)
        data = textfile.readline()
        data = data.rstrip()
        
def bubblesort(lines): # as the name states, it bubble sorts the lines array so that it is in alphabetical order
    print(lines)
    for x in range(0,len(lines)):
        for y in range(0,len(lines)-1):
            if lines[y] > lines[y + 1]:
                temp = lines[y + 1]
                lines[y + 1] = lines[y]
                lines[y] = temp
    print(lines)
    return lines

def rbubblesort(lines): # as the name states, it bubble sorts the lines array so that it is in alphabetical order
    for x in range(0,len(lines)):
        for y in range(0,len(lines)-1):
            if lines[y] < lines[y + 1]:
                temp = lines[y + 1]
                lines[y + 1] = lines[y]
                lines[y] = temp
    print(lines)
    return lines

def rewritedata(): # completely clears the text file, then puts the sorted values in order into the text file.
    print(lines)
    textfile = open("Untitled.txt", "w")
    textfile.truncate()
    textfile = open("Untitled.txt", "w")
    for x in range(0,len(lines)):
        lines[x] += "\n"
        textfile.write(lines[x])
    
textfile = open("Untitled.txt", "r")
lines = []
strippingline()
textfile.close()
if int(input("sort alphabetically or reverse alphabetically? Alphabetically = 1, Reverse Alphabetically = 2 \n")) == 1:
    lines = bubblesort(lines)
else:
    lines = rbubblesort(lines)
rewritedata()



