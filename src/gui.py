
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
# Documentation --> https://tkdocs.com/index.html


import tkinter as tk
import DDPlotting
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path

import os
import time
import DDSerial
import kinematics
import matplotlib
import numpy as np
import random
import sys
import tkintermapview
matplotlib.use("TkAgg")

# Explicit imports to satisfy Flake8

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path((os.getcwd() + r"/src/assets/frame0"))


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Application(tk.Frame):
    window = Tk()

    # Define Plotter
    plotter = DDPlotting.LinePlotter()

    # Define after1
    after1, after2 = None, None

    # Get GPS Information
    lat, lon = 35.76926, -78.67635

    canvas = Canvas(
        window,
        bg="#232323",
        height=400,
        width=865,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        387,
        54,
        anchor="nw",
        text="GPS Location",
        fill="#D9D9D9",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        749,
        48,
        anchor="nw",
        text="Bucket Location",
        fill="#D9D9D9",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        20,
        49.0,
        anchor="nw",
        text="COM Port",
        fill="#D9D9D9",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        464,
        17,
        anchor="nw",
        text="Dig Detect",
        fill="#D9D9D9",
        font=("Roboto Medium", 20 * -1)
    )

    canvas.create_text(
        26,
        206,
        anchor="nw",
        text="Close!",
        fill="#D9D9D9",
        font=("Roboto Medium", 20 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        167.5,
        60.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=122.0,
        y=49.0,
        width=91.0,
        height=20.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: app.updateSerialPorts(),
        relief="flat"
    )
    button_1.place(
        x=20,
        y=82.0,
        width=91.0,
        height=22.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: app.useLocal(),
        relief="flat"
    )
    button_2.place(
        x=20.0,
        y=175,
        width=91.0,
        height=22.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: app.useGPS(),
        relief="flat"
    )
    button_3.place(
        x=20,
        y=144,
        width=91.0,
        height=22.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: app.visualizeModel(),
        relief="flat"
    )
    button_5.place(
        x=20.0,
        y=113.0,
        width=91.0,
        height=22.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: app.connectSerial(),
        relief="flat"
    )
    button_6.place(
        x=122.0,
        y=82.0,
        width=91.0,
        height=22.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: app.disconnectSerial(),
        relief="flat"
    )
    button_7.place(
        x=123.0,
        y=113.0,
        width=91.0,
        height=22.0
    )

    # Placeholder for GPS Location
    # image_image_1 = PhotoImage(
    #     file=relative_to_assets("image_1.png"))
    # image_1 = canvas.create_image(
    #     374.0,
    #     186.0,
    #     image=image_image_1
    # )

    # create map widget
    map_widget = tkintermapview.TkinterMapView(
        window, width=300, height=300, corner_radius=0)
    map_widget.place(x=288, y=84)

    # set current widget position and zoom
    map_widget.set_position(lat, lon)  # Hunt Library
    map_widget.set_zoom(17)

    # add markers to map
    marker_1 = map_widget.set_marker(
        lat, lon)

    # Placeholder for the 3D Plot
    # canvas.create_rectangle(
    #     545.0,
    #     82.0,
    #     787.0,
    #     291.0,
    #     fill="#D9D9D9",
    #     outline="")

    canvas2 = FigureCanvasTkAgg(plotter.fig, master=window)
    canvas2.draw()
    canvas2.get_tk_widget().place(x=663, y=84, width=300, height=300)

    rec1 = canvas.create_rectangle(
        122,
        144,
        144.0,
        166.0,
        fill="#FF0000",
        outline="")

    rec2 = canvas.create_rectangle(
        122.0,
        175.0,
        144.0,
        197.0,
        fill="#00FF00",
        outline="")

    rec3 = canvas.create_rectangle(
        122.0,
        206,
        144.0,
        228.0,
        fill="#00FF00",
        outline="")

    def updateSerialPorts(self):
        DDSerial.updateSerialPorts()

    def visualizeModel(self):
        kinematics.visualizeKM()

    def connectSerial(self):
        if DDSerial.serArduino.is_open == False:
            DDSerial.selected_SerialPort = self.entry_1.get()
            DDSerial.startSerial("Arduino")

    def disconnectSerial(self):
        DDSerial.closeSerial("Arduino")
        DDSerial.closeSerial("GPS")

    def updateData(self):
        data = [0] * 10
        # Read Data
        if DDSerial.serArduino.is_open:
            data = DDSerial.readSerial()
        # Process Data
        float_array = [float(x) for x in data[1:5]]
        kinematics.calculateAngle(float_array)
        # Create a random number generator for variable i
        i = random.randint(0, 100)
        self.plotter.p0 = [
            5 + 3*np.sin(i/10), 1 + np.cos(i/10), 1 + np.sin(i/10)]

        # print(kinematics.efLocation)
        # app.plotter.set_point(kinematics.efLocation)
        # If DDPlotting.CloseToLine is true, then change rec3 to red
        if app.plotter.closeToLine:
            self.canvas.itemconfig(self.rec3, fill="#FF0000")
            # print("The point is close to the line.")
        else:
            self.canvas.itemconfig(self.rec3, fill="#00FF00")
            # print("The point is not close to the line.")

    def updateMap(self):
        # Generate random data for the map and update the map
        # generate random offsets within +-1ft
        offset_lat = random.uniform(-0.0000075, 0.0000075)
        offset_lng = random.uniform(-0.0000075, 0.0000075)

        # get current position of marker
        self.lat, self.lon = self.lat + offset_lat, self.lon + offset_lng

        # update marker position
        self.marker_1.set_position(self.lat, self.lon)

        # schedule next update
        self.after2 = self.master.after(500, self.updateMap)

    def on_close(self):
        print("Serial is ending...")
        DDSerial.closeSerial("Arduino")
        DDSerial.closeSerial("GPS")
        app.after_cancel(app.after1)
        app.map_widget.destroy()
        app.after_cancel(app.after2)
        app.plotter.stop_animation()
        print("Window is closing...")
        # Close the tkinter window
        # self.window.destroy()
        print("Done closing everything...")
        sys.exit()

    # This is the function that will be updating all of the gui elements.
    def dataRefreshTimer(self):
        # Get the current time
        current_time = time.strftime("%H:%M:%S")
        self.updateData()
        # Schedule the refreshTimer() method to be called again in 1 second
        self.after1 = self.after(50, self.dataRefreshTimer)

    def useGPS(self):
        self.canvas.itemconfig(self.rec1, fill="#00FF00")
        self.canvas.itemconfig(self.rec2, fill="#FF0000")
        if DDSerial.serGPS.is_open == False:
            DDSerial.selected_SerialPort = self.entry_1.get()
            DDSerial.startSerial("GPS")

    def useLocal(self):
        self.canvas.itemconfig(self.rec1, fill="#FF0000")
        self.canvas.itemconfig(self.rec2, fill="#00FF00")


if __name__ == "__main__":
    # Define a tkinter window
    app = Application()
    app.master.title("Dig Detect Desktop")
    app.master.protocol("WM_DELETE_WINDOW", app.on_close)

    app.master.geometry("1024x600")
    app.master.configure(bg="#232323")
    app.master.resizable(False, False)
    app.dataRefreshTimer()
    app.updateMap()
    app.plotter.start_animation()
    app.mainloop()
