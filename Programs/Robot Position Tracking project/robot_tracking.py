import numpy as np
import matplotlib.pyplot as plt

x = 0
y = 0

x_position = []
y_position = []

x_noisy = []
y_noisy = []

x_kalman = []
y_kalman = []

x_est = 0
y_est = 0

alpha = 0.2   


for i in range(10):   
  x = x + 1.2
  y = y + 0.5

  x_position.append(x)
  y_position.append(y)

  x_noise = np.random.normal(0, 1)
  y_noise = np.random.normal(0, 1)

  x_noisy.append(x + x_noise)
  y_noisy.append(y + y_noise)

  x_est = x_est + alpha * (x_noisy[-1] - x_est)
  y_est = y_est + alpha * (y_noisy[-1] - y_est)

  x_kalman.append(x_est)
  y_kalman.append(y_est)



print(x_position)  
print(y_position)

#plt.plot(x_position, y_position, marker='o')
plt.plot(x_position, y_position, marker='o', label="True Path")
plt.plot(x_noisy, y_noisy, 'ro--', label="Noisy Path")
plt.plot(x_kalman, y_kalman, 'b-', label="Filtered Path")

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Robot Movement Path")
plt.legend()
plt.grid()
plt.show()

