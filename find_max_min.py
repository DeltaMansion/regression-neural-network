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
