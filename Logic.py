"""Conversion engine for Universal Converter MP8V."""

from data import AREA_CROSS, CONVERTER_UNITS, CONVERSIONS, LENGTH_CROSS, MENU_OPTIONS, MENU_LABELS, VOLUME_CROSS, WEIGHT_CROSS

CROSS_FACTORS = {
    ("5", "inch", "centimeter"): LENGTH_CROSS["inch_to_cm"],
    ("5", "foot", "meter"): LENGTH_CROSS["foot_to_m"],
    ("5", "mile", "kilometer"): LENGTH_CROSS["mile_to_km"],
    ("7", "ft²", "m²"): AREA_CROSS["ft2_to_m2"],
    ("7", "acre", "m²"): AREA_CROSS["acre_to_m2"],
    ("7", "mi²", "km²"): AREA_CROSS["mi2_to_km2"],
    ("7", "m²", "ft²"): AREA_CROSS["m2_to_ft2"],
    ("7", "m²", "acre"): AREA_CROSS["m2_to_acre"],
    ("9", "us_fluid_ounce", "mL"): VOLUME_CROSS["us_floz_to_ml"],
    ("9", "us_pint", "L"): VOLUME_CROSS["us_pt_to_L"],
    ("9", "us_quart", "L"): VOLUME_CROSS["us_qt_to_L"],
    ("9", "us_gallon", "L"): VOLUME_CROSS["us_gal_to_L"],
    ("9", "mL", "us_fluid_ounce"): 1 / VOLUME_CROSS["us_floz_to_ml"],
    ("9", "L", "us_gallon"): 1 / VOLUME_CROSS["us_gal_to_L"],
    ("10", "uk_fluid_ounce", "mL"): VOLUME_CROSS["uk_floz_to_ml"],
    ("10", "uk_pint", "L"): VOLUME_CROSS["uk_pt_to_L"],
    ("10", "uk_gallon", "L"): VOLUME_CROSS["uk_gal_to_L"],
    ("10", "L", "uk_gallon"): 1 / VOLUME_CROSS["uk_gal_to_L"],
    ("10", "mL", "uk_fluid_ounce"): 1 / VOLUME_CROSS["uk_floz_to_ml"],
    ("12", "ounce", "gram"): WEIGHT_CROSS["oz_to_g"],
    ("12", "pound", "kilogram"): WEIGHT_CROSS["lb_to_kg"],
    ("12", "stone", "kilogram"): WEIGHT_CROSS["stone_to_kg"],
    ("12", "ton", "kilogram"): WEIGHT_CROSS["ton_to_kg"],
    ("12", "gram", "ounce"): WEIGHT_CROSS["g_to_oz"],
    ("12", "kilogram", "pound"): WEIGHT_CROSS["kg_to_lb"],
    ("12", "kilogram", "stone"): WEIGHT_CROSS["kg_to_st"],
}


def _linear(converter_type, from_unit, to_unit, value):
    units = CONVERTER_UNITS[converter_type]["units"]
    if from_unit not in units or to_unit not in units:
        return None
    return value * units[from_unit] / units[to_unit]


def _temperature(choice, value):
    formulas = {
        "1": lambda x: x * 9 / 5 + 32,
        "2": lambda x: (x - 32) * 5 / 9,
        "3": lambda x: x + 273.15,
        "4": lambda x: x - 273.15,
        "5": lambda x: (x - 32) * 5 / 9 + 273.15,
        "6": lambda x: (x - 273.15) * 9 / 5 + 32,
        "7": lambda x: (x + 273.15) * 9 / 5,
        "8": lambda x: (x - 491.67) * 5 / 9,
        "9": lambda x: x + 459.67,
        "10": lambda x: x - 459.67,
    }
    func = formulas.get(str(choice))
    return func(value) if func else None


def convert(converter_type, choice, value):
    """Convert value for a menu choice; invalid choices return None."""
    converter_type, choice = str(converter_type), str(choice)
    if converter_type == "13":
        return _temperature(choice, value)
    choices = CONVERSIONS.get(converter_type)
    if not choices:
        return None
    try:
        from_unit, to_unit = choices[int(choice) - 1].split("->", 1)
    except (ValueError, IndexError):
        return None
    factor = CROSS_FACTORS.get((converter_type, from_unit, to_unit))
    return value * factor if factor is not None else _linear(converter_type, from_unit, to_unit, value)


def get_unit_label(converter_type, unit_key):
    if str(converter_type) == "13":
        return {"C": "°C", "F": "°F", "K": "K", "R": "°R"}.get(unit_key, unit_key)
    units = CONVERTER_UNITS.get(str(converter_type))
    return units["labels"].get(unit_key, unit_key) if units else unit_key


def get_conversion_pair(converter_type, choice):
    try:
        return CONVERSIONS[str(converter_type)][int(choice) - 1].split("->", 1)
    except (KeyError, ValueError, IndexError):
        return None


def format_result(value, max_digits=12):
    return str(value) if isinstance(value, int) else f"{value:.{max_digits}g}"

__all__ = ["convert", "get_unit_label", "get_conversion_pair", "format_result", "MENU_OPTIONS", "MENU_LABELS"]
