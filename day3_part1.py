# Python program for reading
# from file


h = open('inputDay3.txt', 'r')

# Reading from the file
content = h.readlines()

# Iterating through the content
# Of the file

gamma = ""
epsilon = ""
count1 = 0
count0 = 0
range2 = len(content)
j = 0
while j < 13 :
    count1 = 0
    count0 = 0
    i = 0
    while i < range2:

        #print(content[i])
        if content[i][j] == "1":
            count1 += 1

        elif content[i][j] == "0":
            count0 += 1
        i += 1

    print("Count of 0s for this iteration is: " + str(count0))
    print("Count of 1s for this iteration is: " + str(count1))
    print("Length of the line is " + str(len(content[i-1])))

    if count1 > count0:
            gamma += "1"
            print("Updating Gamma, tagging on a 1: " + gamma)
    elif count0 > count1:
            gamma += "0"
            print("Updating Gamma, tagging on a 0: " + gamma)

    j += 1






print("GAMMA: " + str(gamma))
x= 0
while x < len(gamma):
    if gamma[x] == "1":
        temp = "0"
    elif gamma[x] == "0":
        temp = "1"
    epsilon = epsilon + temp
    x += 1


print("EPSILON: " + str(epsilon))



length = len(gamma)
gamma = int(gamma)
m = 1
dec_num = 0
for k in range(length):
    reminder = gamma % 10
    dec_num = dec_num + (reminder * m)
    m = m * 2
    gamma = int(gamma/10)
gammaInt = dec_num
print("Equivalent Decimal Value of gamma = ", dec_num)

length = len(epsilon)
epsilon = int(epsilon)
m = 1
dec_num = 0
for k in range(length):
    reminder = epsilon % 10
    dec_num = dec_num + (reminder * m)
    m = m * 2
    epsilon = int(epsilon/10)

epsilonInt = dec_num
print("Equivalent Decimal Value of epsilon = ", dec_num)


print("Product : " + str(epsilonInt*gammaInt))