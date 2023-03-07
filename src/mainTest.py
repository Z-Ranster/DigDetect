import threading
import queue
import time
import gui
import DDSerial

# Write a todo comment
# TODO: Implement zero location switch
# TODO: Implement Local vs. gps digitial switch
# TODO: Implement https://github.com/ParthJadhav/Tkinter-Designer
# TODO: Implement Zeroing block to help reference the size of the excavtor
# TODO: Implement a plot of the excavator end effector with relation to inground objects
# TODO: Setup and configure the Nvidia Jetson
# TODO: Implement hash checking on the serial string to avoid the crashing that currently happens

class App():
    def btnUpdatePorts_command(self):
        self.lbSerialPorts.delete(0, tk.END)
        ports = DDSerial.tools.list_ports.comports()
        # Read and Print Serial Ports
        for port in ports:
            self.lbSerialPorts.insert(tk.END, port.device)

    def btnConnect_command(self):
        DDSerial.startSerial()

    def btnvisualizeBucket_command(self):
        print("Visualize Bucket")

    def btnDisconnect_command(self):
        DDSerial.closeSerial()

    def on_close():
        print("Serial is ending...")
        DDSerial.closeSerial()
        print("Window is closing...")
        # Close the tkinter window
        root.destroy()
        # Stop both threads
        #guiThread.
        #dpThread.stop()
        print("Done closing everything...")

# A thread to start the gui
def gui_thread():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# A thread to start data processing
def processing_thread():
    while True:
        DDSerial.readSerial()
        time.sleep(1)

def bucketVisual_thread(model):
    ik.visualize(model)

if __name__ == "__main__":
    # Kinematic Chain
    # Units in inches
    excavator = ik.Actuator(
            [[0, 0, 0.2], "z", [0.0, 0.5, 0.0], "y", [0.0, 0.0, 1],
                "y", [0.0, 0.0, 1], "y", [0.0, 0.0, 0.5]]
    )

    # End Effector Location
    efLocation = [0,0,0]

    # Start the gui and data processing threads
    guiThread = threading.Thread(target=gui_thread)
    guiThread.start()
    dpThread = threading.Thread(target=processing_thread)
    dpThread.start()
