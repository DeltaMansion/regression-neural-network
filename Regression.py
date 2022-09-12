from keras.layers import Activation, Dense, InputLayer
from keras.models import Sequential
import numpy as np
import matplotlib.pyplot as plt
import timeit
import keys_lists

# вытащить данные из файла и разделить на наборы: X - то, что вводим в нейронку, Y - то, что хотим получить из неё
def get_xy_data(file_name):
    dataset = np.loadtxt('./' + file_name, delimiter=',', skiprows=1, dtype='U')

    # [:] - всё содержимое строки, [N] - номер столбца данных в файле
    x = keys_lists.conversion_to_numbers_data(dataset[:, 0:12])
    y = np.array(dataset[:, 12]).astype(float)

    #если надо посмотреть на данные
    #print(x)
    #print(y)

    return x, y

# данные для обучения и тестирования
x_train, y_train = get_xy_data("processed_cars.csv")
columns_counter = len(x_train[0])

# создание модели сети
model = Sequential()
model.add(Dense(256, input_shape=(columns_counter,), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse', metrics=['mse'])

# обучение
start_seconds: float = timeit.default_timer()
history = model.fit(x_train, y_train, epochs=50, verbose=2, validation_split=0.2, batch_size=256);
end_seconds: float = timeit.default_timer()

# тестирование на пользовательских данных
final_test_data = np.array(['Chrysler', 'automatic', 'front', 'USA', 'black', '250000.0', '2007.0', 'Sedan', 'Sebring', '189.0', '207.0', '10.7'])
final_test_data = keys_lists.conversion_to_numbers_data(final_test_data.reshape((1,)+final_test_data.shape))
result = model.predict(final_test_data)

# вывод графика обучения
plt.figure()
plt.plot(history.history['mse'], label='mse')
plt.plot(history.history['val_mse'], label = 'val_mse')
plt.xlabel('Epoch')
plt.ylabel('mse')
plt.legend(loc='lower right')
plt.title('Predict - ' + str(result[0]) + ' (should be 400000)')
plt.text(0.1, 0.1, str(end_seconds - start_seconds) + ' sec')
plt.show()