# INOUT.py - Complete User Interface for all 20 converter types
print("\n" + "=" * 60)
print("$ - Hello! Welcome to UCP (Universal Converter Pro)")
print("=" * 60)

from data import MENU_OPTIONS
from Logic import convert, get_unit_label


# =========================================== MAIN MENU
def show_main_menu():
    input("$ - let's start(press enter)!")
    print("$ - Which converter do you want?")
    print("$ -  1 Time")
    print("$ -  2 Data (Binary - 1024)")
    print("$ -  3 Data (Decimal - 1000)")
    print("$ -  4 Length (Metric)")
    print("$ -  5 Length (Imperial)")
    print("$ -  6 Area (Metric)")
    print("$ -  7 Area (Imperial)")
    print("$ -  8 Volume (Metric)")
    print("$ -  9 Volume (US)")
    print("$ - 10 Volume (UK)")
    print("$ - 11 Weight (Metric)")
    print("$ - 12 Weight (Imperial)")
    print("$ - 13 Temperature")
    print("$ - 14 Speed")
    print("$ - 15 Pressure")
    print("$ - 16 Energy")
    print("$ - 17 Power")
    print("$ - 18 Frequency")
    print("$ - 19 Angle")
    print("$ - 20 Density")
    print("$ -  0 Exit")
    print("=" * 60)


# =========================================== SUB-MENUS
def show_time_menu():
    print("\n$ - Time Converter")
    print("$ -  1 Seconds to Minutes")
    print("$ -  2 Minutes to Hours")
    print("$ -  3 Hours to Days")
    print("$ -  4 Days to Weeks")
    print("$ -  5 Weeks to Months")
    print("$ -  6 Months to Years")
    print("$ -  7 Years to Decades")
    print("$ -  8 Decades to Centuries")
    print("$ -  9 Centuries to Millennium")
    print("$ - 10 Seconds to Hours")
    print("$ - 11 Minutes to Days")
    print("$ - 12 Hours to Weeks")
    print("$ - 13 Days to Months")
    print("$ - 14 Months to Years")
    print("$ - 15 Years to Decades")


def show_data_binary_menu():
    print("\n$ - Data Converter (Binary - 1024)")
    print("$ -  1 Bit to Byte")
    print("$ -  2 Byte to KB")
    print("$ -  3 KB to MB")
    print("$ -  4 MB to GB")
    print("$ -  5 GB to TB")
    print("$ -  6 TB to PB")
    print("$ -  7 PB to EB")
    print("$ -  8 EB to ZB")
    print("$ -  9 ZB to YB")
    print("$ - 10 Byte to KB")
    print("$ - 11 KB to MB")
    print("$ - 12 MB to GB")
    print("$ - 13 GB to TB")
    print("$ - 14 TB to PB")
    print("$ - 15 PB to EB")
    print("$ - 16 EB to ZB")
    print("$ - 17 ZB to YB")
    print("$ - 18 Bit to KB")
    print("$ - 19 Byte to MB")
    print("$ - 20 KB to GB")


def show_data_decimal_menu():
    print("\n$ - Data Converter (Decimal - 1000)")
    print("$ -  1 Bit to Byte")
    print("$ -  2 Byte to kB")
    print("$ -  3 kB to MB")
    print("$ -  4 MB to GB")
    print("$ -  5 GB to TB")
    print("$ -  6 TB to PB")
    print("$ -  7 PB to EB")
    print("$ -  8 EB to ZB")
    print("$ -  9 ZB to YB")
    print("$ - 10 Byte to kB")
    print("$ - 11 kB to MB")
    print("$ - 12 MB to GB")
    print("$ - 13 GB to TB")
    print("$ - 14 TB to PB")
    print("$ - 15 PB to EB")
    print("$ - 16 EB to ZB")
    print("$ - 17 ZB to YB")


def show_length_metric_menu():
    print("\n$ - Length (Metric)")
    print("$ -  1 Nanometer to Micrometer")
    print("$ -  2 Micrometer to Millimeter")
    print("$ -  3 Millimeter to Centimeter")
    print("$ -  4 Centimeter to Decimeter")
    print("$ -  5 Decimeter to Meter")
    print("$ -  6 Meter to Decameter")
    print("$ -  7 Decameter to Hectometer")
    print("$ -  8 Hectometer to Kilometer")
    print("$ -  9 Kilometer to Megameter")
    print("$ - 10 Megameter to Gigameter")
    print("$ - 11 Nanometer to Millimeter")
    print("$ - 12 Micrometer to Centimeter")
    print("$ - 13 Millimeter to Meter")
    print("$ - 14 Centimeter to Meter")
    print("$ - 15 Meter to Kilometer")
    print("$ - 16 Kilometer to Meter")
    print("$ - 17 Centimeter to Millimeter")
    print("$ - 18 Meter to Centimeter")
    print("$ - 19 Kilometer to Centimeter")
    print("$ - 20 Meter to Millimeter")


def show_length_imperial_menu():
    print("\n$ - Length (Imperial)")
    print("$ -  1 Thou to Inch")
    print("$ -  2 Inch to Foot")
    print("$ -  3 Foot to Yard")
    print("$ -  4 Yard to Chain")
    print("$ -  5 Chain to Furlong")
    print("$ -  6 Furlong to Mile")
    print("$ -  7 Mile to League")
    print("$ -  8 Mile to Nautical Mile")
    print("$ -  9 Inch to Yard")
    print("$ - 10 Foot to Mile")
    print("$ - 11 Yard to Foot")
    print("$ - 12 Mile to Foot")
    print("$ - 13 Nautical Mile to Mile")
    print("$ - 14 Inch to Centimeter")
    print("$ - 15 Foot to Meter")
    print("$ - 16 Mile to Kilometer")


def show_area_metric_menu():
    print("\n$ - Area (Metric)")
    print("$ -  1 mm² to cm²")
    print("$ -  2 cm² to dm²")
    print("$ -  3 dm² to m²")
    print("$ -  4 m² to dam²")
    print("$ -  5 dam² to hm²")
    print("$ -  6 hm² to km²")
    print("$ -  7 m² to Are")
    print("$ -  8 Are to Decare")
    print("$ -  9 Decare to Hectare")
    print("$ - 10 m² to Hectare")
    print("$ - 11 cm² to m²")
    print("$ - 12 mm² to m²")
    print("$ - 13 km² to Hectare")
    print("$ - 14 Hectare to m²")
    print("$ - 15 m² to cm²")
    print("$ - 16 km² to m²")


def show_area_imperial_menu():
    print("\n$ - Area (Imperial)")
    print("$ -  1 in² to ft²")
    print("$ -  2 ft² to yd²")
    print("$ -  3 yd² to ch²")
    print("$ -  4 ch² to Acre")
    print("$ -  5 Acre to mi²")
    print("$ -  6 mi² to Section")
    print("$ -  7 Section to Township")
    print("$ -  8 ft² to Acre")
    print("$ -  9 Acre to ft²")
    print("$ - 10 mi² to Acre")
    print("$ - 11 ft² to m²")
    print("$ - 12 Acre to m²")
    print("$ - 13 mi² to km²")
    print("$ - 14 m² to ft²")
    print("$ - 15 m² to Acre")


def show_volume_metric_menu():
    print("\n$ - Volume (Metric)")
    print("$ -  1 mL to cL")
    print("$ -  2 cL to dL")
    print("$ -  3 dL to Liter")
    print("$ -  4 Liter to daL")
    print("$ -  5 daL to hL")
    print("$ -  6 hL to m³")
    print("$ -  7 m³ to km³")
    print("$ -  8 mL to cm³")
    print("$ -  9 Liter to dm³")
    print("$ - 10 mm³ to cm³")
    print("$ - 11 cm³ to Liter")
    print("$ - 12 Liter to m³")
    print("$ - 13 m³ to Liter")
    print("$ - 14 mL to Liter")
    print("$ - 15 Liter to mL")


def show_volume_us_menu():
    print("\n$ - Volume (US)")
    print("$ -  1 Minim to Fluid Dram")
    print("$ -  2 Fluid Dram to Fluid Ounce")
    print("$ -  3 Fluid Ounce to Shot")
    print("$ -  4 Shot to Jigger")
    print("$ -  5 Jigger to Cup")
    print("$ -  6 Cup to Pint")
    print("$ -  7 Pint to Quart")
    print("$ -  8 Quart to Gallon")
    print("$ -  9 Gallon to Barrel")
    print("$ - 10 Fluid Ounce to mL")
    print("$ - 11 Pint to Liter")
    print("$ - 12 Quart to Liter")
    print("$ - 13 Gallon to Liter")
    print("$ - 14 mL to Fluid Ounce")
    print("$ - 15 Liter to Gallon")


def show_volume_uk_menu():
    print("\n$ - Volume (UK)")
    print("$ -  1 Minim to Fluid Dram")
    print("$ -  2 Fluid Dram to Fluid Ounce")
    print("$ -  3 Fluid Ounce to Pint")
    print("$ -  4 Pint to Quart")
    print("$ -  5 Quart to Gallon")
    print("$ -  6 Gallon to Peck")
    print("$ -  7 Peck to Bushel")
    print("$ -  8 Bushel to Barrel")
    print("$ -  9 Fluid Ounce to mL")
    print("$ - 10 Pint to Liter")
    print("$ - 11 Gallon to Liter")
    print("$ - 12 Liter to Gallon")
    print("$ - 13 mL to Fluid Ounce")


def show_weight_metric_menu():
    print("\n$ - Weight (Metric)")
    print("$ -  1 Microgram to Milligram")
    print("$ -  2 Milligram to Centigram")
    print("$ -  3 Centigram to Decigram")
    print("$ -  4 Decigram to Gram")
    print("$ -  5 Gram to Decagram")
    print("$ -  6 Decagram to Hectogram")
    print("$ -  7 Hectogram to Kilogram")
    print("$ -  8 Kilogram to Megagram")
    print("$ -  9 Megagram to Ton")
    print("$ - 10 Ton to Gigagram")
    print("$ - 11 Gram to Kilogram")
    print("$ - 12 Kilogram to Ton")
    print("$ - 13 Milligram to Gram")
    print("$ - 14 Kilogram to Gram")
    print("$ - 15 Ton to Kilogram")
    print("$ - 16 Microgram to Gram")


def show_weight_imperial_menu():
    print("\n$ - Weight (Imperial)")
    print("$ -  1 Grain to Dram")
    print("$ -  2 Dram to Ounce")
    print("$ -  3 Ounce to Pound")
    print("$ -  4 Pound to Stone")
    print("$ -  5 Stone to Quarter")
    print("$ -  6 Quarter to Hundredweight")
    print("$ -  7 Hundredweight to Ton")
    print("$ -  8 Ton to Short Ton")
    print("$ -  9 Ounce to Gram")
    print("$ - 10 Pound to Kilogram")
    print("$ - 11 Stone to Kilogram")
    print("$ - 12 Ton to Kilogram")
    print("$ - 13 Gram to Ounce")
    print("$ - 14 Kilogram to Pound")
    print("$ - 15 Kilogram to Stone")


def show_temperature_menu():
    print("\n$ - Temperature Converter")
    print("$ -  1 °C to °F")
    print("$ -  2 °F to °C")
    print("$ -  3 °C to Kelvin")
    print("$ -  4 Kelvin to °C")
    print("$ -  5 °F to Kelvin")
    print("$ -  6 Kelvin to °F")
    print("$ -  7 °C to Rankine")
    print("$ -  8 Rankine to °C")
    print("$ -  9 °F to Rankine")
    print("$ - 10 Rankine to °F")


def show_speed_menu():
    print("\n$ - Speed Converter")
    print("$ -  1 m/s to km/h")
    print("$ -  2 km/h to m/s")
    print("$ -  3 mph to m/s")
    print("$ -  4 m/s to mph")
    print("$ -  5 Knot to m/s")
    print("$ -  6 m/s to Knot")
    print("$ -  7 ft/s to m/s")
    print("$ -  8 m/s to ft/s")
    print("$ -  9 Mach to m/s")
    print("$ - 10 m/s to Mach")
    print("$ - 11 mph to km/h")
    print("$ - 12 km/h to mph")
    print("$ - 13 Knot to km/h")
    print("$ - 14 km/h to Knot")


def show_pressure_menu():
    print("\n$ - Pressure Converter")
    print("$ -  1 Pa to kPa")
    print("$ -  2 kPa to MPa")
    print("$ -  3 atm to Pa")
    print("$ -  4 PSI to Pa")
    print("$ -  5 bar to Pa")
    print("$ -  6 mmHg to Pa")
    print("$ -  7 inHg to Pa")
    print("$ -  8 Torr to Pa")
    print("$ -  9 kgf/cm² to Pa")
    print("$ - 10 inH₂O to Pa")
    print("$ - 11 Pa to atm")
    print("$ - 12 Pa to PSI")
    print("$ - 13 Pa to bar")
    print("$ - 14 kPa to Pa")
    print("$ - 15 MPa to kPa")
    print("$ - 16 Pa to mmHg")
    print("$ - 17 Pa to inHg")
    print("$ - 18 Pa to Torr")
    print("$ - 19 Pa to kgf/cm²")
    print("$ - 20 Pa to inH₂O")


def show_energy_menu():
    print("\n$ - Energy Converter")
    print("$ -  1 Joule to kJ")
    print("$ -  2 kJ to MJ")
    print("$ -  3 MJ to GJ")
    print("$ -  4 Calorie to Joule")
    print("$ -  5 kcal to Joule")
    print("$ -  6 Wh to Joule")
    print("$ -  7 kWh to Joule")
    print("$ -  8 MWh to Joule")
    print("$ -  9 eV to Joule")
    print("$ - 10 keV to Joule")
    print("$ - 11 MeV to Joule")
    print("$ - 12 GeV to Joule")
    print("$ - 13 BTU to Joule")
    print("$ - 14 ft·lb to Joule")
    print("$ - 15 hp·h to Joule")
    print("$ - 16 Therm to Joule")
    print("$ - 17 Joule to Calorie")
    print("$ - 18 Joule to kWh")
    print("$ - 19 Joule to eV")
    print("$ - 20 Joule to BTU")


def show_power_menu():
    print("\n$ - Power Converter")
    print("$ -  1 Watt to kW")
    print("$ -  2 kW to MW")
    print("$ -  3 MW to GW")
    print("$ -  4 GW to TW")
    print("$ -  5 hp to Watt")
    print("$ -  6 BTU/h to Watt")
    print("$ -  7 kcal/h to Watt")
    print("$ -  8 ft·lb/s to Watt")
    print("$ -  9 Watt to hp")
    print("$ - 10 Watt to BTU/h")
    print("$ - 11 kW to hp")
    print("$ - 12 hp to kW")


def show_frequency_menu():
    print("\n$ - Frequency Converter")
    print("$ -  1 Hz to kHz")
    print("$ -  2 kHz to MHz")
    print("$ -  3 MHz to GHz")
    print("$ -  4 GHz to THz")
    print("$ -  5 RPM to Hz")
    print("$ -  6 Hz to RPM")
    print("$ -  7 kHz to Hz")
    print("$ -  8 MHz to Hz")
    print("$ -  9 GHz to Hz")
    print("$ - 10 THz to Hz")


def show_angle_menu():
    print("\n$ - Angle Converter")
    print("$ -  1 Degree to Radian")
    print("$ -  2 Radian to Degree")
    print("$ -  3 Degree to Gradian")
    print("$ -  4 Gradian to Degree")
    print("$ -  5 Degree to Revolution")
    print("$ -  6 Revolution to Degree")
    print("$ -  7 Degree to Arcminute")
    print("$ -  8 Arcminute to Degree")
    print("$ -  9 Arcminute to Arcsecond")
    print("$ - 10 Arcsecond to Arcminute")
    print("$ - 11 Radian to Milliradian")
    print("$ - 12 Milliradian to Radian")


def show_density_menu():
    print("\n$ - Density Converter")
    print("$ -  1 kg/m³ to g/cm³")
    print("$ -  2 g/cm³ to kg/m³")
    print("$ -  3 g/cm³ to g/mL")
    print("$ -  4 g/cm³ to kg/L")
    print("$ -  5 lb/ft³ to kg/m³")
    print("$ -  6 kg/m³ to lb/ft³")
    print("$ -  7 lb/in³ to kg/m³")
    print("$ -  8 oz/in³ to kg/m³")
    print("$ -  9 g/mL to g/cm³")
    print("$ - 10 kg/L to g/cm³")


# =========================================== MENU DISPATCHER
def show_menu(converter_type):
    menus = {
        "1": show_time_menu,
        "2": show_data_binary_menu,
        "3": show_data_decimal_menu,
        "4": show_length_metric_menu,
        "5": show_length_imperial_menu,
        "6": show_area_metric_menu,
        "7": show_area_imperial_menu,
        "8": show_volume_metric_menu,
        "9": show_volume_us_menu,
        "10": show_volume_uk_menu,
        "11": show_weight_metric_menu,
        "12": show_weight_imperial_menu,
        "13": show_temperature_menu,
        "14": show_speed_menu,
        "15": show_pressure_menu,
        "16": show_energy_menu,
        "17": show_power_menu,
        "18": show_frequency_menu,
        "19": show_angle_menu,
        "20": show_density_menu,
    }
    menus.get(converter_type, lambda: print("$ - Invalid choice!"))()


# =========================================== MAIN PROGRAM
def main():
    while True:
        show_main_menu()
        converter_type = input("$ - Enter your choice (0-20): ")

        if converter_type == "0":
            print("\n$ - Goodbye! Thanks for using UCP.")
            break

        if converter_type not in MENU_OPTIONS:
            print("$ - Invalid choice! Please try again.")
            continue

        show_menu(converter_type)
        choice = input("$ - Choose conversion: ")

        try:
            value = float(input("$ - Enter value to convert: "))
            result = convert(converter_type, choice, value)

            if result is not None:
                print(f"\n$ - Result: {value} → {result}")
                print("=" * 60)
            else:
                print("$ - Invalid conversion choice!")
        except ValueError:
            print("$ - Please enter a valid number!")
        except Exception as e:
            print(f"$ - Error: {e}")


# =========================================== RUN
if __name__ == "__main__":
    main()
