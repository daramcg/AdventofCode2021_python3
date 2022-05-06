# Python program for reading
# from file


h = open('inputDay1.txt', 'r')

# Reading from the file
content = h.readlines()

# Iterating through the content
# Of the file

count = 0
range = len(content)
i=0
while i < range:
    print(content[i])

    if int(content[i]) > int(content[i-1]):
        count+=1
    i+=1

print(count)