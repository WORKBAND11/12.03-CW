import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

# Шаг 1: Считываем данные из Excel
file_path = 'Книга15.xlsx'  # Путь к файлу Excel
df = pd.read_excel(file_path)

# Проверяем структуру данных
print(df.head())  # Вывод первых строк для проверки
x = df['x']
y = df['y']
# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()