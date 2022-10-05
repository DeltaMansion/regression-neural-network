from file.filemanager import FileManager
import pandas as pd
import numpy as np


class CsvManager(FileManager):
	data = None

	def __init__(self, path):
		self.load(path)

	def __init__(self):
		pass

	def save(self,
			 path,
			 sep=',',
			 na_rep='',
			 float_format=None,
			 columns=None,
			 header=True,
			 index=True,
			 index_label=None,
			 mode='w',
			 encoding=None,
			 compression='infer',
			 quoting=None,
			 quotechar='"',
			 lineterminator=None,
			 chunksize=None,
			 date_format=None,
			 doublequote=True,
			 escapechar=None,
			 decimal='.',
			 errors='strict',
			 storage_options=None):

		"""
		Сохраняет данные в файл по пути path

		:param path: путь к файлу
		:param sep: Разделитель полей для выходного файла
		:param na_rep: заполнитель для отсутствующих данных
		:param float_format: Строка формата для чисел с плавающей запятой
		:param columns: Столбцы для записи
		:param header: названия столбцов
		:param index: имена строк (индекс)
		:param index_label: Метка столбца для столбца (столбцов) индекса, если это необходимо
		:param mode: Режим записи Python. Доступные режимы записи такие же, как и в open().
		:param encoding: Строка, представляющая кодировку для использования в выходном файле, по умолчанию — «utf-8»
		:param compression: Для оперативного сжатия выходных данных. Если 'infer' и 'path_or_buf' аналогичны пути, то обнаружите сжатие из следующих расширений: '.gz', '.bz2', '.zip', '.xz', '.zst', '.tar' , '.tar.gz', '.tar.xz' или '.tar.bz2' (в противном случае без сжатия)
		:param quoting:
		:param quotechar: Символ, используемый для кавычек полей
		:param lineterminator: Символ новой строки или последовательность символов для использования в выходном файле
		:param chunksize: Кол-во строки записываемых за раз.
		:param date_format: Строка формата для объектов datetime
		:param doublequote: Контролировать цитирование кавычек внутри поля
		:param escapechar: Символ, используемый для экранирования sep и кавычек, когда это необходимо
		:param decimal: Символ, распознанный как десятичный разделитель
		:param errors: Указывает, как должны обрабатываться ошибки кодирования и декодирования
		:param storage_options: Дополнительные параметры, которые имеют смысл для конкретного подключения к хранилищу, например. хост, порт, имя пользователя, пароль и т. д.
		:return:
		"""

		if not isinstance(path, pd.DataFrame) or not FileManager.isCsv(path):
			return False

		self.data.to_csv(path,
						 sep=sep,
						 na_rep=na_rep,
						 float_format=float_format,
						 columns=columns,
						 header=header,
						 index=index,
						 index_label=index_label,
						 mode=mode,
						 encoding=encoding,
						 compression=compression,
						 quoting=quoting,
						 quotechar=quotechar,
						 lineterminator=lineterminator,
						 chunksize=chunksize,
						 date_format=date_format,
						 doublequote=doublequote,
						 escapechar=escapechar,
						 decimal=decimal,
						 errors=errors,
						 storage_options=storage_options)

		return True

	def load(self,
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
		Загружает данные из файла

		:param path: путь к файлу
		:param sep: разделитель
		:param delimiter: псевдоним для sep
		:param header: номер(а) для использования в качестве имен столбцов и начала данных
		:param names: список имен столбцов для использования
		:param index_col: столбец (столбцы) для использования в качестве меток строк DataFrame, либо в виде имени строки,либо в виде индекса столбца
		:param usecols: возвращает подмножество столбцов
		:param squeeze: если данные содержат только один столбец, возвращает Series
		:param prefix: Префикс для добавления к номерам столбцов, когда нет заголовка, например. «X» для X0, X1, …
		:param mangle_dupe_cols: Дублирующиеся столбцы будут указаны как «X», «X.1», … «X.N», а не «X»… «X». Передача False приведет к перезаписыванию данных, если в столбцах есть повторяющиеся имена.
		:param dtype: Тип данных для данных или столбцов. Например. {‘a’: np.float64, ‘b’: np.int32, ‘c’: ‘Int64’}
		:param engine: {‘c’, ‘python’, ‘pyarrow’} Используемый движок парсера
		:param converters: Словарь функций для преобразования значений в определенных столбцах
		:param true_values: Значения, которые следует считать как True
		:param false_values: Значения, которые следует считать как False
		:param skipinitialspace: Пропускать пробелы после разделителя
		:param skiprows: Номера строк для пропуска (0-индексированные) или количество строк для пропуска (int) в начале файла
		:param skipfooter: Количество строк в нижней части файла, которые нужно пропустить (не поддерживается для engine=’c’)
		:param nrows: Количество строк файла для чтения
		:param na_values: Дополнительные строки для распознавания как NA/NaN
		:param keep_default_na: Следует ли включать значения NaN по умолчанию при анализе данных
		:param na_filter: Обнаружение маркеров отсутствующих значений (пустые строки и значение na_values)
		:param verbose: количество значений NA, помещенных в нечисловые столбцы
		:param skip_blank_lines: Если True, пропускать пустые строки, а не интерпретировать их как значения NaN
		:param parse_dates:
		:param infer_datetime_format: Если True и parse_dates включены, pandas попытается определить формат строк даты и времени в столбцах и, если это возможно, переключиться на более быстрый метод их анализа
		:param keep_date_col: Если значение True и parse_dates указывает на объединение нескольких столбцов, сохраняет исходные столбцы
		:param date_parser: Функция, используемая для преобразования последовательности строковых столбцов в массив экземпляров даты и времени
		:param dayfirst: Даты в формате ДД/ММ, международный и европейский формат
		:param cache_dates: Если значение равно True, используйте кеш уникальных преобразованных дат, чтобы применить преобразование даты и времени
		:param iterator: Возвратите объект TextFileReader для итерации или получения чанков
		:param chunksize:
		:param compression: Для оперативной распаковки данных на диске. Если 'infer' и 'filepath_or_buffer' аналогичны пути, то обнаружите сжатие из следующих расширений: '.gz', '.bz2', '.zip', '.xz', '.zst', '.tar' , '.tar.gz', '.tar.xz' или '.tar.bz2' (в противном случае без сжатия)
		:param thousands: Разделитель тысяч
		:param decimal: Символ для распознавания в качестве десятичной точки
		:param lineterminator: Символ для разбиения файла на строки. Действует только с C-парсером
		:param quotechar: Символ, используемый для обозначения начала и конца цитируемого элемента
		:param quoting:
		:param doublequote:
		:param escapechar: Односимвольная строка, используемая для экранирования других символов
		:param comment: Указывает, что оставшуюся часть строки не следует анализировать
		:param encoding: кодировка, используемая для UTF при чтении/записи (например, ‘utf-8’)
		:param encoding_errors: Как обрабатываются ошибки кодирования
		:param dialect: Если указан, этот параметр переопределит значения (по умолчанию или нет) для следующих параметров: delimiter, doublequote, escapechar, skipinitialspace, quotechar, quoting
		:param error_bad_lines: Строки со слишком большим количеством полей (например, строка csv со слишком большим количеством запятых) по умолчанию вызовут исключение, и DataFrame не будет возвращен
		:param warn_bad_lines: Если для error_bad_lines установлено значение False, а для warn_bad_lines установлено значение True, будет выведено предупреждение для каждой «плохой строки»
		:param on_bad_lines: {‘error’, ‘warn’, ‘skip’} Указывает, что делать при обнаружении плохой строки (строки со слишком большим количеством полей)
		:param delim_whitespace: Указывает, будут ли использоваться пробелы (например, '' или ' ') в качестве sep
		:param low_memory: Внутренне обрабатывать файл фрагментами, что приводит к меньшему использованию памяти при синтаксическом анализе, но, возможно, к выводу смешанного типа
		:param memory_map: Если для filepath_or_buffer указан путь к файлу, сопоставьте файловый объект непосредственно с памятью и получите доступ к данным непосредственно оттуда
		:param float_precision: Указывает, какой преобразователь должен использовать механизм для C-engine для значений с плавающей запятой
		:param storage_options: Дополнительные параметры, которые имеют смысл для конкретного подключения к хранилищу, например. хост, порт, имя пользователя, пароль и т. д.
		:return:
		"""

		# Файл типа csv ?
		if not FileManager.isCsv(path):
			return False

		self.data = pd.read_csv(path,
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
								storage_options=storage_options)

		return True

	def headers(self):

		"""
		Возвращает названия столбцов
		:return:
		"""

		if isinstance(self.data, pd.DataFrame):
			return self.data.columns

		return []

	def min(self, column):

		"""
		Возвращает min значение столбца column

		:param column: название столбца
		:return:
		"""

		if isinstance(self.data, pd.DataFrame):
			return self[column].min()

		return None

	def max(self, column):

		"""
		Возвращает max значение столбца column

		:param column: название столбца
		:return:
		"""

		if isinstance(self.data, pd.DataFrame):
			return self[column].max()

		return None

	def unique(self, column):

		"""
		Возвращает уникальные значения столца column

		:param column: название столбца
		:return:
		"""

		if isinstance(self.data, pd.DataFrame):
			return self[column].unique()

		return None

	def sort(self,
			 by,
			 axis=0,
			 ascending=True,
			 inplace=False,
			 kind='quicksort',
			 na_position='last',
			 ignore_index=False,
			 key=None):

		"""
		Сортирует DataFrame по стобцу by

		:param by: столбец(-цы) по которым идет сортировка
		:param axis: по чему идет сортировка (0 --‘index’, 1 -- ‘columns’)
		:param ascending: сортировать про возрастанию
		:param inplace: выполнять в исходных данных
		:param kind: {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’} алгоритм сортировки
		:param na_position: {‘first’, ‘last’} помещает NaN в начало, если first; если last NaN в конец
		:param ignore_index: если True, результирующая ось будет помечена 0, 1, …, n - 1.
		:param key: применяет ключевую функцию к значениям перед сортировкой
		:return:
		"""

		if (isinstance(self.data, pd.DataFrame)):
			return self.data.sort_values(by,
										 axis=axis,
										 ascending=ascending,
										 inplace=inplace,
										 kind=kind,
										 na_position=na_position,
										 ignore_index=ignore_index,
										 key=key)

		return None

	def drop(self,
			 labels=None,
			 axis=0,
			 index=None,
			 columns=None,
			 level=None,
			 inplace=False,
			 errors='raise'):

		"""
		Удаляет строки и/или столбцы

		:param labels: Метки индекса или столбца, которые необходимо удалить
		:param axis: {0 or ‘index’, 1 or ‘columns’} Удалять ли метки из индекса или столбцов
		:param index: Альтернатива указанию оси (axis)
		:param columns: Альтернатива указанию оси (axis)
		:param level: Для MultiIndex уровень, с которого будут удалены метки
		:param inplace: Если False, верните копию, иначе удалит в DataFrame
		:param errors: {‘ignore’, ‘raise’} Если «игнорировать», ошибка подавляется, и удаляются только существующие метки.
		:return:
		"""

		if isinstance(self.data, pd.DataFrame):
			return self.data.drop(labels=labels,
								  axis=axis,
								  index=index,
								  columns=columns,
								  level=level,
								  inplace=inplace,
								  errors=errors)

		return False

	def append(self,
			   data,
			   name=None,
			   sort=False,
			   verify_integrity=False):

		"""
		Добавляет новую строку

		:param data: Данные со значениями типа dict {column: value}
		:param name: index для строки (если None или '', то инициализируется числовым значением)
		:param sort: Отсортировать столбцы
		:param verify_integrity: Если True, выбросить ValueError при создании индекса с дубликатами
		:return:
		"""

		if not isinstance(self.data, pd.DataFrame):
			return False

		if name is None or name == '':
			self.data = self.data.append(data,
										 ignore_index=True,
										 sort=sort,
										 verify_integrity=verify_integrity)
		else:
			new_row = pd.Series(data=data, name=name)
			self.data = self.data.append(new_row,
										 ignore_index=True,
										 sort=sort,
										 verify_integrity=verify_integrity)

		return True

	def insert(self,
			   column,
			   data=np.NaN):

		"""
		Вставляет новый столбец

		:param column: Название нового столбца
		:param data: Вставляемые значения нового столбца
		:return:
		"""

		if not isinstance(self.data, pd.DataFrame):
			return False

		if type(data) == list or type(data) == tuple:
			if len(data) == len(self.data):
				self.data[column] = data
			else:
				self.data[column] = np.NaN
		else:
			self.data[column] = data

		return True

	def getColumn(self, column):

		"""
		Возвращает все значения столбца column

		:param column: название столбца
		:return:
		"""

		if isinstance(self.data, pd.DataFrame):
			return self.data[column]

		return []

	def __getitem__(self, column):
		return self.getColumn(column)

	def __setitem__(self, key, value):

		if type(key) == tuple and len(key) == 2:
			self.setItem(key[0], key[1], value)

	def setItem(self, row, column, value):

		"""
		Устанавливает новое значение в DataFrame

		:param row: название строки
		:param column: название столбца
		:param value: новое значение
		:return:
		"""

		if isinstance(self.data, pd.DataFrame):
			self.data.at[row, column] = value


if __name__ == "__main__":

	csv = CsvManager()

	if csv.load("../dataset.csv"):
		for column in csv.headers():
			print(csv.headers().get_loc(column))
