#Bar chart

import matplotlib.pyplot as plt
import numpy as np

# the bar chart will compare the date represented in each category with a bar

Categories = ["0-18", "18-24", "25-35", "36-50", "50-65","65+"]
Values = np.array([4.2, 7.8, 8.3, 7.2, 4.8, 2.9])

plt.bar(Categories, Values, color = "red")
#for a horizontal barchart use (plt.barh())

plt.title("Computer literate people per age range")
plt.xlabel("Age range")
plt.ylabel("Score out of 10")

plt.show()