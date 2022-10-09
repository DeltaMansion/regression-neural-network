Текущее состояние:<br>
Regression.py - работающая модель сети без настройки параметров, есть вывод графика обучения. Точность предикта случайная (400000-700000 в сравнении с 400000).<br>
cooked-nn - загрузка кое-как обученной модели и подключение GUI интерфейса из cooked-interface. Тестовая версия V2. Есть нормализация диапазона значений [0; 1]<br><br>
Библиотеки: numpy, matplotlib, keras, PySimpleGUI, scikit learn, pandas.<br>
Набор данных: https://www.kaggle.com/datasets/beaver68/cars-dataset-in-russia<br>
Используются столбцы: mark,  Model,  Mileage,  Year,  Car_class,  Maximum_power,  Drive_unit,  Box,  Boost_type,  Volume,  Torque,  Maximum_speed,  Speed_to_100,  Consumption,  [Price] 
