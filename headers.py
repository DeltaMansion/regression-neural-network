headers_main =  [
    "mark",
    "Model",
    "Mileage", # Max min
    "Year", # Max min
    "Car_class",
    "Maximum_power", # Max min, ignore 0
    "Drive_unit",
    "Box",
]

other_headers = [
    "Boost_type", # Max min, ignore 0
    "Volume", # Max min, ignore 0
    "Torque", # Max min, ignore 0
    "Maximum_speed", # Max min, ignore 0
    "Speed_to_100", # Max min, ignore 0
    "Consumption" # Max min, ignore 0
]

headers = headers_main + other_headers
