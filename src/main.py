import tkinter as tk
import tkinter.font as tkFont
import serial
import serial.tools.list_ports
import time
import tinyik as ik
import numpy as np
import threading
import queue

class App():
    def __init__(self, root):
        #setting title
        root.title("Dig Detect Desktop")
        #setting window size
        width=300
        height=200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)
        # Bind the function to the window's WM_DELETE_WINDOW protocol
        root.protocol("WM_DELETE_WINDOW", App.on_close)

        # Timer Attempt
        self.root = root
        self.refreshTimer()

        lblSerialPort=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblSerialPort["font"] = ft
        lblSerialPort["fg"] = "#333333"
        lblSerialPort["justify"] = "center"
        lblSerialPort["text"] = "Serial Port"
        lblSerialPort.place(x=20,y=20,width=70,height=25)

        lbSerialPorts=tk.Listbox(root)
        lbSerialPorts["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        lbSerialPorts["font"] = ft
        lbSerialPorts["fg"] = "#333333"
        lbSerialPorts["justify"] = "center"
        lbSerialPorts.place(x=100,y=20,width=150,height=25)
        self.lbSerialPorts = lbSerialPorts

        """
        msgSerialStream=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        msgSerialStream["font"] = ft
        msgSerialStream["fg"] = "#333333"
        msgSerialStream["justify"] = "center"
        msgSerialStream["text"] = "Message"
        msgSerialStream.place(x=370,y=10,width=300,height=50)
        """

        lblBaudRate=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblBaudRate["font"] = ft
        lblBaudRate["fg"] = "#333333"
        lblBaudRate["justify"] = "center"
        lblBaudRate["text"] = "Baud Rate"
        lblBaudRate.place(x=20,y=50,width=70,height=25)

        lbBaudRate=tk.Listbox(root)
        lbBaudRate["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        lbBaudRate["font"] = ft
        lbBaudRate["fg"] = "#333333"
        lbBaudRate["justify"] = "center"
        lbBaudRate.insert(tk.END, str(baudRate))
        lbBaudRate.place(x=100,y=50,width=150,height=25)
        self.lbBaudRate = lbBaudRate

        btnUpdatePorts=tk.Button(root)
        btnUpdatePorts["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnUpdatePorts["font"] = ft
        btnUpdatePorts["fg"] = "#000000"
        btnUpdatePorts["justify"] = "center"
        btnUpdatePorts["text"] = "Update Ports"
        btnUpdatePorts.place(x=20,y=100,width=100,height=30)
        btnUpdatePorts["command"] = self.btnUpdatePorts_command

        btnConnect=tk.Button(root)
        btnConnect["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnConnect["font"] = ft
        btnConnect["fg"] = "#000000"
        btnConnect["justify"] = "center"
        btnConnect["text"] = "Connect"
        btnConnect.place(x=130,y=100,width=100,height=30)
        btnConnect["command"] = self.btnConnect_command

        btnClearSerial=tk.Button(root)
        btnClearSerial["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnClearSerial["font"] = ft
        btnClearSerial["fg"] = "#000000"
        btnClearSerial["justify"] = "center"
        btnClearSerial["text"] = "Visualize Bucket"
        btnClearSerial.place(x=20,y=140,width=100,height=30)
        btnClearSerial["command"] = self.btnvisualizeBucket_command

        btnDisconnect=tk.Button(root)
        btnDisconnect["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnDisconnect["font"] = ft
        btnDisconnect["fg"] = "#000000"
        btnDisconnect["justify"] = "center"
        btnDisconnect["text"] = "Disconnect"
        btnDisconnect.place(x=130,y=140,width=100,height=30)
        btnDisconnect["command"] = self.btnDisconnect_command

        """
        lblSerialStream=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblSerialStream["font"] = ft
        lblSerialStream["fg"] = "#333333"
        lblSerialStream["justify"] = "center"
        lblSerialStream["text"] = "Serial Stream"
        lblSerialStream.place(x=280,y=40,width=100,height=50)
        """

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
    excavator = ik.Actuator(
            [[0, 0, 0.2], "z", [0.0, 0.0, .2], "y", [0.0, 0.0, 1],
                "y", [0.0, 0.0, 1], "y", [0.0, 0.0, 0.5]]
    )

    # End Effector Location
    efLocation = [0,0,0]

    root = tk.Tk()
    app = App(root)
    root.mainloop()

