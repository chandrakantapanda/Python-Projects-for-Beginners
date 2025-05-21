
# 🌦️ Multi-Location Weather Dashboard (Python)

This Python script fetches **real-time weather** for multiple cities using the free [Open-Meteo API](https://open-meteo.com/), displaying temperature, wind speed, and direction in a terminal dashboard.

## 🛠️ Features

- 🔁 Automatically updates weather at your chosen interval
- 🌍 Supports any number of locations (just add latitude & longitude)
- 🔌 No API key required
- 💻 Simple command-line interface

## 📸 Sample Output

```
📊 Weather Dashboard (Live)
-----------------------------------
📍 Salepur (20.3869, 86.1318)
🌡️ Temp: 33.1°C
💨 Wind: 10.2 km/h
🧭 Dir: 170°

📍 Cuttack (20.4625, 85.8828)
🌡️ Temp: 34.4°C
💨 Wind: 11.7 km/h
🧭 Dir: 150°
-----------------------------------
```

## 🚀 How to Run

1. **Clone or Download** the script:

```bash
git clone https://github.com/your-username/weather-dashboard
cd weather-dashboard
```

2. **Install dependencies** (only `requests` is required):

```bash
pip install requests
```

3. **Run the script**:

```bash
python weather_dashboard.py
```

4. Enter the update interval (e.g., `5` for every 5 minutes)

## 🧾 Customize Your Locations

Edit the `locations` list in the script:

```python
locations = [
    {"name": "Your City", "lat": XX.XXXX, "lon": YY.YYYY}
]
```

Use [Google Maps](https://www.google.com/maps) or [latlong.net](https://www.latlong.net/) to find coordinates.

## 📚 Dependencies

- Python 3.x
- [requests](https://pypi.org/project/requests/)

## ✅ API Used

- [Open-Meteo](https://open-meteo.com/): A free, no-auth weather API with real-time data.

## 📌 To-Do (Suggestions)

- [ ] Save output to CSV
- [ ] Add color formatting
- [ ] Build a GUI version with Tkinter or PyQt
- [ ] Add hourly/weekly forecast

## 🧑‍💻 Author

Made with ❤️ by `CodeWithPython`
