import requests
import time

# 📌 Add your favorite locations here
locations = [
    {"name": "Salepur", "lat": 20.3869, "lon": 86.1318},
    {"name": "Cuttack", "lat": 20.4625, "lon": 85.8828},
    {"name": "Bhubaneswar", "lat": 20.2961, "lon": 85.8245},
    {"name": "Delhi", "lat": 28.6139, "lon": 77.2090}
]

def get_weather(name, lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )
    try:
        response = requests.get(url)
        data = response.json()
        if "current_weather" in data:
            weather = data["current_weather"]
            print(f"\n📍 {name} ({lat}, {lon})")
            print(f"🌡️ Temp: {weather['temperature']}°C")
            print(f"💨 Wind: {weather['windspeed']} km/h")
            print(f"🧭 Dir: {weather['winddirection']}°")
        else:
            print(f"⚠️ No weather data for {name}")
    except Exception as e:
        print(f"❌ Error for {name}: {e}")

if __name__ == "__main__":
    interval = int(input("⏱️ Enter update interval (minutes): "))

    try:
        while True:
            print("\n📊 Weather Dashboard (Live)")
            print("-" * 35)
            for location in locations:
                get_weather(location["name"], location["lat"], location["lon"])
            print("-" * 35)
            time.sleep(interval * 60)
    except KeyboardInterrupt:
        print("\n🛑 Dashboard stopped.")
