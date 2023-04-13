import tkinter as tk
import serial


class SerialOutputWindow:
    def __init__(self, serial_port):
        self.serial_port = serial_port
        self.serial_data = ""
        self.window = tk.Tk()
        self.window.title("Serial Output")
        self.window.geometry("400x300")
        self.text_area = tk.Text(self.window, height=20)
        self.text_area.pack()
        self.window.after(1000, self.update_serial_output)

    def update_serial_output(self):
        try:
            while self.serial_port.inWaiting() > 0:
                self.serial_data += self.serial_port.read(1).decode("utf-8")
            self.text_area.insert("end", self.serial_data)
            self.serial_data = ""
        except Exception as e:
            print(e)
        self.window.after(100, self.update_serial_output)

    def start(self):
        self.window.mainloop()


if __name__ == '__main__':
    serial_port = serial.Serial('COM6', 9600)
    window = SerialOutputWindow(serial_port)
    window.start()
