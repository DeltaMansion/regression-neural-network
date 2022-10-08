import numpy as np
import keras.layers
import pickle
import os
from file.csvmanager import CsvManager
from file.filemanager import FileManager
from keras.layers import Dense
from keras.models import Sequential


class Model:

	fileHandler = None
	data = None
	x_train = None
	y_train = None
	x_test = None
	y_test = None
	uniqueValues = {}

	def __init__(self):
		pass

	def prepare(self, show_loading=False):

		"""
		Подготавливает данные, загруженные из файла перед обучением

		:return:
		"""

		if isinstance(self.fileHandler, CsvManager):

			self.columns = self.fileHandler.headers()
			self.data = np.zeros((len(self.fileHandler.data), len(self.fileHandler.headers())))

			if show_loading:
				print("Обработка данных")

			for row in range(len(self.fileHandler.data)):
				for column in self.fileHandler.headers():

					column_index = self.fileHandler.headers().get_loc(column)

					if self.fileHandler[column].dtype == object:
						self.data[row][column_index] = Model.convertUnit(self.uniqueValues[column],
																		 self.fileHandler[column][row])
					elif self.fileHandler[column].dtype == np.float64:
						self.data[row][column_index] = Model.convertFloat(self.fileHandler[column][row])

				if show_loading:
					if row % 1000 == 0:
						print("\r" + str(round(row / len(self.fileHandler.data) * 100, 2)) + "%", end="")

			if show_loading:
				print("\r100%\n")


	def loadCsvData(self,
					path,
					sep=None,
					delimiter=None,
					header='infer',
					names=None,
					index_col=None,
					usecols=None,
					squeeze=None,
					prefix=None,
					mangle_dupe_cols=True,
					dtype=None,
					engine=None,
					converters=None,
					true_values=None,
					false_values=None,
					skipinitialspace=False,
					skiprows=None,
					skipfooter=0,
					nrows=None,
					na_values=None,
					keep_default_na=True,
					na_filter=True,
					verbose=False,
					skip_blank_lines=True,
					parse_dates=None,
					infer_datetime_format=False,
					keep_date_col=False,
					date_parser=None,
					dayfirst=False,
					cache_dates=True,
					iterator=False,
					chunksize=None,
					compression='infer',
					thousands=None,
					decimal='.',
					lineterminator=None,
					quotechar='"',
					quoting=0,
					doublequote=True,
					escapechar=None,
					comment=None,
					encoding=None,
					encoding_errors='strict',
					dialect=None,
					error_bad_lines=None,
					warn_bad_lines=None,
					on_bad_lines=None,
					delim_whitespace=False,
					low_memory=True,
					memory_map=False,
					float_precision=None,
					storage_options=None):

		"""
		Загружает данные из файла по пути path

		:param path: Путь к файлу с данными
		:return:
		"""

		if FileManager.isCsv(path):
			self.fileHandler = CsvManager()
			self.fileHandler.load(path,
								  sep=sep,
								  delimiter=delimiter,
								  header=header,
								  names=names,
								  index_col=index_col,
								  usecols=usecols,
								  squeeze=squeeze,
								  prefix=prefix,
								  mangle_dupe_cols=mangle_dupe_cols,
								  dtype=dtype,
								  engine=engine,
								  converters=converters,
								  true_values=true_values,
								  false_values=false_values,
								  skipinitialspace=skipinitialspace,
								  skiprows=skiprows,
								  skipfooter=skipfooter,
								  nrows=nrows,
								  na_values=na_values,
								  keep_default_na=keep_default_na,
								  na_filter=na_filter,
								  verbose=verbose,
								  skip_blank_lines=skip_blank_lines,
								  parse_dates=parse_dates,
								  infer_datetime_format=infer_datetime_format,
								  keep_date_col=keep_date_col,
								  date_parser=date_parser,
								  dayfirst=dayfirst,
								  cache_dates=cache_dates,
								  iterator=iterator,
								  chunksize=chunksize,
								  compression=compression,
								  thousands=thousands,
								  decimal=decimal,
								  lineterminator=lineterminator,
								  quotechar=quotechar,
								  quoting=quoting,
								  doublequote=doublequote,
								  escapechar=escapechar,
								  comment=comment,
								  encoding=encoding,
								  encoding_errors=encoding_errors,
								  dialect=dialect,
								  error_bad_lines=error_bad_lines,
								  warn_bad_lines=warn_bad_lines,
								  on_bad_lines=on_bad_lines,
								  delim_whitespace=delim_whitespace,
								  low_memory=low_memory,
								  memory_map=memory_map,
								  float_precision=float_precision,
								  storage_options=storage_options
								  )

			self.uniqueValues = {}
			for column in self.fileHandler.headers():
				self.uniqueValues[column] = self.fileHandler.unique(column)

	def splitTrainTest(self, features=[], labels=[], test_size=0.3, shuffle=True):

		"""
		Разделяет набор на тренировочный и тестовый

		:param features: массив с названиями столбцов признаков (массив строк или целых чисел), если пустой или не list, то признаками являются все столбцы, кроме labels
		:param labels: массив меток (массив строк или целых чисел), если пустой, то последний столбец, не входящий в features
		:param test_size: {0.0 -- 1.0} процент тестового набора от общего числа
		:param shuffle: перемешать данные
		:return:
		"""

		if self.data is None:

			if isinstance(self.fileHandler, CsvManager):
				self.data = self.fileHandler.data.to_numpy()

		if isinstance(self.data, np.ndarray):

			if test_size <= 0.0:
				test_size = 0.0
			elif test_size >= 1.0:
				test_size = 1.0

			if shuffle:
				np.random.shuffle(self.data)

			if type(features) is list and len(features):
				# переданы названия столбцов
				if type(features[0]) is str:
					if isinstance(self.fileHandler, CsvManager):
						for i in range(len(features)):
							column_index = self.fileHandler.headers().get_loc(features[i])
							features[i] = column_index

			if type(labels) is list and len(labels):
				# переданы названия столбцов
				if type(labels[0]) is str:
					if isinstance(self.fileHandler, CsvManager):
						for i in range(len(labels)):
							column_index = self.fileHandler.headers().get_loc(labels[i])
							labels[i] = column_index

			# не переданы названия меток
			if len(labels) == 0:
				if isinstance(self.fileHandler, CsvManager):

					allColumnsIndexes = np.array([i for i in range(len(self.fileHandler.headers()))])
					feats = np.array(features)
					# вычитаем из всех столбцов признаки
					columnsWithoutFeatures = np.setdiff1d(allColumnsIndexes, feats)

					if len(columnsWithoutFeatures):
						labels = [columnsWithoutFeatures[-1]]
					else:
						# последний индекс столбцов
						labels = [self.fileHandler.headers().get_loc(self.fileHandler.headers()[-1])]

			if len(features) == 0:
				if isinstance(self.fileHandler, CsvManager):
					allColumnsIndexes = np.array([i for i in range(len(self.fileHandler.headers()))])
					lbls = np.array(labels)
					# вычитаем из всех столбцов метки
					features = np.setdiff1d(allColumnsIndexes, lbls)

			testLen = len(self.data) * test_size
			testLen = int(testLen)

			test = self.data[0:testLen]
			train = self.data[testLen:len(self.data)]

			# признаки для теста
			self.x_test = np.zeros((len(test), len(features)))
			# метки для теста
			self.y_test = np.zeros((len(test), len(labels)))
			# признаки для обучения
			self.x_train = np.zeros((len(train), len(features)))
			# метки для обучения
			self.y_train = np.zeros((len(train), len(labels)))

			row = 0
			for i in range(0, testLen):
				for j in range(len(features)):
					self.x_test[row][j] = self.data[i][features[j]]
				for j in range(len(labels)):
					self.y_test[row][j] = self.data[i][labels[j]]
				row += 1

			row = 0
			for i in range(testLen, len(self.data)):
				for j in range(len(features)):
					self.x_train[row][j] = self.data[i][features[j]]
				for j in range(len(labels)):
					self.y_train[row][j] = self.data[i][labels[j]]
				row += 1

	def initSequential(self,
					   layers=[],
					   optimizer='rmsprop',
					   loss=None,
					   metrics=None,
					   loss_weights=None,
					   weighted_metrics=None,
					   ):

		"""
		Инициализирует модель слоями

		:param layers: массив слоев (наследники Layer)
		:param optimizer: Строка (имя оптимизатора) или экземпляр оптимизатора
		:param loss: Функция потерь
		:param metrics: Список метрик, которые будут оцениваться моделью во время обучения и тестирования
		:param loss_weights: Необязательный список или словарь, определяющий скалярные коэффициенты (число с плавающей запятой Python) для взвешивания потерь, связанных с различными выходными данными модели
		:param weighted_metrics: Список метрик, которые необходимо оценить и взвесить по sample_weight или class_weight во время обучения и тестирования
		:return:
		"""

		self.model = Sequential()

		for layer in layers:
			if isinstance(layer, keras.layers.Layer):
				self.model.add(layer)

		self.model.compile(optimizer=optimizer,
						   loss=loss,
						   metrics=metrics,
						   loss_weights=loss_weights,
						   weighted_metrics=weighted_metrics)

	@staticmethod
	def convertUnit(keys_list, elem):

		try:
			indexesArray = np.where(keys_list == elem)[0]

			if len(indexesArray) != 0:
				return indexesArray[0]

			return -1

		except ValueError:
			return -1

	@staticmethod
	def convertFloat(elem):

		if (elem == ''):
			return -1
		else:
			return float(elem)

	def fit(self,
			x=None,
			y=None,
			batch_size=None,
			epochs=1,
			verbose=1,
			callbacks=None,
			validation_split=0.,
			validation_data=None,
			shuffle=True,
			class_weight=None,
			sample_weight=None,
			initial_epoch=0,
			steps_per_epoch=None,
			validation_steps=None,
			validation_freq=1,
			max_queue_size=10,
			workers=1,
			use_multiprocessing=False):

		"""

		:param x: признаки
		:param y: метки
		:param batch_size: Количество выборок на обновление градиента
		:param epochs: Количество эпох для обучения модели
		:param verbose: 'авто', 0, 1 или 2. Режим детализации. 0 = без звука, 1 = индикатор выполнения, 2 = одна строка в эпоху
		:param callbacks: Список экземпляров keras.callbacks
		:param validation_split: Плавающее значение от 0 до 1. Доля обучающих данных, которые будут использоваться в качестве данных проверки
		:param validation_data: Данные для оценки потерь и любые метрики модели в конце каждой эпохи. Модель не будет обучаться на этих данных
		:param shuffle: необходимо ли перемешивать обучающие данные перед каждой эпохой
		:param class_weight: Необязательный словарь, отображающий индексы класса (целые числа) в весовое (плавающее) значение, используемое для взвешивания функции потерь (только во время обучения)
		:param sample_weight: Необязательный массив весов Numpy для обучающих выборок, используемый для взвешивания функции потерь (только во время обучения)
		:param initial_epoch: Эпоха начала обучения (полезно для возобновления предыдущего тренировочного прогона)
		:param steps_per_epoch: Общее количество шагов (партий выборок) перед объявлением одной эпохи завершенной и началом следующей эпохи
		:param validation_steps: Имеет значение только в том случае, если указана validation_data и она представляет собой набор данных tf.data. Общее количество шагов (партий выборок) для рисования перед остановкой при выполнении проверки в конце каждой эпохи
		:param validation_freq: Актуально только в том случае, если предоставлены данные проверки
		:param max_queue_size: Используется только для ввода генератора или keras.utils.Sequence. Максимальный размер очереди генератора
		:param workers: Используется только для ввода генератора или keras.utils.Sequence. Максимальное количество процессов
		:param use_multiprocessing: Используется только для ввода генератора или keras.utils.Sequence. Если True, используйте многопоточность на основе процессов
		:return:
		"""

		if self.model:
			return self.model.fit(x=x,
						   y=y,
						   batch_size=batch_size,
						   epochs=epochs,
						   verbose=verbose,
						   callbacks=callbacks,
						   validation_split=validation_split,
						   validation_data=validation_data,
						   shuffle=shuffle,
						   class_weight=class_weight,
						   sample_weight=sample_weight,
						   initial_epoch=initial_epoch,
						   steps_per_epoch=steps_per_epoch,
						   validation_steps=validation_steps,
						   validation_freq=validation_freq,
						   max_queue_size=max_queue_size,
						   workers=workers,
						   use_multiprocessing=use_multiprocessing)

		return None

	def loadModel(self, path):

		"""
		Загружает готовую модель по пути path

		:param path: путь с сохраненной моделью
		:return:
		"""

		if os.path.isdir(path):

			self.model = keras.models.load_model(path + "/model.h5")

			if os.path.getsize(path + "/unique.pickle") > 0:
				with open(path + "/unique.pickle", 'rb') as f:
					self.uniqueValues = pickle.load(f)
			else:
				self.uniqueValues = {}

			if os.path.getsize(path + "/columns.pickle") > 0:
				with open(path + "/columns.pickle", 'rb') as f:
					self.columns = pickle.load(f)
			else:
				self.columns = []

			return True

		return False

	def saveModel(self, path):

		"""
		Сохраняет готовую модель по пути path

		:param path: путь по которому нужно сохранить готовую модуль (название папки относительно текущего файла)
		:return:
		"""

		if self.model:

			if not os.path.isdir(path):
				os.mkdir(path)

			self.model.save(path + "/model.h5")

			with open(path + "/unique.pickle", 'wb') as f:
				pickle.dump(self.uniqueValues, f)

			if isinstance(self.fileHandler, CsvManager):
				with open(path + "/columns.pickle", 'wb') as f:
					pickle.dump(self.fileHandler.headers(), f)

			return True

		return False

	def predict(self, data):

		"""
		Возвращает вычесленное значение для подставляемых данных в обученную модель

		:param data: 1d np.array
		:return:
		"""

		predictedData = []

		if self.model:

			if type(data) is list:
				data = np.array(data)

			data = data.reshape((1,)+data.shape)
			rows = 0
			cols = 0

			if data.shape[0] > 0:
				rows = data.shape[0]

			if len(data.shape) == 2 and data.shape[1] > 0:
				cols = data.shape[1]

			preparedData = np.empty(data.shape, dtype=np.object)

			for i in range(rows):
				if len(data.shape) == 2:
					for j in range(cols):
						try:
							preparedData[i][j] = Model.convertFloat(str(data[i][j]))
						except Exception:
							preparedData[i][j] = Model.convertUnit(self.uniqueValues[self.columns[i]], str(data[i][j]))

			predictedData = self.model.predict(np.asarray(preparedData).astype(np.float32))

		return predictedData[0][0]


if __name__ == "__main__":

	model = Model()

	if not model.loadModel("test"):

		model.loadCsvData("../dataset.csv", sep=";")
		model.prepare(show_loading=True)
		model.splitTrainTest(labels=["Price"])
		x_train, y_train, x_test, y_test = model.x_train, model.y_train, model.x_test, model.y_test
		model.initSequential(layers=[
			Dense(len(x_train[0]), input_shape=(len(x_train[0]),), activation='relu'),
			Dense(256, activation='relu'),
			Dense(128, activation='relu'),
			Dense(64, activation='relu'),
			Dense(16, activation='relu'),
			Dense(1, activation='linear')
		],
			optimizer='adam',
			loss='mse',
			metrics=['mse'])

		history = model.fit(x_train, y_train, epochs=50, verbose=2, validation_split=0.2, batch_size=256)
		if model.saveModel("test"):
			print("\n\nSaved")


	data = np.array(['Nissan', 'X-Trail', 57000.0, 2018.0, 'J', 171.0, 'full', 'variator', 'no', 2.0, 380.0, 199.0, 9.50, 6.20])
	print(model.predict(data))



