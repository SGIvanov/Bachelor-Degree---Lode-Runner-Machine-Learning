f_inRoot = 'C:\\Users\\silvi\\Desktop\\Note+Credite.txt'
allCredits = 0
averageAll = 0
with open(f_inRoot, 'r') as fin:
    for line in fin:
        array = line.split()
        grade = int(array[0])
        credit = int(array[1])
        allCredits += credit
        averageAll += grade*credit
average = averageAll/allCredits
print("Numar total credite: " + str(allCredits))
print("Suma nota*credite: " + str(averageAll))
print("Medie: " + str(average))
