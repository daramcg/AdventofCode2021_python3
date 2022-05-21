# Python program for reading
# from file


h = open('inputDay2a.txt', 'r')

# Reading from the file
content = h.readlines()

# Iterating through the content
# Of the file

count = 0
range = len(content)
horizontalPos = 0
depthPos = 0
aim = 0
i=0


while i < range:
    #print(content[i])
    # if the length of the line is more than or equal to 10, it is forward command
    if len(content[i]) >= 10:
        #print(content[i][-2])
        horizontalPos += int(content[i][-2])
        temp = int(content[i][-2])
        depthPos += (aim*temp)

    # if the length of the line is more than or equal to 6, it is down command
    elif len(content[i]) >= 6:
        #print(content[i][-2])
        #depthPos += int(content[i][-2])
        aim+= int(content[i][-2])
    # if the length of the line is more than or equal to 4, it is up command
    elif len(content[i]) >= 4:
        #print(content[i][-2])
        #depthPos -= int(content[i][-2])
        aim -= int(content[i][-2])


    i+=1

print("horizontal position relative to origin after " + str(horizontalPos))
print("depth position relative to origin after " + str(depthPos))
print("Aims is " + str(aim))

finalAns = depthPos * horizontalPos
print("Final result input " + str(finalAns))