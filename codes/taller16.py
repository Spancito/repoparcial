import json
import math
with open('dolarTaller16.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

x = [item['id'] for item in data]
y = [item['value'] for item in data]

n = len(x)

prom_x = sum(x)/n
prom_y = sum(y)/n

sxx = sum((xi - prom_x)**2 for xi in x)
syy = sum((yi - prom_y)**2 for yi in y)
sxy = sum((xi - prom_x) * (yi - prom_y) for xi, yi in zip(x,y))

a1 = (sxy/sxx)
a0 = prom_y - a1 * prom_x

sy = math.sqrt((syy / n-1))
sr = sum((yi - (a0 + a1 * xi))**2 for xi, yi in zip(x,y))
sy_x = math.sqrt((sr / n-2))
r2 = ((syy - sr) / syy)
r = math.sqrt(r2)

print(f"Desviación estándar: {sy:.5f}")
print(f"Error estándar (Sy/x): {sy_x:.5f}")
print(f"Coeficiencia de determinación (R^2): {r2:.5f}")
print(f"Coeficiente de correlación (r): {r:.5f}")


