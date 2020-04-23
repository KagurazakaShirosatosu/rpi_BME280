import smbus2
import bme280
import json
import time
import requests

print("System Start.")
port = 1
address = 0x77
bus = smbus2.SMBus(port)

while True:

    calibration_params = bme280.load_calibration_params(bus, address)
    sensor_data = bme280.sample(bus, address, calibration_params)
    timestamp = time.time()
    data = {'id': int(timestamp), 'temperature': sensor_data.temperature, 'pressure': sensor_data.pressure, 'humidity': sensor_data.humidity}

    json_str = json.dumps(data)
    print(json_str)

    httpRequest = requests.put(YOUR_ADDR, data=json_str)
    print(httpRequest.status_code, httpRequest.content)

    time.sleep(int(60))