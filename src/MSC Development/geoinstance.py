import tkinter as tk
import tkintermapview
import random


class MyApp:
    def __init__(self, master):

        self.master = master
        master.title("My Tkinter App")

        # create map widget
        self.map_widget = tkintermapview.TkinterMapView(
            master, width=800, height=600, corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # set current widget position and zoom
        self.map_widget.set_position(35.787743, -78.672858)  # Hunt Library
        self.map_widget.set_zoom(17)

        # add markers to map
        self.marker_1 = self.map_widget.set_marker(
            self.lat, self.lon, text="Marker 1")

        # schedule marker update
        self.master.after(500, self.update_marker)

    def update_marker(self):

        # generate random offsets within +-100ft
        offset_lat = random.uniform(-0.00015, 0.00015)
        offset_lng = random.uniform(-0.00015, 0.00015)

        # get current position of marker
        self.lat, self.lon = self.lat + offset_lat, self.lon + offset_lng

        # update marker position
        self.marker_1.set_position(self.lat, self.lon)

        # schedule next update
        self.master.after(500, self.update_marker)


root = tk.Tk()
app = MyApp(root)
root.mainloop()
