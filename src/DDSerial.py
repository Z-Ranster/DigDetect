import serial
import serial.tools.list_ports

# Serial Variables
baudRate = 9600
selected_SerialPort = ''
ser = serial.Serial()

def readSerial(model):
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
                deg = [0,a,b,c]
                model.angles = np.deg2rad(deg)
                efLocation = model.fk.solve(np.deg2rad(deg))
                print(efLocation)

def startSerial():
    try:
        index = self.lbSerialPorts.curselection()
        selected_SerialPort = self.lbSerialPorts.get(index)
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