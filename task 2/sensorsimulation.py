import random
import pandas as pd
from datetime import datetime

# Generate random sensor values
temperature = round(random.uniform(20, 40), 2)
humidity = round(random.uniform(40, 90), 2)
motion = random.choice(["Detected", "Not Detected"])

# Get current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create a table
sensor_data = {
    "Time": [current_time],
    "Temperature (°C)": [temperature],
    "Humidity (%)": [humidity],
    "Motion": [motion]
}

# Convert to DataFrame
df = pd.DataFrame(sensor_data)

# Save data to CSV
df.to_csv("sensor_data.csv", index=False)

# Display output
print("\n========== IoT Sensor Simulation ==========")
print(f"Time         : {current_time}")
print(f"Temperature  : {temperature} °C")
print(f"Humidity     : {humidity} %")
print(f"Motion       : {motion}")
print("===========================================")
print("Sensor data has been saved to 'sensor_data.csv'")