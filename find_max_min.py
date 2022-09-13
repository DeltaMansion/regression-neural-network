from pathlib import Path
import os


data = []

with open(Path(os.path.realpath(__file__)).parent / "processed_cars.csv") as file:
    lines = file.readlines()

    for line in lines:
        data.append([item for item in line.replace('\n', '').split(",")])

def find_float_max_min(index: int, ignore_zeros: bool = False) -> float:
    arr = [float(item[index]) for item in data[1:] if float(item[index]) != 0 or not ignore_zeros]
    return data[0][index] + ": ", max(arr), min(arr)

def get_unique_items(index: int) -> list:
    array = []
    for line in data[1:]:
        if line[index] not in array:
            array.append(line[index])
    return data[0][index] + ": ", array

def sort_by_key(index_to_be_key: int, index_to_be_value: int) -> dict[str, str]:
    result = {}
    for line in data[1:]:
        if line[index_to_be_key] not in result.keys():
            result[line[index_to_be_key]] = []
        result[line[index_to_be_key]].append(line[index_to_be_value])
    return result


# Mark
print(*get_unique_items(0))
# Box
print(*get_unique_items(1))
# Drive Unit
print(*get_unique_items(2))
# Country
print(*get_unique_items(3))
# Color
print(*get_unique_items(4))
# Car type
print(*get_unique_items(7))
# Model

print("Models")
for key, value in sort_by_key(0, 8).items():
    print(key + ": ", value)

# Mileadge
print(*find_float_max_min(5))
# Year
print(*find_float_max_min(6))
# Max power
print(*find_float_max_min(9, True))
# Max speed
print(*find_float_max_min(10, True))
# Consumption
print(*find_float_max_min(11, True))
