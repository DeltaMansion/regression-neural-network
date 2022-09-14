from pathlib import Path
import os
from data_analysis import DataAnalyser
from csv import reader


def get_data_from_file(file_name: str, divider: str = ",") -> list[list]:
    data = []
    with open(Path(os.path.realpath(__file__)).parent / file_name) as file:
        reader_obj = reader(file, quotechar=divider)

        for line in reader_obj:
            data.append(line)
    return data


def save_to_file(file_name: str, data: list[list], divider: str = ";"):
    with open(Path(os.path.realpath(__file__)).parent / file_name, "w") as file:
        for line in data:
            str_line = divider.join([str(item) if type(item) is not str else item for item in line]) + "\n"
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
    print(arrays[4])
    data = [headers]
    data += [list(item) for item in zip(*arrays)]
    save_to_file(file_name_new, data, divider_new)


if __name__ == "__main__":

    from headers import headers

    select_headers_and_save_file(
        headers,
        "processed_dataset.csv",
        "processed_dataset_result.csv",
        "|",
        ";"
        )
