class DataAnalyser:
    data = []

    def __init__(self, data: list[list] = []):
        self.data = data

    def get_header(self) -> list[str]:
        return self.data[0]

    # Can return columns as well
    def __getitem__(self, key: int | str) -> list:
        if type(key) is str:
            index = self.data[0].index(key)
            return [item[index] for item in self.data[1:]]
        else:
            return self.data[1:][key]

    def find_float_max_min(self, key: int | str, ignore_zeros: bool = False) -> (float, float):
        arr = [float(item) for item in self[key] if float(item) != 0 or not ignore_zeros]
        return max(arr), min(arr)

    def get_unique_items(self, index: int | str, items_to_ignore: list = []) -> list:
        return filter(lambda item: item not in items_to_ignore,list(set(self[index])))

    def sort_by_key(self, key_col: str, value_col: str, only_unique: bool = True) -> dict[list]:
        result = {}
        key_index = self.data[0].index(key_col)
        val_col_index = self.data[0].index(value_col)
        for line in self.data[1:]:
            if line[key_index] not in result.keys():
                result[line[key_index]] = []
            if line[val_col_index] not in result[line[key_index]] or not only_unique:
                result[line[key_index]].append(line[val_col_index])
        return result



# --------------------------------
# Examples
# --------------------------------

if __name__ == "__main__":
    from file_utils import get_data_from_file

    analyser = DataAnalyser(get_data_from_file("processed_cars.csv"))

    for item in analyser.get_header():
        print(item)

    print(analyser.get_unique_items("Country"))
    print(analyser.find_float_max_min("Year"))
    print(analyser.find_float_max_min("Mileage"))
    print(analyser.find_float_max_min("Maximum_power", True))
    print(analyser.find_float_max_min("Maximum_speed", True))
    print(analyser.find_float_max_min("Consumption", True))

    print("Models")
    for key, value in analyser.sort_by_key("mark", "Model").items():
        print(key + ": ", value)

