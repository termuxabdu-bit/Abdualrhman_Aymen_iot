import json
import time
import random
import datetime


class WeatherStation:

    def __init__(self, station_id):
        self.id = station_id
        self.history = []

    def take_reading(self):
        data = {
            "temp": round(random.uniform(10, 40), 1),
            "humidity": random.randint(40, 90),
            "time": datetime.datetime.now().strftime("%H:%M:%S")
        }

        self.history.append(data)
        print(f"[{self.id}] Recorded: {data}")

    def save_to_cloud(self):
        with open(f"{self.id}_data.json", "w") as f:
            json.dump(self.history, f, indent=4)

        print("Data uploaded to JSON successfully!")


w1 = WeatherStation("Sanaa")

for i in range(3):
    w1.take_reading()
    time.sleep(1)

w1.save_to_cloud()