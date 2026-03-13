import network
import urequests
import ujson
import time
import machine
import esp32

# Wi-Fi Configurations
SSID = "SSID"
PASSWORD = "PASSWORD"

# Your Oracle 26ai database endpoint
ORDS_URL = "URL"

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        wlan.connect(SSID, PASSWORD)
        
        # 15-second timeout
        for _ in range(15):
            if wlan.isconnected():
                break
            time.sleep(1)
            print('.', end='')
            
    if wlan.isconnected():
        print('\nConnected! IP:', wlan.ifconfig()[0])
        return True
    else:
        print('\nWi-Fi connection failed.')
        return False

def send_data():
    while True:
        if connect_wifi():
            try:
                # Reading the internal ESP32-S3 temperature
                # (esp32.raw_temperature() returns Fahrenheit; we convert to Celsius)
                temp_f = esp32.raw_temperature()
                temp_c = (temp_f - 32) * 5 / 9
                
                # JSON Payload matching your database columns (SENSOR_NAME, READING, UNIT)
                payload = {
                    "SENSOR_NAME": "ESP32-S3-Wellington",
                    "READING": round(temp_c, 2),
                    "UNIT": "Celsius"
                }
                
                print("\nSending to Oracle:", payload)
                
                # Perform the POST request
                response = urequests.post(
                    ORDS_URL, 
                    data=ujson.dumps(payload),
                    headers={'Content-Type': 'application/json'}
                )
                
                print("Status Code:", response.status_code)
                print("Response:", response.text)
                response.close()
                
            except Exception as e:
                print("Error sending data:", e)
        
        # Wait 60 seconds for the next reading
        print("Waiting 60 seconds...")
        time.sleep(60)

# Start the program
send_data()