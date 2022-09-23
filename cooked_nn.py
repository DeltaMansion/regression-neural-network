from keras.models import Sequential, load_model
import numpy as np
import keys_lists
import cooked_interface
from file_utils import resource_path

model = load_model(resource_path('my_model'))

#np.array(['Nissan', 'X-Trail', '57000.0', '2018.0', 'J', '171.0', 'full', 'variator', 'no', '2.0', '380.0', '199.0', '9.50', '6.20']) # 1599000

def data_input(data):
    print(data)
    data = np.array(data)
    data = keys_lists.conversion_to_numbers_data(data.reshape((1,)+data.shape))
    return model.predict(data)[0][0]