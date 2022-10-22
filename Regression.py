from keras.callbacks import EarlyStopping
import numpy as np
import matplotlib.pyplot as plt
import timeit
from model.model import Model
from keras.layers import Dense
import matplotlib.pylab as pylab
from file.filemanager import FileManager
from file.csvmanager import CsvManager
np.set_printoptions(formatter={'float': '{: 0.7f}'.format})

model = Model()
model.loadCsvData("dataset.csv", sep=";")
model.prepare(show_loading=True)
model.splitTrainTest(labels=["Price"])
x_train, y_train, x_test, y_test = model.x_train, model.y_train, model.x_test, model.y_test

mm = 8
model.initSequential(layers=[
			Dense(len(x_train[0]), input_shape=(len(x_train[0]),), activation='relu'),
			Dense(128 * mm, activation='relu'),
			Dense(64 * mm, activation='relu'),
			Dense(16 * mm, activation='relu'),
            Dense(4 * mm, activation='relu'),
			Dense(1, activation='linear')
		],
			optimizer='adam',
			loss='mse',
			metrics=['mse'])

# обучение
start_seconds: float = timeit.default_timer()
history = model.fit(x_train, y_train, epochs=5, verbose=2, validation_split=0.2, batch_size=256)
end_seconds: float = timeit.default_timer()

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
plt.plot(history.history['mse'], label='mse', color='#bb3333')
plt.plot(history.history['val_mse'], label='val_mse')
plt.xlabel('Эпохи')
plt.ylabel('mse')
plt.legend(loc='best')
plt.text(0.1, 0.1005, 'Время обучения: ' + str(end_seconds - start_seconds) + ' сек.')

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