import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import dd_plotting

plotter = dd_plotting.LinePlotter()

# Create a Tkinter window
root = tk.Tk()
root.title("Matplotlib plot in Tkinter")

# Add a Matplotlib plot to the Tkinter window
canvas = FigureCanvasTkAgg(plotter.fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Add a Quit button to the Tkinter window
quit_button = tk.Button(master=root, text='Quit', command=root.quit)
quit_button.pack(side=tk.BOTTOM)

# Start the Tkinter event loop
plotter.start_animation()
tk.mainloop()
