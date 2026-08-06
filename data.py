# Data.py - Complete conversion constants, mappings, labels, and metadata

# =========================================== TIME
TIME = {
    # Base unit: second
    "units": {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800,
        "month": 2629800,      # 30.44 days average
        "year": 31557600,      # 365.25 days average
        "decade": 315576000,
        "century": 3155760000,
        "millennium": 31557600000,
    },
    "labels": {
        "second": "s",
        "minute": "min",
        "hour": "h",
        "day": "d",
        "week": "wk",
        "month": "mo",
        "year": "yr",
        "decade": "dec",
        "century": "c",
        "millennium": "milen",
    },
    "conversions": {
        "s_to_min": 60,
        "min_to_h": 60,
        "h_to_d": 24,
        "d_to_wk": 7,
        "wk_to_mo": 4.34524,
        "mo_to_yr": 12,
        "yr_to_dec": 10,
        "dec_to_c": 10,
        "c_to_milen": 10,
    }
}

# =========================================== DATA STORAGE (Binary - 1024 based)
DATA_BINARY = {
    # Base unit: byte
    "units": {
        "bit": 0.125,
        "byte": 1,
        "KB": 1024,
        "MB": 1048576,
        "GB": 1073741824,
        "TB": 1099511627776,
        "PB": 1125899906842624,
        "EB": 1152921504606846976,
        "ZB": 1180591620717411303424,
        "YB": 1208925819614629174706176,
    },
    "labels": {
        "bit": "b",
        "byte": "B",
        "KB": "KB",
        "MB": "MB",
        "GB": "GB",
        "TB": "TB",
        "PB": "PB",
        "EB": "EB",
        "ZB": "ZB",
        "YB": "YB",
    },
    "conversions": {
        "b_to_B": 8,
        "B_to_KB": 1024,
        "KB_to_MB": 1024,
        "MB_to_GB": 1024,
        "GB_to_TB": 1024,
        "TB_to_PB": 1024,
        "PB_to_EB": 1024,
        "EB_to_ZB": 1024,
        "ZB_to_YB": 1024,
    }
}

# =========================================== DATA STORAGE (Decimal - 1000 based)
DATA_DECIMAL = {
    # Base unit: byte
    "units": {
        "bit": 0.125,
        "byte": 1,
        "kB": 1000,
        "MB": 1000000,
        "GB": 1000000000,
        "TB": 1000000000000,
        "PB": 1000000000000000,
        "EB": 1000000000000000000,
        "ZB": 1000000000000000000000,
        "YB": 1000000000000000000000000,
    },
    "labels": {
        "bit": "b",
        "byte": "B",
        "kB": "kB",
        "MB": "MB",
        "GB": "GB",
        "TB": "TB",
        "PB": "PB",
        "EB": "EB",
        "ZB": "ZB",
        "YB": "YB",
    },
    "conversions": {
        "b_to_B": 8,
        "B_to_kB": 1000,
        "kB_to_MB": 1000,
        "MB_to_GB": 1000,
        "GB_to_TB": 1000,
        "TB_to_PB": 1000,
        "PB_to_EB": 1000,
        "EB_to_ZB": 1000,
        "ZB_to_YB": 1000,
    }
}

# =========================================== LENGTH / DISTANCE (Metric)
LENGTH_METRIC = {
    # Base unit: meter
    "units": {
        "nanometer": 1e-9,
        "micrometer": 1e-6,
        "millimeter": 0.001,
        "centimeter": 0.01,
        "decimeter": 0.1,
        "meter": 1,
        "decameter": 10,
        "hectometer": 100,
        "kilometer": 1000,
        "megameter": 1000000,
        "gigameter": 1000000000,
    },
    "labels": {
        "nanometer": "nm",
        "micrometer": "µm",
        "millimeter": "mm",
        "centimeter": "cm",
        "decimeter": "dm",
        "meter": "m",
        "decameter": "dam",
        "hectometer": "hm",
        "kilometer": "km",
        "megameter": "Mm",
        "gigameter": "Gm",
    },
    "conversions": {
        "nm_to_µm": 1000,
        "µm_to_mm": 1000,
        "mm_to_cm": 10,
        "cm_to_dm": 10,
        "dm_to_m": 10,
        "m_to_dam": 10,
        "dam_to_hm": 10,
        "hm_to_km": 10,
        "km_to_Mm": 1000,
        "Mm_to_Gm": 1000,
    }
}

# =========================================== LENGTH / DISTANCE (Imperial / US)
LENGTH_IMPERIAL = {
    # Base unit: inch
    "units": {
        "thou": 0.001,
        "inch": 1,
        "foot": 12,
        "yard": 36,
        "chain": 792,
        "furlong": 7920,
        "mile": 63360,
        "league": 190080,
        "nautical_mile": 72913.4,
    },
    "labels": {
        "thou": "thou",
        "inch": "in",
        "foot": "ft",
        "yard": "yd",
        "chain": "ch",
        "furlong": "fur",
        "mile": "mi",
        "league": "lea",
        "nautical_mile": "NM",
    },
    "conversions": {
        "thou_to_in": 1000,
        "in_to_ft": 12,
        "ft_to_yd": 3,
        "yd_to_ch": 22,
        "ch_to_fur": 10,
        "fur_to_mi": 8,
        "mi_to_lea": 3,
        "mi_to_NM": 0.868976,
    }
}

# =========================================== LENGTH (Cross-system)
LENGTH_CROSS = {
    "inch_to_cm": 2.54,
    "foot_to_m": 0.3048,
    "yard_to_m": 0.9144,
    "mile_to_km": 1.609344,
    "nautical_mile_to_km": 1.852,
    "km_to_mile": 0.621371,
    "m_to_foot": 3.28084,
    "cm_to_inch": 0.393701,
}

# =========================================== AREA (Metric)
AREA_METRIC = {
    # Base unit: square meter
    "units": {
        "mm²": 1e-6,
        "cm²": 0.0001,
        "dm²": 0.01,
        "m²": 1,
        "dam²": 100,
        "hm²": 10000,
        "km²": 1000000,
        "hectare": 10000,
        "are": 100,
        "decare": 1000,
    },
    "labels": {
        "mm²": "mm²",
        "cm²": "cm²",
        "dm²": "dm²",
        "m²": "m²",
        "dam²": "dam²",
        "hm²": "hm²",
        "km²": "km²",
        "hectare": "ha",
        "are": "a",
        "decare": "daa",
    },
    "conversions": {
        "mm2_to_cm2": 100,
        "cm2_to_dm2": 100,
        "dm2_to_m2": 100,
        "m2_to_dam2": 100,
        "dam2_to_hm2": 100,
        "hm2_to_km2": 100,
        "m2_to_are": 100,
        "are_to_da": 10,
        "da_to_ha": 10,
        "m2_to_ha": 10000,
    }
}

# =========================================== AREA (Imperial / US)
AREA_IMPERIAL = {
    # Base unit: square foot
    "units": {
        "in²": 0.00694444,
        "ft²": 1,
        "yd²": 9,
        "ch²": 4356,
        "acre": 43560,
        "mi²": 27878400,
        "section": 27878400,
        "township": 1003622400,
    },
    "labels": {
        "in²": "in²",
        "ft²": "ft²",
        "yd²": "yd²",
        "ch²": "ch²",
        "acre": "ac",
        "mi²": "mi²",
        "section": "section",
        "township": "township",
    },
    "conversions": {
        "in2_to_ft2": 144,
        "ft2_to_yd2": 9,
        "yd2_to_ch2": 484,
        "ch2_to_acre": 10,
        "acre_to_mi2": 640,
        "mi2_to_section": 1,
        "section_to_twp": 36,
    }
}

# =========================================== AREA (Cross-system)
AREA_CROSS = {
    "m2_to_ft2": 10.7639,
    "m2_to_acre": 0.000247105,
    "m2_to_mi2": 3.861e-7,
    "ft2_to_m2": 0.092903,
    "acre_to_m2": 4046.856,
    "mi2_to_km2": 2.58999,
    "km2_to_mi2": 0.386102,
    "ha_to_acre": 2.47105,
    "acre_to_ha": 0.404686,
}

# =========================================== VOLUME (Metric)
VOLUME_METRIC = {
    # Base unit: liter
    "units": {
        "ml": 0.001,
        "cl": 0.01,
        "dl": 0.1,
        "liter": 1,
        "dal": 10,
        "hl": 100,
        "m³": 1000,
        "km³": 1e12,
        "mm³": 1e-6,
        "cm³": 0.001,
        "dm³": 1,
    },
    "labels": {
        "ml": "mL",
        "cl": "cL",
        "dl": "dL",
        "liter": "L",
        "dal": "daL",
        "hl": "hL",
        "m³": "m³",
        "km³": "km³",
        "mm³": "mm³",
        "cm³": "cm³",
        "dm³": "dm³",
    },
    "conversions": {
        "ml_to_cl": 10,
        "cl_to_dl": 10,
        "dl_to_L": 10,
        "L_to_daL": 10,
        "daL_to_hL": 10,
        "hL_to_m3": 10,
        "L_to_m3": 1000,
        "m3_to_km3": 1e9,
        "ml_to_cm3": 1,
        "L_to_dm3": 1,
    }
}

# =========================================== VOLUME (Imperial / US)
VOLUME_IMPERIAL = {
    # Base unit: US gallon
    "units": {
        "us_minim": 1.536e-5,
        "us_fluid_dram": 0.00390625,
        "us_fluid_ounce": 0.0078125,
        "us_shot": 0.015625,
        "us_jigger": 0.046875,
        "us_cup": 0.0625,
        "us_pint": 0.125,
        "us_quart": 0.25,
        "us_gallon": 1,
        "us_barrel": 31.5,
    },
    "labels": {
        "us_minim": "min",
        "us_fluid_dram": "fl dr",
        "us_fluid_ounce": "fl oz",
        "us_shot": "shot",
        "us_jigger": "jigger",
        "us_cup": "cup",
        "us_pint": "pt",
        "us_quart": "qt",
        "us_gallon": "gal",
        "us_barrel": "bbl",
    },
    "conversions": {
        "minim_to_dram": 60,
        "dram_to_floz": 8,
        "floz_to_shot": 2,
        "shot_to_jigger": 3,
        "jigger_to_cup": 1.33333,
        "cup_to_pt": 2,
        "pt_to_qt": 2,
        "qt_to_gal": 4,
        "gal_to_bbl": 31.5,
    }
}

# =========================================== VOLUME (Imperial UK)
VOLUME_UK = {
    # Base unit: Imperial gallon
    "units": {
        "uk_minim": 1.302e-5,
        "uk_fluid_dram": 0.003125,
        "uk_fluid_ounce": 0.00625,
        "uk_pint": 0.125,
        "uk_quart": 0.25,
        "uk_gallon": 1,
        "uk_peck": 2.5,
        "uk_bushel": 10,
        "uk_barrel": 42,
    },
    "labels": {
        "uk_minim": "min",
        "uk_fluid_dram": "fl dr",
        "uk_fluid_ounce": "fl oz",
        "uk_pint": "pt",
        "uk_quart": "qt",
        "uk_gallon": "gal",
        "uk_peck": "pk",
        "uk_bushel": "bu",
        "uk_barrel": "bbl",
    },
    "conversions": {
        "minim_to_dram": 60,
        "dram_to_floz": 8,
        "floz_to_pt": 20,
        "pt_to_qt": 2,
        "qt_to_gal": 4,
        "gal_to_pk": 2.5,
        "pk_to_bu": 4,
        "bu_to_bbl": 4.2,
    }
}

# =========================================== VOLUME (Cross-system)
VOLUME_CROSS = {
    "us_gal_to_L": 3.78541,
    "uk_gal_to_L": 4.54609,
    "us_qt_to_L": 0.946353,
    "uk_qt_to_L": 1.13652,
    "us_pt_to_L": 0.473176,
    "uk_pt_to_L": 0.568261,
    "us_cup_to_L": 0.236588,
    "us_floz_to_ml": 29.5735,
    "uk_floz_to_ml": 28.4131,
    "L_to_us_gal": 0.264172,
    "L_to_uk_gal": 0.219969,
    "m3_to_us_gal": 264.172,
    "m3_to_uk_gal": 219.969,
}

# =========================================== WEIGHT / MASS (Metric)
WEIGHT_METRIC = {
    # Base unit: gram
    "units": {
        "microgram": 1e-6,
        "milligram": 0.001,
        "centigram": 0.01,
        "decigram": 0.1,
        "gram": 1,
        "decagram": 10,
        "hectogram": 100,
        "kilogram": 1000,
        "megagram": 1000000,
        "ton": 1000000,
        "gigagram": 1000000000,
    },
    "labels": {
        "microgram": "µg",
        "milligram": "mg",
        "centigram": "cg",
        "decigram": "dg",
        "gram": "g",
        "decagram": "dag",
        "hectogram": "hg",
        "kilogram": "kg",
        "megagram": "Mg",
        "ton": "t",
        "gigagram": "Gg",
    },
    "conversions": {
        "µg_to_mg": 1000,
        "mg_to_cg": 10,
        "cg_to_dg": 10,
        "dg_to_g": 10,
        "g_to_dag": 10,
        "dag_to_hg": 10,
        "hg_to_kg": 10,
        "kg_to_Mg": 1000,
        "Mg_to_t": 1,
        "t_to_Gg": 1000,
    }
}

# =========================================== WEIGHT / MASS (Imperial / US)
WEIGHT_IMPERIAL = {
    # Base unit: pound
    "units": {
        "grain": 1/7000,
        "dram": 0.0625,
        "ounce": 0.0625,
        "pound": 1,
        "stone": 14,
        "quarter": 28,
        "hundredweight": 112,
        "ton": 2240,
        "short_ton": 2000,
    },
    "labels": {
        "grain": "gr",
        "dram": "dr",
        "ounce": "oz",
        "pound": "lb",
        "stone": "st",
        "quarter": "qr",
        "hundredweight": "cwt",
        "ton": "ton",
        "short_ton": "sh tn",
    },
    "conversions": {
        "gr_to_dr": 27.34375,
        "dr_to_oz": 16,
        "oz_to_lb": 16,
        "lb_to_st": 14,
        "st_to_qr": 2,
        "qr_to_cwt": 4,
        "cwt_to_ton": 20,
        "ton_to_sh_tn": 0.892857,
    }
}

# =========================================== WEIGHT (Cross-system)
WEIGHT_CROSS = {
    "lb_to_kg": 0.453592,
    "oz_to_g": 28.3495,
    "stone_to_kg": 6.35029,
    "ton_to_kg": 1016.05,
    "short_ton_to_kg": 907.185,
    "kg_to_lb": 2.20462,
    "g_to_oz": 0.035274,
    "kg_to_st": 0.157473,
}

# =========================================== TEMPERATURE
TEMPERATURE = {
    "formulas": {
        "c_to_f": "°F = (°C × 9/5) + 32",
        "f_to_c": "°C = (°F - 32) × 5/9",
        "c_to_k": "K = °C + 273.15",
        "k_to_c": "°C = K - 273.15",
        "f_to_k": "K = (°F - 32) × 5/9 + 273.15",
        "k_to_f": "°F = (K - 273.15) × 9/5 + 32",
        "c_to_rankine": "°R = (°C + 273.15) × 9/5",
        "rankine_to_c": "°C = (°R - 491.67) × 5/9",
        "f_to_rankine": "°R = °F + 459.67",
        "rankine_to_f": "°F = °R - 459.67",
    },
    "fixed_points": {
        "absolute_zero_C": -273.15,
        "absolute_zero_F": -459.67,
        "water_freeze_C": 0,
        "water_freeze_F": 32,
        "water_boil_C": 100,
        "water_boil_F": 212,
        "water_boil_K": 373.15,
    }
}

# =========================================== SPEED
SPEED = {
    # Base unit: m/s
    "units": {
        "m/s": 1,
        "km/h": 0.277778,
        "mph": 0.44704,
        "ft/s": 0.3048,
        "knot": 0.514444,
        "mach": 343,           # at sea level
        "speed_of_light": 299792458,
    },
    "labels": {
        "m/s": "m/s",
        "km/h": "km/h",
        "mph": "mph",
        "ft/s": "ft/s",
        "knot": "kn",
        "mach": "Mach",
        "speed_of_light": "c",
    },
    "conversions": {
        "ms_to_kmh": 3.6,
        "kmh_to_ms": 0.277778,
        "mph_to_ms": 0.44704,
        "ms_to_mph": 2.23694,
        "knot_to_ms": 0.514444,
        "ms_to_knot": 1.94384,
        "ftps_to_ms": 0.3048,
        "ms_to_ftps": 3.28084,
        "mach_to_ms": 343,
        "ms_to_mach": 0.00291545,
    }
}

# =========================================== PRESSURE
PRESSURE = {
    # Base unit: Pascal
    "units": {
        "Pa": 1,
        "kPa": 1000,
        "MPa": 1000000,
        "bar": 100000,
        "mbar": 100,
        "atm": 101325,
        "mmHg": 133.322,
        "inHg": 3386.39,
        "PSI": 6894.76,
        "torr": 133.322,
        "kgf/cm²": 98066.5,
        "inH2O": 249.089,
    },
    "labels": {
        "Pa": "Pa",
        "kPa": "kPa",
        "MPa": "MPa",
        "bar": "bar",
        "mbar": "mbar",
        "atm": "atm",
        "mmHg": "mmHg",
        "inHg": "inHg",
        "PSI": "psi",
        "torr": "Torr",
        "kgf/cm²": "kgf/cm²",
        "inH2O": "inH₂O",
    },
    "conversions": {
        "Pa_to_kPa": 1000,
        "kPa_to_MPa": 1000,
        "atm_to_Pa": 101325,
        "PSI_to_Pa": 6894.76,
        "bar_to_Pa": 100000,
        "mmHg_to_Pa": 133.322,
        "inHg_to_Pa": 3386.39,
        "torr_to_Pa": 133.322,
        "kgfcm2_to_Pa": 98066.5,
        "inH2O_to_Pa": 249.089,
    }
}

# =========================================== ENERGY
ENERGY = {
    # Base unit: Joule
    "units": {
        "J": 1,
        "kJ": 1000,
        "MJ": 1000000,
        "GJ": 1000000000,
        "cal": 4.184,
        "kcal": 4184,
        "Wh": 3600,
        "kWh": 3600000,
        "MWh": 3600000000,
        "eV": 1.602176634e-19,
        "keV": 1.602176634e-16,
        "MeV": 1.602176634e-13,
        "GeV": 1.602176634e-10,
        "BTU": 1055.06,
        "ftlb": 1.35582,
        "hp_h": 2684519.54,
        "therm": 105506000,
    },
    "labels": {
        "J": "J",
        "kJ": "kJ",
        "MJ": "MJ",
        "GJ": "GJ",
        "cal": "cal",
        "kcal": "kcal",
        "Wh": "Wh",
        "kWh": "kWh",
        "MWh": "MWh",
        "eV": "eV",
        "keV": "keV",
        "MeV": "MeV",
        "GeV": "GeV",
        "BTU": "BTU",
        "ftlb": "ft·lb",
        "hp_h": "hp·h",
        "therm": "thm",
    },
    "conversions": {
        "J_to_kJ": 1000,
        "cal_to_J": 4.184,
        "kcal_to_J": 4184,
        "Wh_to_J": 3600,
        "kWh_to_J": 3600000,
        "MWh_to_J": 3600000000,
        "eV_to_J": 1.602176634e-19,
        "BTU_to_J": 1055.06,
        "ftlb_to_J": 1.35582,
        "hp_h_to_J": 2684519.54,
        "therm_to_J": 105506000,
    }
}

# =========================================== POWER
POWER = {
    # Base unit: Watt
    "units": {
        "W": 1,
        "kW": 1000,
        "MW": 1000000,
        "GW": 1000000000,
        "TW": 1000000000000,
        "hp": 745.7,
        "BTU/h": 0.293071,
        "kcal/h": 1.163,
        "ftlb/s": 1.35582,
    },
    "labels": {
        "W": "W",
        "kW": "kW",
        "MW": "MW",
        "GW": "GW",
        "TW": "TW",
        "hp": "hp",
        "BTU/h": "BTU/h",
        "kcal/h": "kcal/h",
        "ftlb/s": "ft·lb/s",
    },
    "conversions": {
        "W_to_kW": 1000,
        "kW_to_MW": 1000,
        "MW_to_GW": 1000,
        "GW_to_TW": 1000,
        "hp_to_W": 745.7,
        "BTUh_to_W": 0.293071,
        "kcalh_to_W": 1.163,
        "ftlbs_to_W": 1.35582,
    }
}

# =========================================== FREQUENCY
FREQUENCY = {
    # Base unit: Hertz
    "units": {
        "Hz": 1,
        "kHz": 1000,
        "MHz": 1000000,
        "GHz": 1000000000,
        "THz": 1000000000000,
        "rpm": 1/60,
    },
    "labels": {
        "Hz": "Hz",
        "kHz": "kHz",
        "MHz": "MHz",
        "GHz": "GHz",
        "THz": "THz",
        "rpm": "rpm",
    },
    "conversions": {
        "Hz_to_kHz": 1000,
        "kHz_to_MHz": 1000,
        "MHz_to_GHz": 1000,
        "GHz_to_THz": 1000,
        "rpm_to_Hz": 60,
        "Hz_to_rpm": 1/60,
    }
}

# =========================================== ANGLE
ANGLE = {
    # Base unit: degree
    "units": {
        "degree": 1,
        "radian": 57.2958,
        "gradian": 0.9,
        "revolution": 360,
        "arcminute": 1/60,
        "arcsecond": 1/3600,
        "milliradian": 0.0572958,
    },
    "labels": {
        "degree": "°",
        "radian": "rad",
        "gradian": "grad",
        "revolution": "rev",
        "arcminute": "'",
        "arcsecond": '"',
        "milliradian": "mrad",
    },
    "conversions": {
        "deg_to_rad": 57.2958,
        "deg_to_grad": 1.11111,
        "deg_to_rev": 360,
        "deg_to_arcmin": 60,
        "arcmin_to_arcsec": 60,
        "rad_to_mrad": 1000,
    }
}

# =========================================== DENSITY
DENSITY = {
    # Base unit: kg/m³
    "units": {
        "kg/m³": 1,
        "g/cm³": 1000,
        "g/mL": 1000,
        "kg/L": 1000,
        "lb/ft³": 16.0185,
        "lb/in³": 27679.9,
        "oz/in³": 1729.99,
    },
    "labels": {
        "kg/m³": "kg/m³",
        "g/cm³": "g/cm³",
        "g/mL": "g/mL",
        "kg/L": "kg/L",
        "lb/ft³": "lb/ft³",
        "lb/in³": "lb/in³",
        "oz/in³": "oz/in³",
    },
    "conversions": {
        "kgm3_to_gcm3": 1000,
        "gcm3_to_kgm3": 0.001,
        "gcm3_to_gmL": 1,
        "gcm3_to_kgL": 1,
        "lbft3_to_kgm3": 16.0185,
        "lbin3_to_kgm3": 27679.9,
        "ozin3_to_kgm3": 1729.99,
    }
}

# =========================================== MENU MAPPING
MENU_OPTIONS = {
    "1": "Time",
    "2": "Data (Binary)",
    "3": "Data (Decimal)",
    "4": "Length (Metric)",
    "5": "Length (Imperial)",
    "6": "Area (Metric)",
    "7": "Area (Imperial)",
    "8": "Volume (Metric)",
    "9": "Volume (US)",
    "10": "Volume (UK)",
    "11": "Weight (Metric)",
    "12": "Weight (Imperial)",
    "13": "Temperature",
    "14": "Speed",
    "15": "Pressure",
    "16": "Energy",
    "17": "Power",
    "18": "Frequency",
    "19": "Angle",
    "20": "Density",
}

# =========================================== ALL UNITS REFERENCE
ALL_UNITS = {
    "time": TIME,
    "data_binary": DATA_BINARY,
    "data_decimal": DATA_DECIMAL,
    "length_metric": LENGTH_METRIC,
    "length_imperial": LENGTH_IMPERIAL,
    "area_metric": AREA_METRIC,
    "area_imperial": AREA_IMPERIAL,
    "volume_metric": VOLUME_METRIC,
    "volume_us": VOLUME_IMPERIAL,
    "volume_uk": VOLUME_UK,
    "weight_metric": WEIGHT_METRIC,
    "weight_imperial": WEIGHT_IMPERIAL,
    "temperature": TEMPERATURE,
    "speed": SPEED,
    "pressure": PRESSURE,
    "energy": ENERGY,
    "power": POWER,
    "frequency": FREQUENCY,
    "angle": ANGLE,
    "density": DENSITY,
}
