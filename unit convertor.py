def convert_length(value, from_unit, to_unit):
    units = {
        "m": 1,
        "cm": 100,
        "mm": 1000,
        "km": 0.001,
        "in": 39.3701,
        "ft": 3.28084,
        "yd": 1.09361,
        "mi": 0.000621371
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid length units")

    return value * units[to_unit] / units[from_unit]


def convert_weight(value, from_unit, to_unit):
    units = {
        "kg": 1,
        "g": 1000,
        "mg": 1e6,
        "lb": 2.20462,
        "oz": 35.274
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid weight units")

    return value * units[to_unit] / units[from_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "C":
        return value * 9 / 5 + 32 if to_unit == "F" else value + 273.15
    elif from_unit == "F":
        return (value - 32)

