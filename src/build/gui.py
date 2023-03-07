
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

import os
from mainTest import runnableItems as RI
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path((os.getcwd() + r"\src\build\assets\frame0"))

window = Tk()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def graph(fig):
    canvas = FigureCanvasTkAgg(fig)

def create_window():
    window.title("Dig Detect Desktop")
    window.protocol("WM_DELETE_WINDOW", RI.on_close)
    # Timer Attempt
    RI.refreshTimer()
    window.geometry("800x400")
    window.configure(bg = "#232323")


    canvas = Canvas(
        window,
        bg = "#232323",
        height = 400,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        324.0,
        49.0,
        anchor="nw",
        text="GPS Location",
        fill="#D9D9D9",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        602.0,
        49.0,
        anchor="nw",
        text="Bucket Location",
        fill="#D9D9D9",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        19.0,
        49.0,
        anchor="nw",
        text="Serial Port",
        fill="#D9D9D9",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        19.0,
        85.0,
        anchor="nw",
        text="Baud Rate",
        fill="#D9D9D9",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        352.0,
        15.0,
        anchor="nw",
        text="Dig Detect",
        fill="#D9D9D9",
        font=("Roboto Medium", 20 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        113.0,
        256.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=13.0,
        y=221.0,
        width=200.0,
        height=68.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        167.5,
        96.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=122.0,
        y=85.0,
        width=91.0,
        height=20.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        167.5,
        60.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=122.0,
        y=49.0,
        width=91.0,
        height=20.0
    )

    canvas.create_text(
        37.0,
        199.0,
        anchor="nw",
        text="Serial Communication",
        fill="#D9D9D9",
        font=("Roboto", 15 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=13.0,
        y=128.0,
        width=91.0,
        height=22.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=240.0,
        y=366.0,
        width=91.0,
        height=22.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=240.0,
        y=333.0,
        width=91.0,
        height=22.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=13.0,
        y=333.0,
        width=91.0,
        height=22.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=13.0,
        y=163.0,
        width=91.0,
        height=22.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=122.0,
        y=128.0,
        width=91.0,
        height=22.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=122.0,
        y=163.0,
        width=91.0,
        height=22.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        374.0,
        186.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        545.0,
        82.0,
        787.0,
        291.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        -4.98468017578125,
        313.5,
        800.0153198242188,
        318.5,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        342.0,
        335.0,
        362.0,
        355.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        342.0,
        368.0,
        362.0,
        388.0,
        fill="#D9D9D9",
        outline="")
    window.resizable(False, False)
    window.mainloop()
