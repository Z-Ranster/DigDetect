import threading
import build.gui as gui
import time
import DDSerial
import matplotlib.pylab as plt
import kinematics
import sched

# Write a todo comment
# TODO: Implement Zeroing block to help reference the size of the excavtor
# TODO: Implement a plot of the excavator end effector with relation to inground objects
# TODO: Setup and configure the Nvidia Jetson

class runnableItems():
    def updateSerialPorts():
        DDSerial.updateSerialPorts()

    def visualizeModel():
        kinematics.visualizeKM()

    def connectSerial():
        DDSerial.startSerial()

    def disconnectSerial():
        DDSerial.closeSerial()

    def updateData():
        print("Updating Data...")
        # Read Data
        deg = DDSerial.readSerial()
        # Update Kinematics
        kinematics.calculateAngle(deg)

    def on_close():
        print("Serial is ending...")
        DDSerial.closeSerial()
        print("Window is closing...")
        # Close the tkinter window
        gui.window.destroy()
        # Stop both threads
        print("Done closing everything...")

    # This is the function that will be updating all of the gui elements.
    def refreshTimer():
        # Get the current time
        current_time = time.strftime("%H:%M:%S")
        runnableItems.updateData()
        #scheduler.enter(10, runnableItems.refreshTimer)

if __name__ == "__main__":
    gui.create_window()
    
