import pandas as pd
from model.model import Model
import numpy as np
from keras.callbacks import EarlyStopping
import keras
import numpy as np
import matplotlib.pyplot as plt
import timeit
from model.model import Model
from keras.layers import  Conv2D, AveragePooling2D, Dense, Dropout, Flatten, BatchNormalization
import matplotlib.pylab as pylab
from file.filemanager import FileManager
from file.csvmanager import CsvManager
from keras.callbacks import ModelCheckpoint
import pathlib
from pathlib import Path
import tensorflow as tf
import os
import random

model = Model()


model.loadModel("my_model")
# тестирование на пользовательских данных и данные для таблицы
FileHandler = CsvManager()
FileHandler.load("user_dataset.csv", sep=";")

predicts = model.predict(FileHandler.data.iloc[:, 0:14].values.tolist())
reals = FileHandler.data.iloc[:, 14].values.tolist()
accuracy = []
average_accuracy = 0

for i in range(0, len(predicts)):
	acc = predicts[i] / reals[i]
	if acc > 1:
		acc = 1.0 / acc
	average_accuracy += acc
	accuracy.append(str(round(acc * 100.0, 2)) + '%')
average_accuracy = average_accuracy / len(predicts) * 100
table_data = list(zip(reals, predicts, accuracy))

# вывод графика обучения
plt.figure().set_size_inches(6, 6)

#График регрессии
min = min(min(predicts), min(reals)) * 0.7
max = max(max(predicts), max(reals)) * 1.05
x_graph = np.linspace(min, max, 1000)
y_graph = x_graph

plt.plot(x_graph, y_graph, color='black', label='Лучший %')
plt.scatter(reals, predicts, color='green', label='Данные')
plt.xlabel('Исходные')
plt.ylabel('Предсказание')
plt.legend(loc='best')

pylab.xlim(min, max)
pylab.ylim(min, max)

# таблица предиктов
plt.figure().set_size_inches(8, 7)

ax = plt.gca() # (убрать квадрат графика)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.box(on=None)

rcolors = plt.cm.BuPu(np.full(len(table_data), 0.1))
ccolors = plt.cm.BuPu(np.full(3, 0.1))
plt.subplots_adjust(left=0.2, bottom=0.2)
the_table = ax.table(rowLabels=list(range(1, len(table_data)+1)), colLabels=['Настоящее', 'Предсказанное', 'Точность'], cellText=table_data, loc='center', colColours=ccolors, rowColours=rcolors)
the_table.auto_set_font_size(False)
the_table.set_fontsize(16)    
the_table.scale(1, 2)
plt.text(0.37, -0.15, 'Средняя точность: ' + str(round(average_accuracy, 2)) + '%', fontsize=18)

plt.show()