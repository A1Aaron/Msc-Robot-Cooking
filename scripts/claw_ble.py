import bluetooth
import sys

# Used to scan and print nearby devices
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print ("Found %d devices" % len(nearby_devices))
for addr, name in nearby_devices :
    print("    %s - %s" %(addr, name))
  
# Bluetooth address assigned to claw 
# **Ensure the device is connected to the pc via the native bluetooth settings and update the asigned MAC address acordingly** 
addr = "E8:9F:6D:27:74:76"

# Connect to the specified address
service_matches = bluetooth.find_service(address=addr)

# If connection is not made
if len(service_matches) == 0:
    print("Could not connect to the ESP32-Claw")
    sys.exit(0)

# If connection is made the devices begins to setup communciation
first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]
print("Connecting to \"{}\" on {}".format(name, host))

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

print("Connected to ESP32-Claw. Type '1' to OPEN Claw or '0' to CLOSE")
while True:
    data = input()
    if not data:
        break
    sock.send(data)

sock.close()
