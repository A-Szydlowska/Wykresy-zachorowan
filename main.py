# Wykresy zachorowań na COVID w Polsce
# https://www.gov.pl/attachment/7152d6ee-4519-4f02-98e4-38376c3705eb

import matplotlib.pyplot as plt
import numpy as np
import csv

names = []
ills = []
deaths = []
result = []
results = []
f = open("28_11_20_wojewodztwa.csv", "r")
reader = csv.DictReader(f, delimiter=";")
for row in reader:
    name = row['Województwo']
    names.append(name)
    ill = int(row['Liczba przypadków'])
    ills.append(ill)
    death = int(row['Zgony'])
    deaths.append(death)
f.close()

x = names[1:]
y = deaths[1:]
z = ills[1:]
width = 0.4
index = np.arange(len(x))
plt.barh(index - width / 2, z, width, label='Zachorowania')
plt.barh(index + width / 2, y, width, label='Zgony')
plt.yticks(index, x)
plt.title('Wykres zachorowań i zgonów na COVID w Polsce')
plt.legend()
plt.show()

plt.pie(ills[1:], autopct='%.2f')
plt.title('Diagram procentowy zakażonych COVID w Polsce')
plt.legend(labels=names[1:], bbox_to_anchor=(1.3, 1))
plt.show()

plt.pie(deaths[1:], autopct='%.2f')
plt.title('Diagram procentowy zgonów przez COVID w Polsce')
plt.legend(labels=names[1:], bbox_to_anchor=(1.3, 1))
plt.show()
