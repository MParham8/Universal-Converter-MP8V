# 🔄 Universal Converter MP8V

**Universal Converter MP8V (UCMP8V)** is a pure-Python, modular command-line unit converter designed to be accurate, fast, and easy to extend.

The project supports **20 conversion categories** across Metric, Imperial, US, and UK measurement systems. The current architecture separates user interaction, conversion logic, and conversion data so that the application is easier to maintain and expand.

---

## ✨ Features

- 🚀 Interactive command-line interface
- 🔢 20 conversion categories
- 📚 Hundreds of supported units and conversion options
- ⚡ Fast, data-driven conversion engine
- 🌍 Metric, Imperial, US, and UK systems
- 💾 Binary (1024-based) and Decimal (1000-based) data conversion
- 🔄 Cross-system conversions
- 🧩 Modular architecture with shared metadata
- 🛡️ Improved numeric/input validation
- 🐍 Pure Python — no external dependencies

---

## 📌 Supported Converters

| # | Category |
|---:|---|
| 1 | ⏱️ Time |
| 2 | 💾 Data Storage (Binary) |
| 3 | 💾 Data Storage (Decimal) |
| 4 | 📏 Length (Metric) |
| 5 | 📏 Length (Imperial) |
| 6 | 📐 Area (Metric) |
| 7 | 📐 Area (Imperial) |
| 8 | 🧪 Volume (Metric) |
| 9 | 🥤 Volume (US) |
| 10 | 🥛 Volume (UK) |
| 11 | ⚖️ Weight (Metric) |
| 12 | ⚖️ Weight (Imperial) |
| 13 | 🌡️ Temperature |
| 14 | 🚗 Speed |
| 15 | 🧯 Pressure |
| 16 | ⚡ Energy |
| 17 | 🔋 Power |
| 18 | 📡 Frequency |
| 19 | 📐 Angle |
| 20 | 🧪 Density |

---

## 📂 Project Structure

```text
Universal-Converter-MP8V/
│
├── INOUT.py
│   └── CLI, menus, input validation, and output formatting
│
├── Logic.py
│   └── Data-driven conversion engine
│
├── data.py
│   └── Unit definitions, constants, labels, and converter metadata
│
└── README.md
```

---

## 🧠 Architecture

### 🖥️ `INOUT.py`

Handles the command-line user experience:

- Main menu and converter selection
- Conversion option selection
- Numeric input validation
- Error handling for invalid selections
- Result formatting and display

Menus are generated from shared metadata instead of duplicating large menu definitions.

### ⚙️ `Logic.py`

Contains the central conversion engine.

The converter uses shared unit tables and conversion metadata instead of maintaining a large collection of nearly identical conversion functions. This reduces duplicated code and makes new conversion options easier to add.

For linear units, conversions are calculated from their common base-unit factors. Temperature remains a dedicated special case because Celsius, Fahrenheit, Kelvin, and Rankine require affine transformations rather than simple multiplication.

### 📚 `data.py`

Contains the application's conversion data and metadata:

- Unit/base-unit factors
- Display labels
- Cross-system constants
- Converter categories
- Conversion option metadata
- CLI menu metadata

Keeping data separate from the calculation engine makes the project easier to audit and extend.

---

## 🐛 Bug Fixes & Accuracy Improvements

The current refactor also fixes several issues found during review, including:

- Corrected several Imperial and US/UK volume factors
- Improved nautical-mile precision
- Corrected common cross-system area and volume constants
- Normalized unit naming between data and conversion metadata
- Removed duplicated conversion logic that could drift between categories
- Improved handling of invalid menu choices and numeric input
- Preserved the existing 20-category CLI workflow

The conversion engine was also smoke-tested across representative time, data, length, area, volume, weight, temperature, speed, frequency, angle, and density conversions.

---

## ▶️ Run

Requirements:

- Python 3.x
- No third-party packages required

Run the application with:

```bash
python INOUT.py
```

---

## 💻 Example

```text
Welcome to Universal Converter MP8V

Select a converter:

1. Time
2. Data Storage (Binary)
3. Data Storage (Decimal)
4. Length (Metric)
...
20. Density

Enter your choice:
```

Choose a category, select a conversion, enter a numeric value, and the application will display the converted result.

---

## 🛠️ Technologies

- Python 3
- Standard library only

---

## 🎯 Project Goals

Universal Converter MP8V aims to provide:

- ✅ Accurate and consistent conversion formulas
- 🧹 Clean and maintainable code
- 🧩 A data-driven architecture
- ➕ Easy addition of new units and categories
- 🛡️ Robust input handling
- 🚀 Fast command-line operation

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature or fix branch
3. Make and test your changes
4. Submit a pull request

For conversion changes, please verify both the numerical result and the displayed unit label.

---

## 📄 License

This project is open source.

---

## ⭐ Support

If you find Universal Converter MP8V useful, consider giving the project a ⭐ on GitHub!
