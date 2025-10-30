import matplotlib.pyplot as plt
import numpy as np
# point_x=np.array([0,10,20,30])
# point_y=np.array([0,20,45, 34])
#plt.plot(point_y, marker ='o')
# plt.plot(point_y, marker ='o', linestyle ='dotted')
# plt.show()


point_x=np.arange(10, 100, 10)
point_y=np.arange(20, 200, 20)
print ("point_x =", point_x, "point_y =", point_y)
plt.scatter(point_x, point_y, c="r", marker="*")
plt.show()