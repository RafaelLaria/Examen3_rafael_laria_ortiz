import numpy as np
import matplotlib.pyplot as plt
 
prof = []
temp = []

with open('mues_marinas.csv', 'r') as f:
    for linea in f:
        linea = linea.strip()
        if not linea:
            continue
        partes = linea.split(',')
        if len(partes) != 2:
            continue

        try:
            p = float(partes[0])
            t = float(partes[1])
            prof.append(p)
            temp.append(t)
        except ValueError:
            continue

temp = np.array(temp)
media = np.mean(temp)
print(media)
for i in temp:
    if i < 20:
        print(len(i))

prof = np.array(prof)

plt.scatter(prof, temp)
plt.title('Profundidad VS Temperatura')
plt.xlabel('Profundidad (metros)')
plt.ylabel('Profundidad (ºC)')
plt.show()

