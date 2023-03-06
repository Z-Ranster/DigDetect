import tkinter as tk
import tkinter.font as tkFont   
from pathlib import Path
from tkinter import *
# Explicit imports to satisfy Flake8
import serial
import serial.tools.list_ports
import time
import tinyik as ik
import numpy as np
import threading
import queue
import build.gui

# Write a todo comment
# TODO: Implement zero location switch
# TODO: Implement Local vs. gps digitial switch
# TODO: Implement https://github.com/ParthJadhav/Tkinter-Designer
# TODO: Implement Zeroing block to help reference the size of the excavtor
# TODO: Implement a plot of the excavator end effector with relation to inground objects
# TODO: Setup and configure the Nvidia Jetson
# TODO: Implement hash checking on the serial string to avoid the crashing that currently happens

class App():
    def __init__(self, root):
        #a = 0
        #setting title
        #root.title("Dig Detect Desktop")
        #setting window size
        #width=800 # <-- TODO: update this on resize
        #height=300 # <-- TODO: update this on resize
        #screenwidth = root.winfo_screenwidth()
        #screenheight = root.winfo_screenheight()
        #alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        #root.geometry(alignstr)
        #root.resizable(width=False, height=False)
        # Bind the function to the window's WM_DELETE_WINDOW protocol
        #root.protocol("WM_DELETE_WINDOW", App.on_close)

    def btnUpdatePorts_command(self):
        self.lbSerialPorts.delete(0, tk.END)
        ports = serial.tools.list_ports.comports()
        # Read and Print Serial Ports
        for port in ports:
            self.lbSerialPorts.insert(tk.END, port.device)

    def btnConnect_command(self):
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

    def btnvisualizeBucket_command(self):
        ik.visualize(excavator)
        print("Clear Serial")

    def btnDisconnect_command(self):
        try:
            ser.close()
            print("Disconnected!")
        except serial.SerialException as e:
            print("Error opening serial port: {e}")
        except Exception as e:
            print("Unknown error opening serial port: {e}")

    def on_close():
        print("Window is closing...")
        print("Serial is ending...")
        ser.close()
        root.destroy()
        print("Done closing everything...")

    # This is the function that will be updating all of the gui elements.
    def refreshTimer(self):
        # Get the current time
        current_time = time.strftime("%H:%M:%S")
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
                excavator.angles = np.deg2rad(deg)
                efLocation = excavator.fk.solve(np.deg2rad(deg))
                print(efLocation)

        # Schedule the refreshTimer() method to be called again in 1 second
        self.root.after(10, self.refreshTimer)

class processingThread(threading.Thread):
    def __init__(self, q, chain):
        threading.Thread.__init__(self)
        self.q = q
        self.chain = chain
    
    def run(self):

        print(self.chain.fk.solve(np.deg2rad(deg)))
        ik.visualize(self.chain)
        queue.task_done()

if __name__ == "__main__":
    # Serial Variables
    baudRate = 9600
    selected_SerialPort = ''
    ser = serial.Serial()

    # Kinematic Chain
    # Units in inches
    excavator = ik.Actuator(
            [[0, 0, 0.2], "z", [0.0, 0.5, 0.0], "y", [0.0, 0.0, 1],
                "y", [0.0, 0.0, 1], "y", [0.0, 0.0, 0.5]]
    )

    # End Effector Location
    efLocation = [0,0,0]

    #root = tk.Tk()
    #app = App(root)
    root = tk.Tk()
    app = gui.
    #root.mainloop()

