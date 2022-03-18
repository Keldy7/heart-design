import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2200,100000)
x = 16 * np.sin(t) ** 3 + 25
y = 13 * np.cos(t) - 5 * np.cos(2 * t)- 2 * np.cos(3 * t) - np.cos(4 * t) + 20
plt.figure(figsize =(7, 5))
plt.plot(x, y, color = "red", linewidth = 5)
plt.text(10.5, 20, "Favorite Programming Language", fontsize = 20, color= "red")
plt.text(15, 17, "I like Python", fontsize = 20, color= "black")

plt.show()