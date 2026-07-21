#pie chart 
import matplotlib.pyplot as plt
import numpy as np
Categories = ["Python", "Java", "C++", "Javascript"]
Values = np.array([100, 87, 64, 91])
colors = ["blue", "red", "green", "purple"]

plt.pie(Values, labels= Categories,
        autopct="%1.1f%%",
        colors = colors,
        explode=[0.2, 0, 0, 0],
        shadow=True,
        startangle=90)

plt.title("REQUESTS FOR EXPERIECE IN ZAMBIA'S JOB MARKETS")

plt.show()