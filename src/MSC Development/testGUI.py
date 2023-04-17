import tkinter as tk
import serial

# Set up the serial port and open it
ser = serial.Serial('COM8', 9600)

# Create a Tkinter window
root = tk.Tk()
root.title("Serial Output")

# Create a text widget to display the serial output
text = tk.Text(root)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scroll bar for the text widget
scrollbar = tk.Scrollbar(root, command=text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Associate the scroll bar with the text widget
text.configure(yscrollcommand=scrollbar.set)

# Define a function to read data from the serial port and display it in the text widget


def read_serial():
    # Read data from the serial port
    data = ser.readline().decode('utf-8')

    # Display the data in the text widget
    text.insert(tk.END, data)

    # Schedule the function to be called again in 10 milliseconds
    root.after(10, read_serial)


# Call the read_serial function to start reading data from the serial port
read_serial()

# Start the Tkinter event loop
root.mainloop()

# Close the serial port when the Tkinter window is closed
ser.close()

ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
