# 🔄 UCP - Universal Converter Pro

A powerful and modular **command-line unit converter** written in Python.

UCP (Universal Converter Pro) helps users convert values between different measurement systems with support for multiple categories including time, data, length, area, volume, temperature, energy, and more.

---

## 📸 Screenshot
<img width="2803" height="1130" alt="Screenshot 2026-08-06 215446" src="https://github.com/user-attachments/assets/405b4222-4264-4624-a27a-3298a232bb0a" />


---

## ✨ Features

* ✅ 20 different converter categories
* ✅ Hundreds of supported units
* ✅ Metric, Imperial, US, and UK measurement systems
* ✅ Binary (1024-based) and Decimal (1000-based) data conversion
* ✅ Cross-system conversions
* ✅ Interactive CLI interface
* ✅ Modular project architecture
* ✅ Fast and lightweight (Python standard library only)

---

## 📂 Project Structure

```text
UCP/
│
├── INOUT.py
│   └── User interface, menus, input/output handling
│
├── Logic.py
│   └── Conversion algorithms and calculation engine
│
└── data.py
    └── Conversion constants, unit mappings, and metadata
```

---

# 🧩 Architecture

## 🖥 INOUT.py

Responsible for the user interaction layer.

Features:

* Main menu system
* Converter category selection
* Sub-menu navigation
* User input handling
* Displaying conversion results

---

## 🧠 Logic.py

The core conversion engine of UCP.

Responsible for:

* Performing calculations
* Managing conversion functions
* Handling different unit systems
* Returning converted values

Includes conversion logic for:

* Time
* Data Storage
* Length
* Area
* Volume
* Weight
* Temperature
* Speed
* Pressure
* Energy
* Power
* Frequency
* Angle
* Density

---

## 📚 data.py

Contains all conversion data and metadata.

Includes:

* Unit conversion constants
* Unit labels
* Conversion mappings
* Reference values
* Menu configuration

---

# 🔢 Supported Converters

| Category                   | Supported |
| -------------------------- | --------- |
| ⏱ Time                     | ✅         |
| 💾 Data (Binary / Decimal) | ✅         |
| 📏 Length                  | ✅         |
| 📐 Area                    | ✅         |
| 🧪 Volume                  | ✅         |
| ⚖️ Weight                  | ✅         |
| 🌡 Temperature             | ✅         |
| 🚗 Speed                   | ✅         |
| pressure                   | ✅         |
| ⚡ Energy                   | ✅         |
| 🔋 Power                   | ✅         |
| 📡 Frequency               | ✅         |
| 📐 Angle                   | ✅         |
| 🧪 Density                 | ✅         |

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/UCP.git
```

Navigate to the project folder:

```bash
cd UCP
```

---

# ▶️ Usage

Run the program:

```bash
python INOUT.py
```

Then select:

1. Converter category
2. Conversion type
3. Enter the value to convert

The program will display the converted result.

---

# 💻 Example

```text
$ - Hello! Welcome to UCP (Universal Converter Pro)

$ - Which converter do you want?

1 Time
2 Data (Binary - 1024)
3 Data (Decimal - 1000)
...

$ - Enter your choice:
1

$ - Choose conversion:
1

$ - Enter value to convert:
120

$ - Result:
120 → 2 minutes
```

---

# 🛠 Technologies

* Python 3
* Standard Python Library

No external dependencies required.

---

# 🎯 Project Goals

The goal of UCP is to provide a simple, accurate, and extensible unit conversion tool while maintaining a clean modular structure.

---

# 📌 Future Improvements

Possible future updates:

* GUI version
* Web API support
* More conversion categories
* Unit search system
* History of conversions
* Improved user interface

---

# 📄 License

This project is licensed under the MIT License.
