import time 
from wifi_connect import connect_to_wifi
from moon_device_status import moon_device_status
from moon_control import moon_device_control, moon_servo_control
from machine import Pin
import urequests



# User-defined details
ssid = "PandoraBox"
wifi_password = "atithinarayan"
user_token = "19D043F5-D69B-45A2-96CD-5E1138684B26"
device_token = "36B42BEC-4330-4A96-95F2-A14B9F83AB91"
temp_component_id = 1441
fan_component_id = 1442
led_pin = 12 # GPIO Pin for LED (D1)

door_servo_pin = 2
lock_servo_pin = 4

def main():
  try:
    # Step 1: Connect to WiFi
    connect_to_wifi(ssid, wifi_password, device_token)

    # Step 2: Monitor and update LED state
    valuesToggle = moon_device_status(toggle_component_id, device_token, user_token)
    previous_led_state = None
    while True:
      # Step 2: Check toggle component status
      time.sleep(1) # Fetch state every 5 seconds
      values = moon_device_status(component_id, device_token, user_token)
      toggle_status = str(valuesToggle[0])
      print(f"Toggle Status: {toggle_status}")
      if toggle_status == "True":
        print("Unlocking the door...")
        moon_servo_control(lock_servo_pin, 90) # Unlock
        time.sleep(1)
        print("Opening the door...")
        moon_servo_control(door_servo_pin, 0) # Door open
        time.sleep(2)
      else:
        print("Closing the door...") 
        moon_servo_control(door_servo_pin, 70) # Door closed
        time.sleep(1)
        print("l=Locking the door...")
        moon_servo_control(lock_servo_pin, 20) # Lock
        time.sleep(1)
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()