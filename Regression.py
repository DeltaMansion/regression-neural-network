from keras.layers import Activation, Dense, InputLayer
from keras.models import Sequential
import numpy as np
import matplotlib.pyplot as plt
import timeit

# вытащить данные из файла и разделить на наборы: X - то, что вводим в нейронку, Y - то, что хотим получить из неё
def get_xy_data(file_name):
    # при смене датасета нужно менять разделение данных из-за столбцов, сейчас используется 11 для X, 1 для Y
    dataset = np.loadtxt('./' + file_name, delimiter=',', skiprows=1)

    # [:] - всё содержимое строки, [N] - номер столбца данных в файле
    x = dataset[:, 0:11]
    y = dataset[:, 11]

    #если надо посмотреть на данные
    #print(x)
    #print(y)

    return x, y

# данные для обучения и тестирования
x_train, y_train = get_xy_data("train.csv")
x_test, y_test = get_xy_data("test.csv")
columns_counter = len(x_train[0])

# создание модели сети
model = Sequential()
model.add(Dense(128, input_shape=(columns_counter,), activation='relu'))
model.add(Dense(64, input_shape=(columns_counter,), activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse', metrics=['mse'])

# обучение
start_seconds: float = timeit.default_timer()
history = model.fit(x_train, y_train, epochs=500, verbose=2, validation_data=(x_test, y_test), batch_size=256);
end_seconds: float = timeit.default_timer()

# тестирование на пользовательских данных
final_test_data = [6.0,0.31,0.47,3.6,0.067,18.0,42.0,0.99549,3.39,0.66,11.0]
final_test_data = np.array(final_test_data)
final_test_data = final_test_data.reshape((1,)+final_test_data.shape)
result = model.predict(final_test_data)

# вывод графика обучения
plt.figure()
plt.plot(history.history['mse'], label='mse')
plt.plot(history.history['val_mse'], label = 'val_mse')
plt.xlabel('Epoch')
plt.ylabel('mse')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.title('Predict - ' + str(result[0]) + ' (should be 6)')
plt.text(0.1, 0.1, str(end_seconds - start_seconds) + ' sec')
plt.show()

# тру стори:
# почти час сидел и думал: а чо нейронка не обучается?
# позже заметил, что я вместо y_train второй раз x_train написал
# потом оказалось, что на том наборе данных, который я сделал, сеть не работает