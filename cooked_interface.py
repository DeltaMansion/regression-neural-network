import PySimpleGUI as sg
from cooked_nn import data_input
marks = ['Isuzu', 'Changan', 'Jeep', 'Saab', 'Fiat', 'Mazda', 'LADA (VAZ)', 'Subaru', 'Lifan', 'Hummer', 'Chevrolet',
         'Ravon', 'LyAZ', 'Suzuki', 'Chery', 'Porsche', 'Luxgen', 'Hawtai', 'SsangYong', 'GAZ', 'Moskvich', 'Lexus',
         'Smart', 'ZAZ', 'Acura', 'DongFeng', 'DW Hower', 'Daewoo', 'SEAT', 'Daimler', 'ZIL', 'Lamborghini', 'Bentley',
         'Genesis', 'Volkswagen', 'Rover', 'Lincoln', 'AC', 'Peugeot', 'Jaguar', 'Geely', 'Cadillac', 'Mitsubishi',
         'Opel', 'AMC', 'Mercedes-Benz', 'Scion', 'Chrysler', 'Haval', 'Renault', 'Daihatsu', 'Nissan', 'Race car',
         'Vortex', 'ICH', 'BMW', 'Iran Khodro', 'Tesla', 'Toyota', 'Ferrari', 'MINI', 'Aston Martin', 'Citroen',
         'Skoda', 'Datsun', 'Rolls-Royce', 'Hyundai', 'Kia', 'Land Rover', 'Great Wall', 'McLaren', 'Audi', 'Ford',
         'Dodge', 'Infiniti', 'ZX', 'FAW', 'Volvo', 'Maserati', 'YAZ', 'Maybach', 'Honda', 'GMC', 'Alfa Romeo', 'TagAZ']
marks.sort()

car_classes = ['E', 'M', 'A', 'C', 'J', 'D', 'S', 'B', 'F']
car_classes.sort()

#Элементы ввода основных атрибутов
MainInputCol1 = [
    #mark
    [sg.Text("Mark:", background_color="#B1A7A6", text_color="black"),
     sg.Combo(marks, size=(40, 1), key="mark",
              background_color="#D3D3D3", text_color="black", button_background_color="#F5F3F4", button_arrow_color="black", default_value='Nissan')],
    #mileage
    [sg.Text("Mileage:", background_color="#B1A7A6", text_color="black"),
     sg.Slider(orientation="horizontal", enable_events=True, key="mileage-slider", range=(0, 2000000), size=(22, 13),
               trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=57000),
     sg.InputText('57000', key="mileage-input", enable_events=True, size=(10, 1), background_color="#D3D3D3", text_color="black")],
    #car_class
    [sg.Text("Car class:", background_color="#B1A7A6", text_color="black"),
     sg.Combo(car_classes, size=(36, 1), key="car_class",
              background_color="#D3D3D3", text_color="black", button_background_color="#F5F3F4", button_arrow_color="black", default_value='J')],
    #drive_unit
    [sg.Text("Drive unit:", background_color="#B1A7A6", text_color="black"),
     sg.Combo(['rear', 'full', 'front'], size=(36, 1), key="drive_unit",
              background_color="#D3D3D3", text_color="black", button_background_color="#F5F3F4", button_arrow_color="black", default_value='full')]
]

MainInputCol2 = [
    #model
    [sg.Text("Model:", background_color="#B1A7A6", text_color="black"),
     sg.InputText('X-Trail', size=(41, 1), key="model", background_color="#D3D3D3", text_color="black")],
    #year
    [sg.Text("Year:", background_color="#B1A7A6", text_color="black"),
     sg.Slider(orientation="horizontal", enable_events=True, key="year-slider", range=(1908, 2022), size=(27, 13),
               trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=2018),
     sg.InputText('2018', key="year-input", enable_events=True, size=(6, 1), background_color="#D3D3D3", text_color="black")],
    #max_power
    [sg.Text("Max-power:", background_color="#B1A7A6", text_color="black"),
     sg.Slider(orientation="horizontal", enable_events=True, key="max_power-slider", range=(5, 850), size=(23, 13),
               trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=171),
     sg.InputText('171', key="max_power-input", enable_events=True, size=(6, 1), background_color="#D3D3D3", text_color="black")],
    #box
    [sg.Text("Box:", background_color="#B1A7A6", text_color="black"),
     sg.Combo(['robot', 'automatic', 'variator', 'mechanics'], size=(41, 1), key="box",
              background_color="#D3D3D3", text_color="black", button_background_color="#F5F3F4", button_arrow_color="black", default_value='variator')]
]

MainInput = [[sg.Column(MainInputCol1, element_justification='c', background_color="#B1A7A6"),
              sg.Column(MainInputCol2, element_justification='c', background_color="#B1A7A6")]]

#Элементы ввода вторичных атрибутов
SecondaryInputCol1 = [
    # boost_type
    [sg.Text("Boost type:", background_color="#B1A7A6", text_color="black"),
     sg.Combo(['compressor', 'turbocharging', 'no'], size=(35, 1), key="boost_type",
              background_color="#D3D3D3", text_color="black", button_background_color="#F5F3F4", button_arrow_color="black", default_value='no')],
    #torque
    [sg.Text("Torgue:", background_color="#B1A7A6", text_color="black"),
     sg.Slider(orientation="horizontal", enable_events=True, key="torque-slider", range=(0, 1500), size=(26, 13),
               trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=380),
     sg.InputText('380', key="torque-input", enable_events=True, size=(6, 1), background_color="#D3D3D3", text_color="black")],
    #speed_to_100
    [sg.Text("Speed to 100:", background_color="#B1A7A6", text_color="black"),
     sg.Slider(orientation="horizontal", enable_events=True, key="speed_to_100-slider", range=(0.00, 50), size=(22, 13),
               trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=9.5),
     sg.InputText('9.5', key="speed_to_100-input", enable_events=True, size=(6, 1), background_color="#D3D3D3", text_color="black")]
]

SecondaryInputCol2 = [
    # volume
    [sg.Text("Volume:", background_color="#B1A7A6", text_color="black"),
     sg.Slider(orientation="horizontal", enable_events=True, key="volume-slider", range=(0, 10), size=(25, 13),
               trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=2),
     sg.InputText('2', key="volume-input", enable_events=True, size=(6, 1), background_color="#D3D3D3", text_color="black")],
    #maximum_speed
    [sg.Text("Maximum speed:", background_color="#B1A7A6", text_color="black"),
     sg.Slider(orientation="horizontal", enable_events=True, key="maximum_speed-slider", range=(10.0, 492.0), size=(19, 13),
               trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=199),
     sg.InputText('199', key="maximum_speed-input", enable_events=True, size=(6, 1), background_color="#D3D3D3", text_color="black")],
    #consumption
    [sg.Text("Consumption:", background_color="#B1A7A6", text_color="black"),
     sg.Slider(orientation="horizontal", enable_events=True, key="consumption-slider", range=(0, 35), size=(21, 13),
               trough_color="#D3D3D3", background_color="#B1A7A6", text_color="black", default_value=6.2),
     sg.InputText('6.2', key="consumption-input", enable_events=True, size=(6, 1), background_color="#D3D3D3", text_color="black")]
]

SecondaryInput = [[sg.Column(SecondaryInputCol1, element_justification='c', background_color="#B1A7A6"),
                   sg.Column(SecondaryInputCol2, element_justification='c', background_color="#B1A7A6")]]

#Вывод цены
Price = [[sg.Output(size=(101, 3), key='-OutputText-',
                    background_color="#D3D3D3", text_color="black", sbar_background_color="#F5F3F4", sbar_arrow_color="black")]]

#Фрейм со всеми полями ввода
Input = [
    [sg.Frame('Ввод основных атрибутов', layout=MainInput, border_width=6, background_color="#B1A7A6", title_color="black", font="bold")],
    [sg.Frame('Ввод дополнительных атрибутов', layout=SecondaryInput, border_width=6, background_color="#B1A7A6", title_color="black", font="bold")],
    [sg.Button('Принять', enable_events=True, key='-LoadButton-', size=(81, 2),
               border_width=4, button_color=('#BA181B'), font='Helvetica 13')],
    [sg.Frame('Цена автомобиля', layout=Price, border_width=6, background_color="#B1A7A6", title_color="black", font="bold")]
]

#Кнопки для вывода графиков
GraphBottons = [[sg.Button('График1', enable_events=True, key='-Graph1-',  size=(33, 3),
                           border_width=1, button_color=('#BA181B'), font='Helvetica 11'),
                 sg.Button('График2', enable_events=True, key='-Graph2-',  size=(33, 3),
                           border_width=1, button_color=('#BA181B'), font='Helvetica 11')]]

Graphs = [[sg.Frame('Графики', layout=GraphBottons, border_width=9, background_color="#151314", title_color ="white", font="bold")]]

#Кнопка выхода
ExitBotton = [[sg.Button('Выйти', enable_events=True, key='-Exit-', size=(8, 3), button_color=('#A4161A'), font='Helvetica 14')]]

#Все элемнты интерфейса
layout = [[sg.Frame('', layout=Input, border_width=9, background_color="#B1A7A6", title_color ="black")],
          [sg.Column(Graphs, element_justification='c', background_color="#151314"),
           sg.Column(ExitBotton, element_justification='c', background_color="#151314")]]

#Создание окна
window = sg.Window('Компьютерный практикум', layout, background_color='#151314')

#Обработка событий
while True:
    event, values = window.read()

    #Обработка
    if event == '-LoadButton-':
        if(values['mark'] == "" or values['model'] == "" or values['car_class'] == "" or
           values['drive_unit'] == "" or values['box'] == ""):
            sg.Popup('Введены значения не всех основных атрибутов!', keep_on_top=True)
        else:
            data = [values['mark'], values['model'], values['mileage-slider'], values['year-slider'], values['car_class'],
                    values['max_power-slider'], values['drive_unit'], values['box'], values['boost_type'],
                    values['volume-input'], values['torque-slider'], values['maximum_speed-slider'],
                    values['speed_to_100-input'], values['consumption-input']]

            text_elem = window['-OutputText-']
            text_elem.update(data_input(data)) #Ввод-вывод данных для нейронной сети

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