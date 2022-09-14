import numpy
from data_analysis import DataAnalyser
from file_utils import get_data_from_file
from headers import headers

unique_indexes = [0, 1, 4, 6, 7]
float_indexes = [2, 3, 5, 9, 10, 11, 12, 13]

analyser = DataAnalyser(get_data_from_file("processed_dataset_result.csv", ";"))

keys_dict = {}

for i in unique_indexes:
    keys_dict[i] = analyser.get_unique_items(headers[i], [''])

print(analyser.get_unique_items(headers[4], ['']))

for key, value in keys_dict.items():
    #print(key, " - ", value)
    pass
def conversion_to_numbers_data(raw_data):
    return_data = numpy.zeros((len(raw_data), 12))

    index = 0
    for row in raw_data:
        for j in unique_indexes:
            return_data[index][j] = convert_unit(keys_dict[i])

        for j in float_indexes:
            return_data[index][j] = float(row[j])

        index += 1
    return return_data

def convert_unit(keys_list, elem):
    try:
        return keys_list.index(elem)
    except ValueError:
        return -1

