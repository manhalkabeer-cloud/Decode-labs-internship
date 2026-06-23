import random
import pandas as pd
from datetime import datetime

# Generate random sensor values
temperature = round(random.uniform(20, 40), 1)
humidity = round(random.uniform(30, 90), 1)
motion = random.choice(["Detected", "Not Detected"])

# Automation rules
fan = "ON" if temperature > 35 else "OFF"
dehumidifier = "ON" if humidity > 75 else "OFF"
alarm = "ON" if motion == "Detected" else "OFF"

# Save data
data = {
    "Time": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "Temperature": [temperature],
    "Humidity": [humidity],
    "Motion": [motion],
    "Fan": [fan],
    "Dehumidifier": [dehumidifier],
    "Alarm": [alarm]
}

df = pd.DataFrame(data)
df.to_csv("sensor_data.csv", index=False)

print("========== Smart Environment Monitoring ==========")
print(df.to_string(index=False))
print("\nData saved successfully.")