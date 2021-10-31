import matplotlib.pyplot as plt
import numpy as np

sample_figure = plt.figure()

ax1 = ax.add_subplot(121)
ax2 = ax.add_subplot(122)

ax1.hist(data)
ax2.boxplot(data)
plt.show()


# Б) 1- sample_figure.add_subplot(121) 2- sample_figure.add_subplot(122)
# Г) 1- sample_figure.add(1,2,2) 2- sample_figure(1,2,1)
#