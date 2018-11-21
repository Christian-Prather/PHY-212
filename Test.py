import csv
import matplotlib.pyplot as plt
fileDir = input("What is the file path to the csv: ")
fileToOpen = input ("What is the file name: ")
x = []
y = []
secondX = []
secondY = []



with open('C:\\Users\\Christian\\Documents\\GitHub\\PHY-212\\Sound\\Unknown\\DecibelXDataAugment.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[1]))
        y.append(float(row[0]))

with open('C:\\Users\\Christian\\Documents\\GitHub\\PHY-212\\Sound\\LongX_MidY_Null\\DecibelXDataAugment.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        secondX.append(float(row[1]))
        secondY.append(float(row[0]))
plt.plot(x,y, label='Loaded from file!')
plt.plot(secondX,secondY)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
