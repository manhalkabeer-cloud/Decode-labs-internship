import random
from datetime import datetime

# -------------------------------
# IoT Automation Logic Simulation
# -------------------------------

# Generate random sensor values
temperature = round(random.uniform(20, 40), 1)
humidity = round(random.uniform(30, 90), 1)
motion = random.choice(["Detected", "Not Detected"])

# Display current time
print("=" * 50)
print("        IoT AUTOMATION SYSTEM")
print("=" * 50)
print("Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
print()

# Display sensor readings
print("Sensor Readings")
print("-" * 50)
print(f"Temperature : {temperature} °C")
print(f"Humidity    : {humidity} %")
print(f"Motion      : {motion}")
print()

# Automation Logic
print("Automation Status")
print("-" * 50)

# Temperature Rule
if temperature > 35:
    print("Fan               : ON")
else:
    print("Fan               : OFF")

# Humidity Rule
if humidity > 75:
    print("Dehumidifier      : ON")
else:
    print("Dehumidifier      : OFF")

# Motion Rule
if motion == "Detected":
    print("Security Alarm    : ON")
else:
    print("Security Alarm    : OFF")

print("-" * 50)
print("Automation process completed successfully.")
print("=" * 50)