import tkinter as tk
import subprocess as sp


class Terminal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.output = tk.Text(self, height=20, width=80)
        self.output.pack()
        self.input = tk.Entry(self, width=80)
        self.input.pack()
        self.input.bind('<Return>', self.submit_command)

    def submit_command(self, event):
        command = self.input.get()
        self.input.delete(0, tk.END)
        result = sp.getoutput(command)
        self.output.insert(tk.END, f'{command}\n{result}\n')


root = tk.Tk()
terminal = Terminal(root)
terminal.mainloop()
