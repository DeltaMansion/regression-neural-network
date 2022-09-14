import numpy as np
import pandas as pd

data = pd.read_csv('./full_dataset.csv', delimiter=',')

cols_to_keep =  [
    "mark",
    "Model",
    "Mileage",
    "Year",
    "Car_class",
    "Maximum_power",
    "Drive_unit",
    "Box",
    "Boost_type",
    "Volume",
    "Torque",
    "Maximum_speed",
    "Speed_to_100",
    "Consumption",
    "Price"
]

data.loc[:, cols_to_keep].to_csv('foo.csv',encoding='utf8',index=False)