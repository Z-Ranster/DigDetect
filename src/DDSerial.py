import serial
import serial.tools.list_ports

# The checking is causing speed issues.  Need to find a better way to do this.

# Serial Variables
baudRate = 9600
selected_SerialPort = 'COM4'
serialPorts = []
serArduino = serial.Serial()
serGPS = serial.Serial()


def readSerial():
    if serArduino.isOpen():
        data_ready = False
        good_data_count = 0
        while not data_ready:
            if serArduino.in_waiting > 0:
                line = serArduino.readline().decode().strip()
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
    # Print an empty line
    print()


def startSerial(portUse):
    print("Connecting to Serial Port: " + selected_SerialPort)
    if portUse == "Arduino":
        try:
            serArduino.port = selected_SerialPort
            serArduino.baudrate = baudRate
            serArduino.timeout = 1
            serArduino.open()
            print("Arduino - Connected!")
        except serial.SerialException as e:
            print("Error opening serial port: {e}")
        except Exception as e:
            print("Unknown error opening serial port: {e}")
    elif portUse == "GPS":
        try:
            # serGPS.port = selected_SerialPort
            # serGPS.baudrate = baudRate
            # serGPS.timeout = 1
            # serGPS.open()
            # print("GPS - Connected!")
            l = 0
        except serial.SerialException as e:
            print("Error opening serial port: {e}")
        except Exception as e:
            print("Unknown error opening serial port: {e}")
    print()


def closeSerial(portUse):
    if portUse == "Arduino":
        try:
            serArduino.close()
            print("Arduino - Disconnected!")
        except serial.SerialException as e:
            print("Error opening serial port: {e}")
        except Exception as e:
            print("Unknown error opening serial port: {e}")
    elif portUse == "GPS":
        try:
            serGPS.close()
            print("GPS - Disconnected!")
        except serial.SerialException as e:
            print("Error opening serial port: {e}")
        except Exception as e:
            print("Unknown error opening serial port: {e}")
