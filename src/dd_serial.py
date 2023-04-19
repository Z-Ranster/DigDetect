# Import necessary libraries
import serial
import serial.tools.list_ports


class SerialConnection:
    """
    This class provides methods for handling serial connection with Arduino and GPS
    """

    def __init__(self, baud_rate=9600):
        """
        Constructor for SerialConnection class

        :param baud_rate: integer, baud rate for serial connection, default is 9600
        """
        self.baud_rate = baud_rate
        self.serial_ports = []
        self.ser_arduino = serial.Serial()
        self.ser_gps = serial.Serial()
        self.selected_SerialPort = 'COM4'

    def read_arduino_data(self):
        """
        Reads data from Arduino serial port and returns it as a list

        :return: list of current data from Arduino, or None if no data is received
        """
        if self.ser_arduino.isOpen():
            try:
                line = self.ser_arduino.readline().decode().strip()
                current_data = line.split(",")
                if len(current_data) == 5 and "DDT" in current_data[0]:
                    return current_data
            except Exception:
                pass

    def read_gps_data(self):
        """
        Reads data from GPS serial port and returns it as a string

        :return: string of current data from GPS, or None if no data is received
        """
        if self.ser_gps.isOpen():
            line = self.ser_gps.readline().decode('utf-8')
            return line

    def update_serial_ports(self):
        """
        Refreshes the list of available serial ports and returns it

        :return: list of available serial ports
        """
        self.serial_ports.clear()
        ports = serial.tools.list_ports.comports()
        return ports

    def connect_serial(self, port_use):
        """
        Opens a serial connection to a selected port

        :param port_use: string, specifies whether the connection is for 'Arduino' or 'GPS'
        :return: string, message indicating success or error
        """
        if port_use == "Arduino":
            try:
                self.ser_arduino.port = self.selected_SerialPort
                self.ser_arduino.baudrate = self.baud_rate
                self.ser_arduino.timeout = 1
                self.ser_arduino.open()
                return "Arduino - Connected!"
            except serial.SerialException as e:
                return str(e)
        elif port_use == "GPS":
            try:
                self.ser_gps.port = self.selected_SerialPort
                self.ser_gps.baudrate = self.baud_rate
                self.ser_gps.timeout = 1
                self.ser_gps.open()
                return "GPS - Connected!"
            except serial.SerialException as e:
                return str(e)

    def close_serial(self, port_use):
        """
        Closes a serial connection to a selected port

        :param port_use: string, specifies whether the connection is for 'Arduino' or 'GPS'
        :return: string, message indicating success or error
        """
        if port_use == "Arduino":
            try:
                self.ser_arduino.close()
                return "Arduino - Disconnected!"
            except Exception as e:
                return str(e)
        elif port_use == "GPS":
            try:
                self.ser_gps.close()
                return "GPS - Disconnected!"
            except Exception as e:
                return str(e)
