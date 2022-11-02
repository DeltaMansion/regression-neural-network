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

seed = 5
os.environ['PYTHONHASHSEED']=str(seed)
np.random.seed(seed)
random.seed(seed)
tf.random.set_seed(seed)
keras.utils.set_random_seed(seed)


np.set_printoptions(formatter={'float': '{: 0.7f}'.format})

model = Model()
model.loadCsvData("dataset.csv", sep=";")
model.prepare(show_loading=True)
model.splitTrainTest(labels=["Price"])
x_train, y_train, x_test, y_test = model.x_train, model.y_train, model.x_test, model.y_test

mm = 6

model.initSequential(layers=[
			Dense(len(x_train[0]), input_shape=(len(x_train[0]),), activation='relu', kernel_initializer='he_normal'),
            BatchNormalization(),
			Dense(128 * mm, activation='relu', kernel_initializer='he_normal'),
            BatchNormalization(),
            Dropout(0.3),
			Dense(64 * mm, activation='relu', kernel_initializer='he_normal'),
            BatchNormalization(),
            Dropout(0.2),
			Dense(16 * mm, activation='relu', kernel_initializer='he_normal'),
            Dropout(0.1),
            Dense(4 * mm, activation='relu', kernel_initializer='he_normal'),
			Dense(1, activation='linear', kernel_initializer='he_normal')
		],
			optimizer='Adam',
			loss='mean_absolute_error')

# обучение
callbacks=[]

SAVE_BEST_MODELS = True
if SAVE_BEST_MODELS == True:
    PATH_TO_SAVE_THINGS = str(pathlib.Path().resolve()) + '\\' + str(os.path.basename(__file__)).replace('.py', '') + '\\'
    checkpoint = ModelCheckpoint(PATH_TO_SAVE_THINGS + 'ep {epoch} - loss {loss:.0f} - val_loss {val_loss:.0f}.h5', verbose=0, monitor='val_loss',save_best_only=True, mode='min')
    callbacks.append(checkpoint)

start_seconds: float = timeit.default_timer()
history = model.fit(x_train, y_train, epochs=5000, verbose=2, batch_size=512, callbacks=callbacks, validation_data = (x_test, y_test))
end_seconds: float = timeit.default_timer()

pivot = history.history['loss'][0] * 1.1
history.history['loss'] = [float(i) for i in history.history['loss'] if int(i) < pivot]

pivot = history.history['val_loss'][0] * 1.1

history.history['val_loss'] = [float(i) for i in history.history['val_loss'] if int(i) < pivot]

best_val_acc = min(history.history['val_loss'])
index_of_best_vall_acc = history.history['val_loss'].index(best_val_acc)
print('current train: ' + str(history.history['loss'][index_of_best_vall_acc]) + ' with best test: ' + str(best_val_acc))

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
plt.figure().set_size_inches(11, 5)

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss', color='#bb3333')
plt.xlabel('Эпохи')
plt.ylabel('loss')
plt.legend(loc='best')
plt.title('Время обучения: ' + str(round(end_seconds - start_seconds, 2)) + ' сек.')

#График регрессии
min = min(min(predicts), min(reals)) * 0.7
max = max(max(predicts), max(reals)) * 1.05
x_graph = np.linspace(min, max, 1000)
y_graph = x_graph

plt.subplot(1, 2, 2)
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

#model.saveModel("my_model")