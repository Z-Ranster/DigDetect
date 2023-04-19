import tkinter as tk
import DDPlotting
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path

import os
import time
import sys
import time
import DDSerial
import matplotlib
import numpy as np
import random
import sys
import tkintermapview
import tinyik as ik
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
    after1, after2, after3 = None, None, None

    # Get GPS Information
    lat, lon = 35.76979, -78.67625

    # Define eFLocation
    efLocation = [0, 0, 0]
    currentAngles = [0, 0, 0, 0]
    previousAngles = [0, 0, 0, 0]

    canvas = Canvas(
        window,
        bg="#232323",
        height=600,
        width=1024,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        288.0,
        49.0,
        anchor="nw",
        text="GPS Location",
        fill="#D9D9D9",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        288.0,
        434.0,
        anchor="nw",
        text="Data Output",
        fill="#D9D9D9",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        663.0,
        49.0,
        anchor="nw",
        text="Bucket Location",
        fill="#D9D9D9",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        42.0,
        84.0,
        anchor="nw",
        text="COM",
        fill="#D9D9D9",
        font=("Roboto", 15 * -1)
    )

    textClose = canvas.create_text(
        772,
        398,
        anchor="nw",
        text="",
        fill="#FF0000",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        425.0,
        17.0,
        anchor="nw",
        text="Dig Detect Desktop",
        fill="#D9D9D9",
        font=("Roboto Medium", 20 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        190.5,
        95.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=145.0,
        y=84.0,
        width=91.0,
        height=20.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        190.5,
        177.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=145.0,
        y=166.0,
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
        x=145.0,
        y=330.0,
        width=91.0,
        height=22.0
    )

    # button_image_2 = PhotoImage(
    #     file=relative_to_assets("button_2.png"))
    # button_2 = Button(
    #     image=button_image_2,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: app.useLocal(),
    #     relief="flat"
    # )
    # button_2.place(
    #     x=42.0,
    #     y=281.0,
    #     width=91.0,
    #     height=22.0
    # )

    # button_image_3 = PhotoImage(
    #     file=relative_to_assets("button_3.png"))
    # button_3 = Button(
    #     image=button_image_3,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: app.useGPS(),
    #     relief="flat"
    # )
    # button_3.place(
    #     x=42.0,
    #     y=246.0,
    #     width=91.0,
    #     height=22.0
    # )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: app.visualizeModel(),
        relief="flat"
    )
    button_4.place(
        x=44.0,
        y=330.0,
        width=91.0,
        height=22.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: app.connectSerial("Arduino"),
        relief="flat"
    )
    button_5.place(
        x=45.0,
        y=117.0,
        width=91.0,
        height=22.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: DDSerial.closeSerial("Arduino"),
        relief="flat"
    )
    button_6.place(
        x=145.0,
        y=119.0,
        width=91.0,
        height=22.0
    )

    canvas.create_text(
        42.0,
        166.0,
        anchor="nw",
        text="GPS",
        fill="#D9D9D9",
        font=("Roboto", 15 * -1)
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: app.connectSerial("GPS"),
        relief="flat"
    )
    button_7.place(
        x=42.0,
        y=199.0,
        width=91.0,
        height=22.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: DDSerial.closeSerial("GPS"),
        relief="flat"
    )
    button_8.place(
        x=145.0,
        y=199.0,
        width=91.0,
        height=22.0
    )

    # Create Map Widget
    map_widget = tkintermapview.TkinterMapView(
        window, width=300, height=300, corner_radius=0)
    map_widget.place(x=288, y=84)
    # set current widget position and zoom
    map_widget.set_position(lat, lon)
    map_widget.set_zoom(17)
    # add markers to map
    marker_1 = map_widget.set_marker(
        lat, lon)

    # Create Plotter Widget
    canvas2 = FigureCanvasTkAgg(plotter.fig, master=window)
    canvas2.draw()
    canvas2.get_tk_widget().place(x=663, y=84, width=300, height=300)

    # rec1 = canvas.create_rectangle(
    #     145.0,
    #     246.0,
    #     167.0,
    #     268.0,
    #     fill="#D9D9D9",
    #     outline="")

    # rec2 = canvas.create_rectangle(
    #     145.0,
    #     281.0,
    #     167.0,
    #     303.0,
    #     fill="#D9D9D9",
    #     outline="")

    rec3 = canvas.create_rectangle(
        850.0,
        398.0,
        872.0,
        420.0,
        fill="#D9D9D9",
        outline="")

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        135.0,
        480.0,
        image=image_image_2
    )

    text1 = tk.Text(window)
    text1.place(x=288.0, y=464.0)
    text1Scrollbar = tk.Scrollbar(window, command=text1.yview)
    text1Scrollbar.place(x=953.0, y=464.0, height=116)
    text1.configure(yscrollcommand=text1Scrollbar.set, width=83, height=7)

    # Kinematic Chain
    # Units in inches
    excavator = ik.Actuator(
        [[0, 0, 2.19], "z", [0.0, 0.000001, 0.0], "y", [0.0, 0.0, 7.5],
            "y", [0.0, 0.0, 3.5], "y", [0.0, 0.0, 2.4]]
    )

    # End Effector Location
    efLocation = [0, 0, 0]
    currentAngles = [0, 0, 0, 0]

    def updateSerialPorts(self):
        ports = DDSerial.updateSerialPorts()
        app.text1.insert(tk.END, "-- Available Ports --\n")
        for port in ports:
            app.text1.insert(tk.END, str(port) + "\n")
        app.text1.insert(tk.END, "\n")

    def visualizeModel(self):
        app.visualizeKM()

    def connectSerial(self, portUse):
        if portUse == "Arduino":
            if DDSerial.serArduino.is_open == False:
                DDSerial.selected_SerialPort = self.entry_1.get()
                result = DDSerial.startSerial("Arduino")
                app.text1.insert(tk.END, result + "\n")
                app.text1.insert(tk.END, "\n")

        elif portUse == "GPS":
            if DDSerial.serGPS.is_open == False:
                DDSerial.selected_SerialPort = self.entry_2.get()
                result = DDSerial.startSerial("GPS")
                app.text1.insert(tk.END, result + "\n")
                app.text1.insert(tk.END, "\n")

    def disconnectSerial(self):
        result = DDSerial.closeSerial("Arduino")
        app.text1.insert(tk.END, result + "\n")
        result = DDSerial.closeSerial("GPS")
        app.text1.insert(tk.END, result + "\n")
        app.text1.insert(tk.END, "\n")

    def updateData(self):
        data = [0] * 5
        # Read Arduino Data
        if DDSerial.serArduino.is_open:
            try:
                data = DDSerial.readArduinoData()
                app.currentAngles[0] = float(data[1])
                app.currentAngles[1] = float(data[2])
                app.currentAngles[2] = float(data[3])
            except Exception as e:
                pass

    def updateLocationInSpace(self):
        self.plotter.p0 = app.efLocation
        app.calculateAngle()

        # If DDPlotting.CloseToLine is true, then change rec3 to red
        if app.plotter.closeToLine:
            self.canvas.itemconfig(self.textClose, text="Close!")
            self.canvas.itemconfig(self.rec3, fill="#FF0000")
        else:
            self.canvas.itemconfig(
                self.rec3, fill=self.canvas["background"], outline=self.canvas["background"])
            self.canvas.itemconfig(self.textClose, text="")
        self.previousAngles = self.currentAngles

    def initialPosition(self):
        # Angles in Degrees
        app.currentAngles = [0, 81, 45, 126]
        app.calculateAngle()

    def updateMap(self):
        # Generate random data for the map and update the map
        # generate random offsets within +-0.5ft
        offset_lat = random.uniform(-0.00000375, 0.00000375)
        offset_lng = random.uniform(-0.00000375, 0.00000375)

        # get current position of marker
        self.lat, self.lon = self.lat + offset_lat, self.lon + offset_lng

        # update marker position
        self.marker_1.set_position(self.lat, self.lon)

        # schedule next update
        self.after2 = self.master.after(500, self.updateMap)

    def on_close(self):
        print("Serial is ending...")
        result = DDSerial.closeSerial("Arduino")
        print(result)
        result = DDSerial.closeSerial("GPS")
        print(result)
        app.after_cancel(app.after1)
        app.map_widget.destroy()
        app.after_cancel(app.after2)
        app.plotter.stop_animation()
        print("Window is closing...")
        # Close the tkinter window
        print("Done closing everything...")
        sys.exit()

    # This is the function that will be updating all of the gui elements.
    def dataRefreshTimer(self):
        # Get the current time
        current_time = time.strftime("%H:%M:%S")
        self.updateData()
        # Schedule the refreshTimer() method to be called again in 1 second
        self.after1 = self.after(10, self.dataRefreshTimer)

    def updateLocationTimer(self):
        self.updateLocationInSpace()
        self.after3 = self.after(100, self.updateLocationTimer)

    # def useGPS(self):
    #     self.canvas.itemconfig(self.rec1, fill="#00FF00")
    #     self.canvas.itemconfig(self.rec2, fill="#FF0000")

    # def useLocal(self):
    #     self.canvas.itemconfig(self.rec1, fill="#FF0000")
    #     self.canvas.itemconfig(self.rec2, fill="#00FF00")

    def calculateAngle(self):
        app.excavator.angles = np.deg2rad(app.currentAngles)
        app.efLocation = app.excavator.fk.solve(np.deg2rad(app.currentAngles))

    def visualizeKM(self):
        ik.visualize(app.excavator)


if __name__ == "__main__":
    # Define a tkinter window
    app = Application()
    app.master.title("Dig Detect Desktop")
    app.master.protocol("WM_DELETE_WINDOW", app.on_close)
    # app.master.attributes("-fullscreen", True)

    app.master.geometry("1024x600")
    app.master.configure(bg="#232323")
    app.master.resizable(False, False)
    app.initialPosition()
    app.dataRefreshTimer()
    app.updateLocationTimer()
    app.updateMap()
    app.plotter.start_animation()
    app.mainloop()
