# 🔄 Universal Converter Professional (UCP)

<img width="2803" height="1130" alt="Screenshot 2026-08-06 215446" src="https://github.com/user-attachments/assets/1d6cf476-fbd2-42d2-9372-5e34aebd9546" />


**Universal Converter Professional (UCP)** is a powerful and modular command-line unit converter built with Python.

UCP provides a complete conversion system for different measurement categories, supporting Metric, Imperial, US, and UK units with a clean and expandable architecture.

---

## ✨ Features

* 🚀 Interactive command-line interface
* 🔢 20+ conversion categories
* 📚 Hundreds of supported units
* ⚡ Fast and accurate calculations
* 🌍 Metric, Imperial, US, and UK systems
* 💾 Binary (1024-based) and Decimal (1000-based) data conversion
* 🔄 Cross-system unit conversion
* 🧩 Modular project architecture
* 🐍 Pure Python (No external dependencies)

---

# 📌 Supported Converters

| #  | Category                  |
| -- | ------------------------- |
| 1  | ⏱ Time                    |
| 2  | 💾 Data Storage (Binary)  |
| 3  | 💾 Data Storage (Decimal) |
| 4  | 📏 Length (Metric)        |
| 5  | 📏 Length (Imperial)      |
| 6  | 📐 Area (Metric)          |
| 7  | 📐 Area (Imperial)        |
| 8  | 🧪 Volume (Metric)        |
| 9  | 🥤 Volume (US)            |
| 10 | 🥛 Volume (UK)            |
| 11 | ⚖️ Weight (Metric)        |
| 12 | ⚖️ Weight (Imperial)      |
| 13 | 🌡 Temperature            |
| 14 | 🚗 Speed                  |
| 15 | pressure                  |
| 16 | ⚡ Energy                  |
| 17 | 🔋 Power                  |
| 18 | 📡 Frequency              |
| 19 | 📐 Angle                  |
| 20 | 🧪 Density                |

---

# 📂 Project Structure

```text
Universal-Converter-Professional---UCP/

│
├── INOUT.py
│   └── User interface, menus, and input/output handling
│
├── Logic.py
│   └── Conversion functions and calculation engine
│
├── data.py
│   └── Units, constants, labels, and metadata
│
└── README.md
```

---

# 🧠 Architecture

## 🖥 INOUT.py

Responsible for the user experience:

* Main menu system
* Converter selection
* User input handling
* Result formatting
* Display management

---

## ⚙️ Logic.py

The core conversion engine.

Handles:

* Conversion calculations
* Unit mapping
* Conversion selection
* Result generation

All converter functions are separated by category for better maintainability.

---

## 📚 data.py

Contains all conversion data:

* Unit definitions
* Conversion factors
* Unit labels
* Menu mappings
* Metadata

This separation makes adding new units simple and organized.

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/MParham8/Universal-Converter-Professional---UCP.git
```

Navigate into the project directory:

```bash
cd Universal-Converter-Professional---UCP
```

---

# ▶️ Run

Start the application:

```bash
python INOUT.py
```

---

# 💻 Example

```text
Welcome to UCP (Universal Converter Professional)

Select a converter:

1. Time
2. Data Binary
3. Data Decimal
4. Length Metric
...

Enter your choice:
```

Select your category, choose the conversion type, enter your value, and receive the converted result instantly.

---

# 🛠 Technologies

* Python 3
* Standard Python Library

---

# 🎯 Project Goals

The main goal of UCP is to create a reliable, expandable, and user-friendly conversion tool with:

* Clean code organization
* Accurate conversion formulas
* Easy future development
* Support for many measurement systems

---

# 🔮 Future Improvements

Planned improvements:

* 🖥 Graphical User Interface (GUI)
* 🌐 Web API version
* 📱 Mobile application
* 📜 Conversion history
* 🔍 Unit search system
* 🧪 Automated testing
* ➕ Additional scientific conversions

---

# 🤝 Contributing

Contributions are welcome!

If you have ideas, improvements, or bug fixes:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!
