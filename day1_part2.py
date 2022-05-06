# Python program for reading
# from file


h = open('inputDay1.txt', 'r')

# Reading from the file
content = h.readlines()

# Iterating through the content
# Of the file

a = []
b = []
c = []
count = 0
range = len(content)
i=0
while i < range:
    j = i+1

    if i+2 <range:
        a = [content[i], content[i+1], content[i+2]]
        #print(a)
    if j+2 <range:
        b = [content[j], content[j + 1], content[j + 2]]
        #print(b)

    sumA = int(a[0])+ int(a[1]) + int(a[2])
    #print(sumA)
    sumB = int(b[0]) + int(b[1]) + int(b[2])
    #print(sumB)
    if sumB > sumA:
        count+=1
    i+=1

print(count)