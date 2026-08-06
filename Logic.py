# Logic.py - Complete conversion logic functions for all unit types

from data import *


# =========================================== TIME CONVERTERS
def time_converter(choice, value):
    conversions = {
        "1": ("second", "minute"),
        "2": ("minute", "hour"),
        "3": ("hour", "day"),
        "4": ("day", "week"),
        "5": ("week", "month"),
        "6": ("month", "year"),
        "7": ("year", "decade"),
        "8": ("decade", "century"),
        "9": ("century", "millennium"),
        "10": ("second", "hour"),
        "11": ("minute", "day"),
        "12": ("hour", "week"),
        "13": ("day", "month"),
        "14": ("month", "year"),
        "15": ("year", "decade"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        return value * (TIME["units"][from_unit] / TIME["units"][to_unit])
    return None


# =========================================== DATA BINARY CONVERTERS
def data_binary_converter(choice, value):
    conversions = {
        "1": ("bit", "byte"),
        "2": ("byte", "KB"),
        "3": ("KB", "MB"),
        "4": ("MB", "GB"),
        "5": ("GB", "TB"),
        "6": ("TB", "PB"),
        "7": ("PB", "EB"),
        "8": ("EB", "ZB"),
        "9": ("ZB", "YB"),
        "10": ("byte", "KB"),
        "11": ("KB", "MB"),
        "12": ("MB", "GB"),
        "13": ("GB", "TB"),
        "14": ("TB", "PB"),
        "15": ("PB", "EB"),
        "16": ("EB", "ZB"),
        "17": ("ZB", "YB"),
        "18": ("bit", "KB"),
        "19": ("byte", "MB"),
        "20": ("KB", "GB"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        return value * (DATA_BINARY["units"][from_unit] / DATA_BINARY["units"][to_unit])
    return None


# =========================================== DATA DECIMAL CONVERTERS
def data_decimal_converter(choice, value):
    conversions = {
        "1": ("bit", "byte"),
        "2": ("byte", "kB"),
        "3": ("kB", "MB"),
        "4": ("MB", "GB"),
        "5": ("GB", "TB"),
        "6": ("TB", "PB"),
        "7": ("PB", "EB"),
        "8": ("EB", "ZB"),
        "9": ("ZB", "YB"),
        "10": ("byte", "kB"),
        "11": ("kB", "MB"),
        "12": ("MB", "GB"),
        "13": ("GB", "TB"),
        "14": ("TB", "PB"),
        "15": ("PB", "EB"),
        "16": ("EB", "ZB"),
        "17": ("ZB", "YB"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        return value * (DATA_DECIMAL["units"][from_unit] / DATA_DECIMAL["units"][to_unit])
    return None


# =========================================== LENGTH METRIC CONVERTERS
def length_metric_converter(choice, value):
    conversions = {
        "1": ("nanometer", "micrometer"),
        "2": ("micrometer", "millimeter"),
        "3": ("millimeter", "centimeter"),
        "4": ("centimeter", "decimeter"),
        "5": ("decimeter", "meter"),
        "6": ("meter", "decameter"),
        "7": ("decameter", "hectometer"),
        "8": ("hectometer", "kilometer"),
        "9": ("kilometer", "megameter"),
        "10": ("megameter", "gigameter"),
        "11": ("nanometer", "millimeter"),
        "12": ("micrometer", "centimeter"),
        "13": ("millimeter", "meter"),
        "14": ("centimeter", "meter"),
        "15": ("meter", "kilometer"),
        "16": ("kilometer", "meter"),
        "17": ("centimeter", "millimeter"),
        "18": ("meter", "centimeter"),
        "19": ("kilometer", "centimeter"),
        "20": ("meter", "millimeter"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        return value * (LENGTH_METRIC["units"][from_unit] / LENGTH_METRIC["units"][to_unit])
    return None


# =========================================== LENGTH IMPERIAL CONVERTERS
def length_imperial_converter(choice, value):
    conversions = {
        "1": ("thou", "inch"),
        "2": ("inch", "foot"),
        "3": ("foot", "yard"),
        "4": ("yard", "chain"),
        "5": ("chain", "furlong"),
        "6": ("furlong", "mile"),
        "7": ("mile", "league"),
        "8": ("mile", "nautical_mile"),
        "9": ("inch", "yard"),
        "10": ("foot", "mile"),
        "11": ("yard", "foot"),
        "12": ("mile", "foot"),
        "13": ("nautical_mile", "mile"),
        "14": ("inch", "centimeter"),  # cross
        "15": ("foot", "meter"),  # cross
        "16": ("mile", "kilometer"),  # cross
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        if to_unit in ["centimeter", "meter", "kilometer"]:
            # Cross-system conversion
            if from_unit == "inch":
                return value * LENGTH_CROSS["inch_to_cm"]
            elif from_unit == "foot":
                return value * LENGTH_CROSS["foot_to_m"]
            elif from_unit == "mile":
                return value * LENGTH_CROSS["mile_to_km"]
        else:
            return value * (LENGTH_IMPERIAL["units"][from_unit] / LENGTH_IMPERIAL["units"][to_unit])
    return None


# =========================================== AREA METRIC CONVERTERS
def area_metric_converter(choice, value):
    conversions = {
        "1": ("mm²", "cm²"),
        "2": ("cm²", "dm²"),
        "3": ("dm²", "m²"),
        "4": ("m²", "dam²"),
        "5": ("dam²", "hm²"),
        "6": ("hm²", "km²"),
        "7": ("m²", "are"),
        "8": ("are", "decare"),
        "9": ("decare", "hectare"),
        "10": ("m²", "hectare"),
        "11": ("cm²", "m²"),
        "12": ("mm²", "m²"),
        "13": ("km²", "hectare"),
        "14": ("hectare", "m²"),
        "15": ("m²", "cm²"),
        "16": ("km²", "m²"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        return value * (AREA_METRIC["units"][from_unit] / AREA_METRIC["units"][to_unit])
    return None


# =========================================== AREA IMPERIAL CONVERTERS
def area_imperial_converter(choice, value):
    conversions = {
        "1": ("in²", "ft²"),
        "2": ("ft²", "yd²"),
        "3": ("yd²", "ch²"),
        "4": ("ch²", "acre"),
        "5": ("acre", "mi²"),
        "6": ("mi²", "section"),
        "7": ("section", "township"),
        "8": ("ft²", "acre"),
        "9": ("acre", "ft²"),
        "10": ("mi²", "acre"),
        "11": ("ft²", "m²"),  # cross
        "12": ("acre", "m²"),  # cross
        "13": ("mi²", "km²"),  # cross
        "14": ("m²", "ft²"),  # cross
        "15": ("m²", "acre"),  # cross
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        if to_unit in ["m²", "km²"]:
            # Cross-system conversion
            if from_unit == "ft²":
                return value * AREA_CROSS["ft2_to_m2"]
            elif from_unit == "acre":
                return value * AREA_CROSS["acre_to_m2"]
            elif from_unit == "mi²":
                return value * AREA_CROSS["mi2_to_km2"]
        elif from_unit in ["m²", "km²"]:
            # Cross-system conversion (reverse)
            if from_unit == "m²" and to_unit == "ft²":
                return value * AREA_CROSS["m2_to_ft2"]
            elif from_unit == "m²" and to_unit == "acre":
                return value * AREA_CROSS["m2_to_acre"]
            elif from_unit == "km²" and to_unit == "mi²":
                return value * AREA_CROSS["km2_to_mi2"]
        else:
            return value * (AREA_IMPERIAL["units"][from_unit] / AREA_IMPERIAL["units"][to_unit])
    return None


# =========================================== VOLUME METRIC CONVERTERS
def volume_metric_converter(choice, value):
    conversions = {
        "1": ("ml", "cl"),
        "2": ("cl", "dl"),
        "3": ("dl", "liter"),
        "4": ("liter", "dal"),
        "5": ("dal", "hl"),
        "6": ("hl", "m³"),
        "7": ("m³", "km³"),
        "8": ("ml", "cm³"),
        "9": ("liter", "dm³"),
        "10": ("mm³", "cm³"),
        "11": ("cm³", "liter"),
        "12": ("liter", "m³"),
        "13": ("m³", "liter"),
        "14": ("ml", "liter"),
        "15": ("liter", "ml"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        return value * (VOLUME_METRIC["units"][from_unit] / VOLUME_METRIC["units"][to_unit])
    return None


# =========================================== VOLUME US CONVERTERS
def volume_us_converter(choice, value):
    conversions = {
        "1": ("us_minim", "us_fluid_dram"),
        "2": ("us_fluid_dram", "us_fluid_ounce"),
        "3": ("us_fluid_ounce", "us_shot"),
        "4": ("us_shot", "us_jigger"),
        "5": ("us_jigger", "us_cup"),
        "6": ("us_cup", "us_pint"),
        "7": ("us_pint", "us_quart"),
        "8": ("us_quart", "us_gallon"),
        "9": ("us_gallon", "us_barrel"),
        "10": ("us_fluid_ounce", "ml"),  # cross
        "11": ("us_pint", "liter"),  # cross
        "12": ("us_quart", "liter"),  # cross
        "13": ("us_gallon", "liter"),  # cross
        "14": ("ml", "us_fluid_ounce"),  # cross
        "15": ("liter", "us_gallon"),  # cross
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        if to_unit in ["ml", "liter"]:
            if from_unit == "us_fluid_ounce":
                return value * VOLUME_CROSS["us_floz_to_ml"]
            elif from_unit == "us_pint":
                return value * VOLUME_CROSS["us_pt_to_L"]
            elif from_unit == "us_quart":
                return value * VOLUME_CROSS["us_qt_to_L"]
            elif from_unit == "us_gallon":
                return value * VOLUME_CROSS["us_gal_to_L"]
        elif from_unit in ["ml", "liter"] and to_unit in ["us_fluid_ounce", "us_gallon"]:
            if from_unit == "ml" and to_unit == "us_fluid_ounce":
                return value / VOLUME_CROSS["us_floz_to_ml"]
            elif from_unit == "liter" and to_unit == "us_gallon":
                return value / VOLUME_CROSS["us_gal_to_L"]
        else:
            return value * (VOLUME_IMPERIAL["units"][from_unit] / VOLUME_IMPERIAL["units"][to_unit])
    return None


# =========================================== VOLUME UK CONVERTERS
def volume_uk_converter(choice, value):
    conversions = {
        "1": ("uk_minim", "uk_fluid_dram"),
        "2": ("uk_fluid_dram", "uk_fluid_ounce"),
        "3": ("uk_fluid_ounce", "uk_pint"),
        "4": ("uk_pint", "uk_quart"),
        "5": ("uk_quart", "uk_gallon"),
        "6": ("uk_gallon", "uk_peck"),
        "7": ("uk_peck", "uk_bushel"),
        "8": ("uk_bushel", "uk_barrel"),
        "9": ("uk_fluid_ounce", "ml"),  # cross
        "10": ("uk_pint", "liter"),  # cross
        "11": ("uk_gallon", "liter"),  # cross
        "12": ("liter", "uk_gallon"),  # cross
        "13": ("ml", "uk_fluid_ounce"),  # cross
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        if to_unit in ["ml", "liter"]:
            if from_unit == "uk_fluid_ounce":
                return value * VOLUME_CROSS["uk_floz_to_ml"]
            elif from_unit == "uk_pint":
                return value * VOLUME_CROSS["uk_pt_to_L"]
            elif from_unit == "uk_gallon":
                return value * VOLUME_CROSS["uk_gal_to_L"]
        elif from_unit in ["ml", "liter"] and to_unit in ["uk_fluid_ounce", "uk_gallon"]:
            if from_unit == "ml" and to_unit == "uk_fluid_ounce":
                return value / VOLUME_CROSS["uk_floz_to_ml"]
            elif from_unit == "liter" and to_unit == "uk_gallon":
                return value / VOLUME_CROSS["uk_gal_to_L"]
        else:
            return value * (VOLUME_UK["units"][from_unit] / VOLUME_UK["units"][to_unit])
    return None


# =========================================== WEIGHT METRIC CONVERTERS
def weight_metric_converter(choice, value):
    conversions = {
        "1": ("microgram", "milligram"),
        "2": ("milligram", "centigram"),
        "3": ("centigram", "decigram"),
        "4": ("decigram", "gram"),
        "5": ("gram", "decagram"),
        "6": ("decagram", "hectogram"),
        "7": ("hectogram", "kilogram"),
        "8": ("kilogram", "megagram"),
        "9": ("megagram", "ton"),
        "10": ("ton", "gigagram"),
        "11": ("gram", "kilogram"),
        "12": ("kilogram", "ton"),
        "13": ("milligram", "gram"),
        "14": ("kilogram", "gram"),
        "15": ("ton", "kilogram"),
        "16": ("microgram", "gram"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        return value * (WEIGHT_METRIC["units"][from_unit] / WEIGHT_METRIC["units"][to_unit])
    return None


# =========================================== WEIGHT IMPERIAL CONVERTERS
def weight_imperial_converter(choice, value):
    conversions = {
        "1": ("grain", "dram"),
        "2": ("dram", "ounce"),
        "3": ("ounce", "pound"),
        "4": ("pound", "stone"),
        "5": ("stone", "quarter"),
        "6": ("quarter", "hundredweight"),
        "7": ("hundredweight", "ton"),
        "8": ("ton", "short_ton"),
        "9": ("ounce", "gram"),  # cross
        "10": ("pound", "kilogram"),  # cross
        "11": ("stone", "kilogram"),  # cross
        "12": ("ton", "kilogram"),  # cross
        "13": ("gram", "ounce"),  # cross
        "14": ("kilogram", "pound"),  # cross
        "15": ("kilogram", "stone"),  # cross
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        if to_unit in ["gram", "kilogram"]:
            if from_unit == "ounce":
                return value * WEIGHT_CROSS["oz_to_g"]
            elif from_unit == "pound":
                return value * WEIGHT_CROSS["lb_to_kg"]
            elif from_unit == "stone":
                return value * WEIGHT_CROSS["stone_to_kg"]
            elif from_unit == "ton":
                return value * WEIGHT_CROSS["ton_to_kg"]
        elif from_unit in ["gram", "kilogram"] and to_unit in ["ounce", "pound", "stone"]:
            if from_unit == "gram" and to_unit == "ounce":
                return value * WEIGHT_CROSS["g_to_oz"]
            elif from_unit == "kilogram" and to_unit == "pound":
                return value * WEIGHT_CROSS["kg_to_lb"]
            elif from_unit == "kilogram" and to_unit == "stone":
                return value * WEIGHT_CROSS["kg_to_st"]
        else:
            return value * (WEIGHT_IMPERIAL["units"][from_unit] / WEIGHT_IMPERIAL["units"][to_unit])
    return None


# =========================================== TEMPERATURE CONVERTERS
def temperature_converter(choice, value):
    if choice == "1":  # °C to °F
        return (value * 9 / 5) + 32
    elif choice == "2":  # °F to °C
        return (value - 32) * 5 / 9
    elif choice == "3":  # °C to K
        return value + 273.15
    elif choice == "4":  # K to °C
        return value - 273.15
    elif choice == "5":  # °F to K
        return (value - 32) * 5 / 9 + 273.15
    elif choice == "6":  # K to °F
        return (value - 273.15) * 9 / 5 + 32
    elif choice == "7":  # °C to Rankine
        return (value + 273.15) * 9 / 5
    elif choice == "8":  # Rankine to °C
        return (value - 491.67) * 5 / 9
    elif choice == "9":  # °F to Rankine
        return value + 459.67
    elif choice == "10":  # Rankine to °F
        return value - 459.67
    return None


# =========================================== SPEED CONVERTERS
def speed_converter(choice, value):
    conversions = {
        "1": ("m/s", "km/h"),
        "2": ("km/h", "m/s"),
        "3": ("mph", "m/s"),
        "4": ("m/s", "mph"),
        "5": ("knot", "m/s"),
        "6": ("m/s", "knot"),
        "7": ("ft/s", "m/s"),
        "8": ("m/s", "ft/s"),
        "9": ("mach", "m/s"),
        "10": ("m/s", "mach"),
        "11": ("mph", "km/h"),
        "12": ("km/h", "mph"),
        "13": ("knot", "km/h"),
        "14": ("km/h", "knot"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        # Base unit is m/s
        if to_unit == "m/s":
            return value * (SPEED["units"][from_unit] / SPEED["units"]["m/s"])
        elif from_unit == "m/s":
            return value * (SPEED["units"]["m/s"] / SPEED["units"][to_unit])
        else:
            # Convert from_unit to m/s then to to_unit
            in_ms = value * (SPEED["units"][from_unit] / SPEED["units"]["m/s"])
            return in_ms * (SPEED["units"]["m/s"] / SPEED["units"][to_unit])
    return None


# =========================================== PRESSURE CONVERTERS
def pressure_converter(choice, value):
    conversions = {
        "1": ("Pa", "kPa"),
        "2": ("kPa", "MPa"),
        "3": ("atm", "Pa"),
        "4": ("PSI", "Pa"),
        "5": ("bar", "Pa"),
        "6": ("mmHg", "Pa"),
        "7": ("inHg", "Pa"),
        "8": ("torr", "Pa"),
        "9": ("kgf/cm²", "Pa"),
        "10": ("inH2O", "Pa"),
        "11": ("Pa", "atm"),
        "12": ("Pa", "PSI"),
        "13": ("Pa", "bar"),
        "14": ("kPa", "Pa"),
        "15": ("MPa", "kPa"),
        "16": ("Pa", "mmHg"),
        "17": ("Pa", "inHg"),
        "18": ("Pa", "torr"),
        "19": ("Pa", "kgf/cm²"),
        "20": ("Pa", "inH2O"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        return value * (PRESSURE["units"][from_unit] / PRESSURE["units"][to_unit])
    return None


# =========================================== ENERGY CONVERTERS
def energy_converter(choice, value):
    conversions = {
        "1": ("J", "kJ"),
        "2": ("kJ", "MJ"),
        "3": ("MJ", "GJ"),
        "4": ("cal", "J"),
        "5": ("kcal", "J"),
        "6": ("Wh", "J"),
        "7": ("kWh", "J"),
        "8": ("MWh", "J"),
        "9": ("eV", "J"),
        "10": ("keV", "J"),
        "11": ("MeV", "J"),
        "12": ("GeV", "J"),
        "13": ("BTU", "J"),
        "14": ("ftlb", "J"),
        "15": ("hp_h", "J"),
        "16": ("therm", "J"),
        "17": ("J", "cal"),
        "18": ("J", "kWh"),
        "19": ("J", "eV"),
        "20": ("J", "BTU"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        return value * (ENERGY["units"][from_unit] / ENERGY["units"][to_unit])
    return None


# =========================================== POWER CONVERTERS
def power_converter(choice, value):
    conversions = {
        "1": ("W", "kW"),
        "2": ("kW", "MW"),
        "3": ("MW", "GW"),
        "4": ("GW", "TW"),
        "5": ("hp", "W"),
        "6": ("BTU/h", "W"),
        "7": ("kcal/h", "W"),
        "8": ("ftlb/s", "W"),
        "9": ("W", "hp"),
        "10": ("W", "BTU/h"),
        "11": ("kW", "hp"),
        "12": ("hp", "kW"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        return value * (POWER["units"][from_unit] / POWER["units"][to_unit])
    return None


# =========================================== FREQUENCY CONVERTERS
def frequency_converter(choice, value):
    conversions = {
        "1": ("Hz", "kHz"),
        "2": ("kHz", "MHz"),
        "3": ("MHz", "GHz"),
        "4": ("GHz", "THz"),
        "5": ("rpm", "Hz"),
        "6": ("Hz", "rpm"),
        "7": ("kHz", "Hz"),
        "8": ("MHz", "Hz"),
        "9": ("GHz", "Hz"),
        "10": ("THz", "Hz"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        return value * (FREQUENCY["units"][from_unit] / FREQUENCY["units"][to_unit])
    return None


# =========================================== ANGLE CONVERTERS
def angle_converter(choice, value):
    conversions = {
        "1": ("degree", "radian"),
        "2": ("radian", "degree"),
        "3": ("degree", "gradian"),
        "4": ("gradian", "degree"),
        "5": ("degree", "revolution"),
        "6": ("revolution", "degree"),
        "7": ("degree", "arcminute"),
        "8": ("arcminute", "degree"),
        "9": ("arcminute", "arcsecond"),
        "10": ("arcsecond", "arcminute"),
        "11": ("radian", "milliradian"),
        "12": ("milliradian", "radian"),
        "13": ("degree", "radian"),
        "14": ("radian", "degree"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        return value * (ANGLE["units"][from_unit] / ANGLE["units"][to_unit])
    return None


# =========================================== DENSITY CONVERTERS
def density_converter(choice, value):
    conversions = {
        "1": ("kg/m³", "g/cm³"),
        "2": ("g/cm³", "kg/m³"),
        "3": ("g/cm³", "g/mL"),
        "4": ("g/cm³", "kg/L"),
        "5": ("lb/ft³", "kg/m³"),
        "6": ("kg/m³", "lb/ft³"),
        "7": ("lb/in³", "kg/m³"),
        "8": ("oz/in³", "kg/m³"),
        "9": ("g/mL", "g/cm³"),
        "10": ("kg/L", "g/cm³"),
    }

    if choice in conversions:
        from_unit, to_unit = conversions[choice]
        return value * (DENSITY["units"][from_unit] / DENSITY["units"][to_unit])
    return None


# =========================================== MASTER CONVERTER
def convert(converter_type, choice, value):
    converters = {
        "1": time_converter,
        "2": data_binary_converter,
        "3": data_decimal_converter,
        "4": length_metric_converter,
        "5": length_imperial_converter,
        "6": area_metric_converter,
        "7": area_imperial_converter,
        "8": volume_metric_converter,
        "9": volume_us_converter,
        "10": volume_uk_converter,
        "11": weight_metric_converter,
        "12": weight_imperial_converter,
        "13": temperature_converter,
        "14": speed_converter,
        "15": pressure_converter,
        "16": energy_converter,
        "17": power_converter,
        "18": frequency_converter,
        "19": angle_converter,
        "20": density_converter,
    }

    if converter_type in converters:
        return converters[converter_type](choice, value)
    return None


# =========================================== GET UNIT LABEL
def get_unit_label(converter_type, unit_key):
    unit_maps = {
        "1": TIME["labels"],
        "2": DATA_BINARY["labels"],
        "3": DATA_DECIMAL["labels"],
        "4": LENGTH_METRIC["labels"],
        "5": LENGTH_IMPERIAL["labels"],
        "6": AREA_METRIC["labels"],
        "7": AREA_IMPERIAL["labels"],
        "8": VOLUME_METRIC["labels"],
        "9": VOLUME_IMPERIAL["labels"],
        "10": VOLUME_UK["labels"],
        "11": WEIGHT_METRIC["labels"],
        "12": WEIGHT_IMPERIAL["labels"],
        "13": TEMPERATURE["labels"] if "labels" in TEMPERATURE else {"C": "°C", "F": "°F", "K": "K"},
        "14": SPEED["labels"],
        "15": PRESSURE["labels"],
        "16": ENERGY["labels"],
        "17": POWER["labels"],
        "18": FREQUENCY["labels"],
        "19": ANGLE["labels"],
        "20": DENSITY["labels"],
    }

    if converter_type in unit_maps and unit_key in unit_maps[converter_type]:
        return unit_maps[converter_type][unit_key]
    return unit_key
