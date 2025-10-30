#  import matplotlib.pyplot as plt
#  import numpy as np
#  y = np.array([35, 25, 25, 15])
#  mylabels = ["Apples", "Bananas", 
# "Cherries", "Dates"]
#  plt.pie(y, labels = mylabels)
#  plt.legend()
#  plt.show() 

import matplotlib.pyplot as plt
import numpy as np
xpt = np.array([100,200,300,900,400])
ypt = np.array([10,20,30,90,40])

# plt.plot(xpt,ypt, color="blue" )
# plt.xlabel("score")
# plt.ylabel("student number")
# plt.grid(color="red")
# plt.show()

plt.pie(ypt, labels=["green" ,  "orange", "blue","yellow", "red"], colors=["green" ,  "orange", "blue","yellow", "red"])
plt.legend()
plt.show()