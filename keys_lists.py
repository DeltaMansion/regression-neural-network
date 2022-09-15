import numpy
from data_analysis import DataAnalyser
from file_utils import get_data_from_file
from headers import headers

unique_indexes = [0, 1, 4, 6, 7, 8]
float_indexes = [2, 3, 5, 9, 10, 11, 12, 13, 14]
float_indexes2 = [2, 3, 5, 9, 10, 11, 12, 13]

analyser = DataAnalyser(get_data_from_file("dataset.csv", ";"))

keys_dict = {}

for i in unique_indexes:
    keys_dict[i] = analyser.get_unique_items(headers[i], [''])

for key, value in keys_dict.items():
    #print(key, " - ", value)
    pass

def conversion_to_numbers_data(raw_data):
    return_data = numpy.zeros((len(raw_data), 14))
    
    index = 0
    for row in raw_data:
        for j in unique_indexes:
            return_data[index][j] = convert_unit(keys_dict[j], raw_data[index][j])

        for j in float_indexes2:
            return_data[index][j] = float(raw_data[index][j])
        index += 1
    return return_data

def convert_unit(keys_list, elem):
    try:
        return keys_list.index(elem)
    except ValueError:
        return -1

