"""Interactive CLI for Universal Converter MP8V."""

from data import MENU_OPTIONS, MENU_LABELS
from Logic import convert, format_result, get_conversion_pair, get_unit_label

WIDTH = 60


def show_main_menu():
    print("\n" + "=" * WIDTH)
    print("$ - Hello! Welcome to UCMP8")
    print("=" * WIDTH)
    for number, name in MENU_OPTIONS.items():
        suffix = " (Binary - 1024)" if number == "2" else " (Decimal - 1000)" if number == "3" else ""
        print(f"$ - {int(number):2} {name}{suffix}")
    print("$ -  0 Exit")
    print("=" * WIDTH)


def show_menu(converter_type):
    labels = MENU_LABELS.get(str(converter_type))
    if not labels:
        print("$ - Invalid choice!")
        return
    print(f"\n$ - {MENU_OPTIONS[str(converter_type)]} Converter")
    for index, label in enumerate(labels, 1):
        print(f"$ - {index:2} {label}")


def _read_value():
    while True:
        try:
            return float(input("$ - Enter value to convert: ").strip())
        except ValueError:
            print("$ - Please enter a valid number!")


def main():
    print("$ - let's start!")
    while True:
        show_main_menu()
        converter_type = input("$ - Enter your choice (0-20): ").strip()
        if converter_type == "0":
            print("\n$ - Goodbye! Thanks for using UCMP8.")
            return
        if converter_type not in MENU_OPTIONS:
            print("$ - Invalid choice! Please try again.")
            continue

        show_menu(converter_type)
        choice = input("$ - Choose conversion: ").strip()
        pair = get_conversion_pair(converter_type, choice)
        if pair is None:
            print("$ - Invalid conversion choice!")
            continue

        value = _read_value()
        result = convert(converter_type, choice, value)
        if result is None:
            print("$ - Conversion failed. Please check your choice and try again.")
            continue

        from_unit, to_unit = pair
        print(f"\n$ - Result: {format_result(value)} {get_unit_label(converter_type, from_unit)} → "
              f"{format_result(result)} {get_unit_label(converter_type, to_unit)}")
        print("=" * WIDTH)


if __name__ == "__main__":
    main()
