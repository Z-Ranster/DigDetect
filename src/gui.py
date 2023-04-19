# Import necessary libraries
import tkinter as tk
import dd_plotting
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
import os
import time
import sys
import time
import dd_serial
import matplotlib
import numpy as np
import random
import sys
import tkintermapview
import tinyik as ik
matplotlib.use("TkAgg")

# Set the path to the directory that contains the code file
OUTPUT_PATH = Path(__file__).parent
# Set the path to the directory that contains the assets
ASSETS_PATH = OUTPUT_PATH / Path((os.getcwd() + r"/src/assets/frame0"))

# Define a function that returns a path to an asset in the assets directory


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Application(tk.Frame):
    window = Tk()

    # Define Plotter
    plotter = dd_plotting.LinePlotter()

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
        command=lambda: app.update_serial_ports(),
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
        command=lambda: ik.visualize(app.excavator),
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
        command=lambda: app.connect_serial("Arduino"),
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
        command=lambda: app.close_serial("Arduino"),
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
        command=lambda: app.connect_serial("GPS"),
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
        command=lambda: app.close_serial("GPS"),
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

    # Declare global variables for the end effector location and current angles
    efLocation = [0, 0, 0]
    currentAngles = [0, 0, 0, 0]

    def update_serial_ports(self):
        """
        Gets a list of available serial ports and displays them in the GUI
        """
        # Call the update_serial_ports function from the dd_serial module to get the list of available ports
        ports = dd_serial.update_serial_ports()

        # Insert the available ports into the GUI
        app.text1.insert(tk.END, "-- Available Ports --\n")
        for port in ports:
            app.text1.insert(tk.END, str(port) + "\n")
        app.text1.insert(tk.END, "\n")

    def connect_serial(self, portUse):
        """
        Connects to the selected serial port for the specified device (Arduino or GPS)
        """
        if portUse == "Arduino":
            # Check if the Arduino serial connection is not already open
            if dd_serial.ser_arduino.is_open == False:
                # Get the selected serial port from the GUI entry box
                dd_serial.selected_SerialPort = self.entry_1.get()
                # Call the connect_serial function from the dd_serial module to connect to the Arduino
                result = dd_serial.connect_serial("Arduino")
                # Insert the result of the connection attempt into the GUI
                app.text1.insert(tk.END, result + "\n")
                app.text1.insert(tk.END, "\n")
        elif portUse == "GPS":
            # Check if the GPS serial connection is not already open
            if dd_serial.ser_gps.is_open == False:
                # Get the selected serial port from the GUI entry box
                dd_serial.selected_SerialPort = self.entry_2.get()
                # Call the connect_serial function from the dd_serial module to connect to the GPS
                result = dd_serial.connect_serial("GPS")
                # Insert the result of the connection attempt into the GUI
                app.text1.insert(tk.END, result + "\n")
                app.text1.insert(tk.END, "\n")

    def close_serial(self, portUse):
        """
        Closes the serial connection for both the Arduino and GPS devices and displays the results in the GUI.

        :param portUse: The name of the serial port to close.
        :return: None
        """
        # Call the close_serial function from the dd_serial module to close the specified serial connection
        result = dd_serial.close_serial(portUse)
        # Insert the result of the serial connection close attempt into the GUI
        app.text1.insert(tk.END, result + "\n")
        # Add a new line to separate the results of the Arduino and GPS serial connections
        app.text1.insert(tk.END, "\n")

    def update_data(self):
        """
        Reads data from the Arduino and updates the current angles
        """
        # Initialize the data variable
        data = [0] * 5

        # Check if the Arduino serial connection is open
        if dd_serial.ser_arduino.is_open:
            try:
                # Call the readArduinoData function from the dd_serial module to get data from the Arduino
                data = dd_serial.read_arduino_data()
                # Update the current angles with the data
                app.currentAngles[0] = float(data[1])
                app.currentAngles[1] = float(data[2])
                app.currentAngles[2] = float(data[3])
            except Exception as e:
                print("Error update_data:" + str(e))

    def update_location_in_space(self):
        """
        Updates the end effector location and checks if it is close to a line.

        :return: None
        """
        # Update the end effector location
        self.plotter.p0 = app.efLocation
        app.calculate_angle()

        # Check if end effector is close to a line
        if app.plotter.closeToLine:
            # Update the text and set rectangle to red if close to a line
            self.canvas.itemconfig(self.textClose, text="Close!")
            self.canvas.itemconfig(self.rec3, fill="#FF0000")
        else:
            # Reset the text and set rectangle to default color otherwise
            self.canvas.itemconfig(
                self.rec3, fill=self.canvas["background"], outline=self.canvas["background"])
            self.canvas.itemconfig(self.textClose, text="")

        # Store current angles for future reference
        self.previousAngles = self.currentAngles

    def initial_position(self):
        """
        Sets the initial angles of the excavator to [0, 81, 45, 126] and calculates the end effector location.

        :return: None
        """
        app.currentAngles = [0, 81, 45, 126]
        app.calculate_angle()

    def update_map(self):
        """
        Generates random data for the map and updates the marker position.

        :return: None
        """
        # generate random offsets within +-0.5ft
        offset_lat = random.uniform(-0.00000375, 0.00000375)
        offset_lng = random.uniform(-0.00000375, 0.00000375)

        # get current position of marker
        self.lat, self.lon = self.lat + offset_lat, self.lon + offset_lng

        # update marker position
        self.marker_1.set_position(self.lat, self.lon)

        # schedule next update
        self.after2 = self.master.after(500, self.update_map)

    def on_close(self):
        """
        Closes serial connections, stops animation, and exits the program.

        :return: None
        """
        print("Serial is ending...")
        # Close the connection to the Arduino and get the result
        result = dd_serial.close_serial("Arduino")
        print(result)  # Print the result of closing the Arduino connection
        # Close the connection to the GPS and get the result
        result = dd_serial.close_serial("GPS")
        print(result)  # Print the result of closing the GPS connection
        # Cancel the data_refresh_timer method's call using after method
        app.after_cancel(app.after1)
        app.map_widget.destroy()  # Destroy the map widget
        # Cancel the update_location_timer method's call using after method
        app.after_cancel(app.after2)
        app.plotter.stop_animation()  # Stop the plotter's animation
        print("Window is closing...")
        # Close the tkinter window
        print("Done closing everything...")
        sys.exit()  # Exit the program

    def data_refresh_timer(self):
        """
        Updates the data on the GUI and schedules the method to be called again.

        :return: None
        """
        # Get the current time
        current_time = time.strftime("%H:%M:%S")
        self.update_data()  # Update the data on the GUI
        # Schedule the data_refresh_timer() method to be called again in 1/100 second (10 milliseconds)
        self.after1 = self.after(10, self.data_refresh_timer)

    def update_location_timer(self):
        """
        Updates the end effector location periodically and schedules the method to be called again.

        :return: None
        """
        self.update_location_in_space()  # Update the end effector location
        # Schedule the update_location_timer() method to be called again in 1/10 second (100 milliseconds)
        self.after3 = self.after(100, self.update_location_timer)

    def calculate_angle(self):
        """
        Calculates angles for the excavator using the current angles, updates the excavator's angles to radians, and 
        calculates the end effector location.

        :return: None
        """
        # Convert the current angles to radians and update the excavator's angles
        app.excavator.angles = np.deg2rad(app.currentAngles)
        # Calculate the end effector location using the forward kinematics solver of the excavator object
        app.efLocation = app.excavator.fk.solve(np.deg2rad(app.currentAngles))

    # def useGPS(self):
    #     self.canvas.itemconfig(self.rec1, fill="#00FF00")
    #     self.canvas.itemconfig(self.rec2, fill="#FF0000")

    # def useLocal(self):
    #     self.canvas.itemconfig(self.rec1, fill="#FF0000")
    #     self.canvas.itemconfig(self.rec2, fill="#00FF00")


if __name__ == "__main__":
    # Initialize the tkinter window
    app = Application()

    # Initialize the DDSerial object
    dd_serial = dd_serial.SerialConnection()

    # Set the title of the window
    app.master.title("Dig Detect Desktop")

    # Set the close protocol for the window
    app.master.protocol("WM_DELETE_WINDOW", app.on_close)

    # Set the window size
    app.master.geometry("1024x600")

    # Set the background color of the window
    app.master.configure(bg="#232323")

    # Disable window resizing
    app.master.resizable(False, False)

    # Make the window be full screen
    # app.master.attributes("-fullscreen", True)

    # Set the initial position of the window
    app.initial_position()

    # Start the data refresh timer
    app.data_refresh_timer()

    # Start the location update timer
    app.update_location_timer()

    # Update the map
    app.update_map()

    # Start the animation
    app.plotter.start_animation()

    # Start the tkinter event loop
    app.mainloop()
