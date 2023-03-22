import serial
import serial.tools.list_ports
import kinematics

# The checking is causing speed issues.  Need to find a better way to do this.

# Serial Variables
baudRate = 9600
selected_SerialPort = 'COM4'
serialPorts = []
ser = serial.Serial()


def readSerial():
    if ser.isOpen():
        data_ready = False
        good_data_count = 0
        while not data_ready:
            if ser.in_waiting > 0:
                line = ser.readline().decode().strip()
                current_data = line.split(",")
                if len(current_data) == 11 and "DDT" in current_data[0]:
                    good_data_count += 1
                    if good_data_count >= 3:  # Wait for 3 good data entries before processing
                        data_ready = True
                        return current_data
                else:
                    good_data_count = 0  # Reset the good data count if bad data is received


def updateSerialPorts():
    print("Updating Serial Ports...")
    # Clear the list
    serialPorts.clear()
    # Read and Print Serial Ports
    ports = serial.tools.list_ports.comports()
    for port in ports:
        serialPorts.append(port.device)
        print(str(port))


def startSerial():
    print("Connecting to Serial Port: " + selected_SerialPort)
    try:
        ser.port = selected_SerialPort
        ser.baudrate = baudRate
        ser.timeout = 1
        ser.open()
        print("Connected!")
    except serial.SerialException as e:
        print("Error opening serial port: {e}")
    except Exception as e:
        print("Unknown error opening serial port: {e}")


def closeSerial():
    try:
        ser.close()
        print("Disconnected!")
    except serial.SerialException as e:
        print("Error opening serial port: {e}")
    except Exception as e:
        print("Unknown error opening serial port: {e}")
