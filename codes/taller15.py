import matplotlib.pyplot as plt

x = [-3, -2, -1, 0, 1, 2, 3, 4]
y = [4.5, 2, 3, 0.5, 1, -0.5, -1, -2.5]

N = len(x)

sumX = 0
sumY = 0
sumXY = 0
sumX2 = 0

for i in range(N):
    sumX += x[i]
    sumY += y[i]
    sumXY += x[i]*y[i]
    sumX2 += x[i]**2

m = ((N*sumXY)-(sumX*sumY))/((N*sumX2)-(sumX**2))
b = (sumY -(m*sumX))/N

y_pred = [m * xi + b for xi in x]

plt.figure(figsize=(8, 5))

plt.scatter(x, y, color='blue', label='Datos reales', zorder=5)

plt.plot(x, y_pred, color='red', linewidth=2, label=f'Recta: y = {m:.2f}x + {b:.2f}')

plt.xlabel('Variable Independiente (X)')
plt.ylabel('Variable Dependiente (Y)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()