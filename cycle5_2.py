import matplotlib.pyplot as plt

height=[160,162,164,167,170,171,174,177,179,180,155,154,152,168,172,155,150,158,180]

plt.hist(height, bins=5, color='lightgreen', edgecolor='black')

plt.xlabel('Height (in cm)')
plt.ylabel('No of students')

plt.title('Height Distribution of Students')
plt.show()