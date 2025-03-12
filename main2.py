import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')

# Шаг 1: Считываем данные из Excel
file_path = 'Книга15.xlsx'  # Путь к файлу Excel
df = pd.read_excel(file_path)

x = df['x']
# Проверяем структуру данных
print(df.head())  # Вывод первых строк для проверки

# plot
fig, ax = plt.subplots()
ax.pie(x, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()