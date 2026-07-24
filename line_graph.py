#line graph

import matplotlib.pyplot as plt 

x=[2016, 2017, 2019, 2020, 2021, 2022]
#y1=[0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
y1=[80, 50, 100, 80, 95, 75] #whales
y2=[10, 50, 90, 120, 140, 180] #bears
y3=[150,75, 30, 10, 6, 0] #Dolphins

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.title("Wildlife population")
plt.show()