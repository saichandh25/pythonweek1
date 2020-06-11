file = open("txtfile.txt" , 'r') #open the file in read mode
count = {} # created an empty dict
line = file.readline() #read the firstline
newline = line.strip() #strip the spaces and newline char

while newline!="":
    for x in newline.split(" "): #split the words using space
        if x in count:
            count[x] = count[x]+1
        else:
            count[x] = 1
    line = file.readline() #again moves to the new line
    newline = line.strip()

for key in count:
    countstr = key+"--->"+str(count[key])
    print(countstr)
    wrt = open("txtfile.txt","a")
    wrt.write('\n')
    wrt.write(countstr) #append the word count content into the file
