import serial
import serial.tools.list_ports

# List available ports
ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"Found port: {port.device}")

ser = serial.Serial('COM55', baudrate=9600, timeout=1)
try:
    pass
except serial.SerialException as e:
    print(f"Error interacting with port: {str(e)}")
finally:
    ser.close()
