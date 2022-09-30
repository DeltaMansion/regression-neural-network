from keras.layers import Activation, Dense, InputLayer, Dropout, BatchNormalization
from keras.callbacks import EarlyStopping
from keras.models import Sequential
import numpy as np
import matplotlib.pyplot as plt
import timeit
import keys_lists
from sklearn import preprocessing

# вытащить данные из файла и разделить на наборы: X - то, что вводим в нейронку, Y - то, что хотим получить из неё
def get_xy_data(file_name):
    dataset = np.loadtxt('./' + file_name, delimiter=';', skiprows=1, dtype='U')
    EXAMPLES_FOR_TEST = 50

    # [:] - всё содержимое строки, [N] - номер столбца данных в файле
    x_train = keys_lists.conversion_to_numbers_data(dataset[EXAMPLES_FOR_TEST:, 0:14])
    y_train = np.array(dataset[EXAMPLES_FOR_TEST:, 14]).astype(float)

    x_test = keys_lists.conversion_to_numbers_data(dataset[0:EXAMPLES_FOR_TEST, 0:14])
    y_test = np.array(dataset[0:EXAMPLES_FOR_TEST, 14]).astype(float)
    
    # нормализация данных только для набора обучения X
    # для тестирования и предиктов нормализация ломает весь результат 
    for i in range(0, 14):
        x_train[i] = preprocessing.normalize([x_train[i]])

    #если надо посмотреть на данные
    #print(x)
    #print(y)

    return x_train, y_train, x_test, y_test

# данные для обучения и тестирования
x_train, y_train, x_test, y_test = get_xy_data("dataset.csv")
columns_counter = len(x_train[0])

# создание модели сети
model = Sequential()
model.add(Dense(columns_counter, input_shape=(columns_counter,), activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='adam', loss='mse', metrics=['mse'])

# обучение
start_seconds: float = timeit.default_timer()
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, min_delta=10000000000, patience=5) # если захочется проверить раннюю остановку обучения
history = model.fit(x_train, y_train, epochs=50, verbose=2, validation_split=0.2, batch_size=256) #callbacks=[es]
end_seconds: float = timeit.default_timer()

# график регрессии: x - y_test, y - y_pred
y_pred = model.predict(x_test)
for x, y in zip(y_test, y_pred):
    print(x, y)

# тестирование на пользовательских данных
#final_test_data = np.array(['Chrysler', 'Sebring', '250000.0', '2007.0', 'D', '189.0', 'front', 'automatic', 'no', '2.7', '260.0', '207.0', '9.2', '10.7']) # 400000
#final_test_data = np.array(['Mercedes-Benz', 'C-Class', '189000.00', '2012.00', 'D', '204.00', 'rear', 'automatic', 'turbocharging', '1.80', '310.00', '240.00', '7.20', '6.40']) # 970000
final_test_data = np.array(['Nissan', 'X-Trail', '57000.0', '2018.0', 'J', '171.0', 'full', 'variator', 'no', '2.0', '380.0', '199.0', '9.50', '6.20']) # 1599000
final_test_data = keys_lists.conversion_to_numbers_data(final_test_data.reshape((1,)+final_test_data.shape))
result = model.predict(final_test_data)

# вывод графика обучения
plt.figure()
plt.plot(history.history['mse'], label='mse')
plt.plot(history.history['val_mse'], label = 'val_mse')
plt.xlabel('Epoch')
plt.ylabel('mse')
plt.legend(loc='lower right')
plt.title('Predict - ' + str(result[0]) + ' (should be 1599000)')
plt.text(0.1, 0.1, str(end_seconds - start_seconds) + ' sec')
plt.show()