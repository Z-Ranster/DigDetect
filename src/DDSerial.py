import serial
import serial.tools.list_ports
import kinematics

# TODO: Implement hash checking on the serial string to avoid the crashing that currently happens

# Serial Variables
baudRate = 9600
selected_SerialPort = 'COM4'
serialPorts = []
ser = serial.Serial()


def readSerial():
    if ser.isOpen():
        # Read a line of serial input
        line = ser.readline().strip().decode()
        # Do something with the input
        print(line)
        # Split the input into a list
        currentData = line.split(",")
        if len(currentData) == 10:
            a = float(currentData[1])
            b = float(currentData[2])
            c = float(currentData[3])
            data = [0, a, b, c]
            kinematics.calculateAngle(data)


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
