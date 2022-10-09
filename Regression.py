from keras.callbacks import EarlyStopping
import numpy as np
import matplotlib.pyplot as plt
import timeit
from model.model import Model
from keras.layers import Dense, BatchNormalization
np.set_printoptions(formatter={'float': '{: 0.7f}'.format})

model = Model()
model.loadCsvData("dataset.csv", sep=";")
model.prepare(show_loading=True)
model.splitTrainTest(labels=["Price"])
x_train, y_train, x_test, y_test = model.x_train, model.y_train, model.x_test, model.y_test

mm = 8
model.initSequential(layers=[
			Dense(len(x_train[0]), input_shape=(len(x_train[0]),), activation='relu'),
            #Dense(256 * mm, activation='relu'),
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
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, min_delta=10000000000, patience=5) # если захочется проверить раннюю остановку обучения
history = model.fit(x_train, y_train, epochs=300, verbose=2, validation_split=0.2, batch_size=256) #callbacks=[es]
end_seconds: float = timeit.default_timer()

# тестирование на пользовательских данных
final_test_data = np.array(['Nissan', 'X-Trail', '57000.0', '2018.0', 'J', '171.0', 'full', 'variator', 'no', '2.0', '380.0', '199.0', '9.50', '6.20']) # 1599000
result = model.predict(final_test_data)

# вывод графика обучения
plt.figure()
plt.plot(history.history['mse'], label='mse')
plt.plot(history.history['val_mse'], label = 'val_mse')
plt.xlabel('Epoch')
plt.ylabel('mse')
plt.legend(loc='best')
plt.title('Predict - ' + str(result) + ' (should be 1599000)')
plt.text(0.1, 0.1, str(end_seconds - start_seconds) + ' sec')
plt.show()

#model.saveModel("my_model")