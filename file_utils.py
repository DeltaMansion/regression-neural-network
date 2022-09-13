from pathlib import Path
import os
from data_analysis import DataAnalyser


def get_data_from_file(file_name: str, divider: str = ",") -> list[list]:
    data = []
    with open(Path(os.path.realpath(__file__)).parent / file_name) as file:
        lines = file.readlines()

        for line in lines:
            data.append([item for item in line.replace('\n', '').split(divider)])
    return data


def save_to_file(file_name: str, data: list[list], divider: str = ";"):
    with open(Path(os.path.realpath(__file__)).parent / file_name, "w") as file:
        for line in data:
            str_line = divider.join([str(item) for item in line]) + "\n"
            file.write(str_line)


def select_headers_and_save_file(
    headers: list[str],
    file_name_old: str,
    file_name_new: str,
    divider_old: str = ",",
    divider_new: str=";"
    ):
    analyser = DataAnalyser(get_data_from_file(file_name_old, divider_old))
    file_headers = analyser.get_header()
    arrays = [analyser[item] for item in headers]
    data = [headers]
    data += [list(item) for item in zip(*arrays)]
    save_to_file(file_name_new, data, divider_new)


if __name__ == "__main__":

    items = [
        "mark",
        "Model",
        "Mileage",
        "Year",
        "Car_class",
        "Maximum_power",
        "Drive_unit",
        "Box",

    ]

    items2 = [
        "Boost_type",
        "Volume",
        "Torque",
        "Maximum_speed",
        "Speed_to_100",
        "Consumption"
    ]

    select_headers_and_save_file(
        items + items2,
        "processed_dataset.csv",
        "processed_dataset_result.csv",
        "|",
        ";"
        )
