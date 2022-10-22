import PySimpleGUI as sg
import pandas as pd
from model.model import Model
import numpy as np
model = Model()

if model.loadModel("my_model"):

	marks = model.uniqueValues["mark"]
	marks = marks[~pd.isna(marks)] # убрать NaN
	marks.sort()
	marks = marks.tolist()

	car_classes = model.uniqueValues["Car_class"]
	car_classes = car_classes[~pd.isna(car_classes)] # убрать NaN
	car_classes.sort()
	car_classes = car_classes.tolist()
    
	#Элементы ввода основных атрибутов
	MainInputCol1 = [
        #mark
        [sg.Text("Бренд: ", background_color="#B1A7A6", text_color="black", size=(12, 1)),
         sg.Combo(marks, size=(37, 1), key="mark",
                  background_color="#D3D3D3", text_color="black", button_background_color="#F5F3F4", button_arrow_color="black", default_value='Nissan')],
        #mileage
        [sg.Text("Пробег (км):", background_color="#B1A7A6", text_color="black", size=(12, 1)),
         sg.Slider(orientation="horizontal", enable_events=True, key="mileage-slider", range=(0, 500000), size=(21, 13),
                   trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=57000),
         sg.InputText('57000', key="mileage-input", enable_events=True, size=(10, 1), background_color="#D3D3D3", text_color="black")],
        #car_class
        [sg.Text("Класс машины:", background_color="#B1A7A6", text_color="black"),
         sg.Combo(car_classes, size=(37, 1), key="car_class",
                  background_color="#D3D3D3", text_color="black", button_background_color="#F5F3F4", button_arrow_color="black", default_value='J')],
        #drive_unit
        [sg.Text("Привод: ", background_color="#B1A7A6", text_color="black", size=(12, 1)),
         sg.Combo(['rear', 'full', 'front'], size=(37, 1), key="drive_unit",
                  background_color="#D3D3D3", text_color="black", button_background_color="#F5F3F4", button_arrow_color="black", default_value='full')]
	]

	MainInputCol2 = [
        # model
        [sg.Text("Модель:", background_color="#B1A7A6", text_color="black", size=(13, 1)),
         sg.InputText('X-Trail', size=(37, 1), key="model", background_color="#D3D3D3", text_color="black")],
        #year
        [sg.Text("Год:", background_color="#B1A7A6", text_color="black", size=(13, 1)),
         sg.Slider(orientation="horizontal", enable_events=True, key="year-slider", range=(1927, 2020), size=(23, 13),
                   trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=2018),
         sg.InputText('2018', key="year-input", enable_events=True, size=(6, 1), background_color="#D3D3D3", text_color="black")],
        # max_power
        [sg.Text("Мощность (л.с.):", background_color="#B1A7A6", text_color="black", size=(13, 1)),
         sg.Slider(orientation="horizontal", enable_events=True, key="max_power-slider", range=(5, 800), size=(23, 13),
                   trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=171),
         sg.InputText('171', key="max_power-input", enable_events=True, size=(6, 1), background_color="#D3D3D3",
                      text_color="black")],
        #box
        [sg.Text("Коробка передач:", background_color="#B1A7A6", text_color="black"),
         sg.Combo(['robot', 'automatic', 'variator', 'mechanics'], size=(35, 1), key="box",
                  background_color="#D3D3D3", text_color="black", button_background_color="#F5F3F4", button_arrow_color="black", default_value='variator')]
    ]

	MainInput = [[sg.Column(MainInputCol1, element_justification='c', background_color="#B1A7A6"),
                  sg.Column(MainInputCol2, element_justification='c', background_color="#B1A7A6")]]

    #Элементы ввода вторичных атрибутов
	SecondaryInputCol1 = [
		# boost_type
		[sg.Text("Тип усилителя: ", background_color="#B1A7A6", text_color="black", size=(20, 1)),
		 sg.Combo(['compressor', 'turbocharging', 'no'], size=(27, 1), key="boost_type",
				  background_color="#D3D3D3", text_color="black", button_background_color="#F5F3F4",
				  button_arrow_color="black", default_value='no')],
		#torque
		[sg.Text("Крутящий момент (Н∙м):", background_color="#B1A7A6", text_color="black", size=(20, 1)),
		 sg.Slider(orientation="horizontal", enable_events=True, key="torque-slider", range=(0, 1000), size=(16, 13),
				   trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=380),
		 sg.InputText('380', key="torque-input", enable_events=True, size=(6, 1), background_color="#D3D3D3", text_color="black")],
		#speed_to_100
		[sg.Text("Время разгона до 100км/ч:", background_color="#B1A7A6", text_color="black", size=(20, 1)),
		 sg.Slider(orientation="horizontal", enable_events=True, key="speed_to_100-slider", range=(0.00, 40), size=(16, 13),
				   trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=9.5),
		 sg.InputText('9.5', key="speed_to_100-input", enable_events=True, size=(6, 1), background_color="#D3D3D3", text_color="black")]
	]

	SecondaryInputCol2 = [
		# volume
		[sg.Text("Объём двигателя: ", background_color="#B1A7A6", text_color="black", size=(17, 1)),
		 sg.Slider(orientation="horizontal", enable_events=True, key="volume-slider", range=(0, 10), size=(20, 13),
				   trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=2),
		 sg.InputText('2', key="volume-input", enable_events=True, size=(6, 1), background_color="#D3D3D3",
					  text_color="black")],
		#maximum_speed
		[sg.Text("Макс. скорость (км/ч): ", background_color="#B1A7A6", text_color="black"),
		 sg.Slider(orientation="horizontal", enable_events=True, key="maximum_speed-slider", range=(70.0, 350.0), size=(20, 13),
				   trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=199),
		 sg.InputText('199', key="maximum_speed-input", enable_events=True, size=(6, 1), background_color="#D3D3D3", text_color="black")],
		#consumption
		[sg.Text("Потребление топлива: ", background_color="#B1A7A6", text_color="black", size=(17, 1)),
		 sg.Slider(orientation="horizontal", enable_events=True, key="consumption-slider", range=(0, 30), size=(20, 13),
				   trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=6.2),
		 sg.InputText('6.2', key="consumption-input", enable_events=True, size=(6, 1), background_color="#D3D3D3", text_color="black")]
	]

	SecondaryInput = [[sg.Column(SecondaryInputCol1, element_justification='c', background_color="#B1A7A6"),
					   sg.Column(SecondaryInputCol2, element_justification='c', background_color="#B1A7A6")]]

	#Вывод цены
	Price = [[sg.Output(size=(71, 1), key='-OutputText-', font='Helvetica 15',
						background_color="#D3D3D3", text_color="black", sbar_background_color="#F5F3F4", sbar_arrow_color="black")]]

	#Фрейм со всеми полями ввода
	Input = [
		[sg.Frame('Ввод основных атрибутов', layout=MainInput, border_width=6, background_color="#B1A7A6", title_color="black", font="bold")],
		[sg.Frame('Ввод дополнительных атрибутов', layout=SecondaryInput, border_width=6, background_color="#B1A7A6", title_color="black", font="bold")],
		[sg.Button('Рассчитать', enable_events=True, key='-LoadButton-', size=(73, 2),
				   border_width=6, button_color=('#BA181B'), font='Helvetica 14')],
		[sg.Frame('Цена автомобиля', layout=Price, border_width=6, background_color="#B1A7A6", title_color="black", font="bold")]
	]

	#Все элемнты интерфейса
	layout = [[sg.Frame('', layout=Input, border_width=9, background_color="#B1A7A6", title_color ="black", pad=(0, 5))]]

	#Создание окна
	window = sg.Window('Компьютерный практикум', layout, background_color='#151314', size=(860, 506))

	#Обработка событий
	while True:
		event, values = window.read()

		#Обработка
		if event == '-LoadButton-':
			if(values['mark'] == "" or values['model'] == "" or values['car_class'] == "" or
			   values['drive_unit'] == "" or values['box'] == ""):
				sg.Popup('Введены значения не всех основных атрибутов!', keep_on_top=True)
			else:
				try:
					data = [values['mark'], values['model'], int(round(float(values['mileage-input']))), int(values['year-slider']), values['car_class'],
							values['max_power-slider'], values['drive_unit'], values['box'], values['boost_type'],
							float(values['volume-input']), values['torque-slider'], values['maximum_speed-slider'],
							float(values['speed_to_100-input']), float(values['consumption-input'])]

					text_elem = window['-OutputText-']
					text_elem.update(int(model.predict(data))) #Ввод-вывод данных для нейронной сети
				except ValueError as e:
					sg.Popup('Введены некорректные значения атрибутов!', keep_on_top=True)

		#Вывод графиков
		if event == '-Graph1-':
			text_elem = window['-OutputText-']
			text_elem.update("Вывод 1-го графика")

		if event == '-Graph2-':
			text_elem = window['-OutputText-']
			text_elem.update("Вывод 2-го графика")

		if event in (sg.WIN_CLOSED, '-Exit-'):
			break

		#Синхронизация изменений слайдеров и текстовых полей()
		#mileage
		if event == "mileage-slider":
			window.Element("mileage-input").Update(values['mileage-slider'])
		if event == "mileage-input":
			window.Element("mileage-slider").Update(values['mileage-input'])

		#year
		if event == "year-slider":
			window.Element("year-input").Update(values['year-slider'])
		if event == "year-input":
			window.Element("year-slider").Update(values['year-input'])

		#max_power
		if event == "max_power-slider":
			window.Element("max_power-input").Update(values['max_power-slider'])
		if event == "max_power-input":
			window.Element("max_power-slider").Update(values['max_power-input'])

		#volume
		if event == "volume-slider":
			window.Element("volume-input").Update(values['volume-slider'])
		if event == "volume-input":
			window.Element("volume-slider").Update(values['volume-input'])

		#torque
		if event == "torque-slider":
			window.Element("torque-input").Update(values['torque-slider'])
		if event == "torque-input":
			window.Element("torque-slider").Update(values['torque-input'])

		#maximum_speed
		if event == "maximum_speed-slider":
			window.Element("maximum_speed-input").Update(values['maximum_speed-slider'])
		if event == "maximum_speed-input":
			window.Element("maximum_speed-slider").Update(values['maximum_speed-input'])

		#speed_to_100
		if event == "speed_to_100-slider":
			window.Element("speed_to_100-input").Update(values['speed_to_100-slider'])
		if event == "speed_to_100-input":
			window.Element("speed_to_100-slider").Update(values['speed_to_100-input'])

		#consumption
		if event == "consumption-slider":
			window.Element("consumption-input").Update(values['consumption-slider'])
		if event == "consumption-input":
			window.Element("consumption-slider").Update(values['consumption-input'])

window.close()