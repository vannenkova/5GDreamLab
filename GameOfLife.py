#!/usr/bin/env python
# coding: utf-8

# In[14]:


#закрузка неодходимых пакетов
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from IPython import display
import time
#получение информации о размере поля от пользователя (игрока) 
ncol = int(input('Введите длину поля (количество клеток) не менее 5: '))
nrow = ncol #предполагается, что поле всегда будет квадратным

#инициализация поля в начальном состоянии
#определение центрального индекса в зависимости от размера поля
if ncol%2 != 0:
    midpoint = int(st.median(list(range(ncol))))
else:
    midpoint = int(st.median(list(range((ncol)))) + 0.5)
    
#создание пустого массива("поля") для дальнейшей визуализации
#пустым клеткам соответствуют нули
dots = np.zeros((ncol*nrow), dtype=int)
#определение индексов клеток в начальном состоянии
cell_id = [midpoint + (ncol * (midpoint - 2)), 
           (midpoint + 1) + (ncol * (midpoint - 1)),
           (midpoint - 1) + (ncol * (midpoint - 1)),
           (midpoint + 1) + (ncol * midpoint),
           (midpoint - 1) + (ncol * midpoint),
           (midpoint + 2) + (ncol * midpoint),
           (midpoint - 2) + (ncol * midpoint),
           (midpoint + 1) + (ncol * (midpoint + 1)),
           (midpoint - 1) + (ncol * (midpoint + 1)),
           midpoint + (ncol * (midpoint + 2))]
filled_values = list([1]*10) #заполненным клеткам соответствуют единицы
dots[cell_id] = filled_values #заполнение массива клетками в начальном состоянии

game_dots = np.array(dots.reshape((nrow, ncol))) #придание массиву квадратной формы поля
fig, ax = plt.subplots() #визуализация поля в начальном состоянии
ax.imshow(game_dots, cmap="Blues", vmin=0)
plt.show()
display.clear_output(wait=True) #подготовка поля для визуализации следующего поколения
time.sleep(0.5) #визуализация поколения через каждые полсекунды

while sum(dots) > 0: #реализация поколений до тех пор, пока поле не опустеет
    neighbourhood = []
    for i in range(len(dots)): #определение индексов соседей каждой клетки
        id1 = i-ncol
        id2 = i+ncol
        id3 = i+1
        id4 = i-1
        id5 = i-ncol+1
        id6 = i-ncol-1
        id7 = i+ncol+1
        id8 = i+ncol-1
        id_list = [id1, id2, id3, id4, id5, id6, id7, id8]
        neighbours = []
        for a in id_list: #исключение индексов, выходящих за пределы поля
            if a > -1 and a < (ncol*nrow):
                neighbours.append(dots[a])
        neighbourhood.append(sum(neighbours)) #поиск количества заполненных соседей для каждой клетки
    
    #проверка условий для изменения состояния клетки
    old_dots = list(dots)
    for i in range(len(dots)):
        if dots[i] == 0:
            if neighbourhood[i] == 3:
                dots[i] = 1
        elif dots[i] == 1:
            if neighbourhood[i] < 2 or neighbourhood[i] > 3:
                dots[i] = 0
    new_dots = list(dots) 
    if old_dots != new_dots: #проверка на наличие клеток, подлежащих изменению
        game_dots = np.array(dots.reshape((nrow, ncol))) #придание массиву квадратной формы поля
        fig, ax = plt.subplots() #визуализация поля в измененном состоянии
        ax.imshow(game_dots, cmap="Blues", vmin=0)
        plt.show()
        display.clear_output(wait=True) #подготовка поля для визуализации следующего поколения
        time.sleep(0.5) #визуализация поколения через каждые полсекунды
    else:
        break

print("Игра окончена")


# In[ ]:




