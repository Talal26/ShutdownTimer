import tkinter as tk
from tkinter import messagebox
from subprocess import run


class MyGUI:
    def __init__(self):

        mainfont = ('Arial', 10)

        self.root = tk.Tk()
        self.root.title('Shutdown timer')

        # Making frame for hours and minutes entries and labels
        self.entryframe = tk.Frame(self.root)
        self.entryframe.rowconfigure(0, pad=10, weight=1)
        self.entryframe.rowconfigure(1, pad=10, weight=1)
        self.entryframe.columnconfigure(0, pad=10, weight=1)
        self.entryframe.columnconfigure(1, pad=10, weight=1)

        self.hourslabel = tk.Label(self.entryframe, text='Hours:', font=mainfont)
        self.hourslabel.grid(row=0, column=0, padx=(0, 10), sticky='e')

        self.hoursentry = tk.Entry(self.entryframe, font=mainfont)
        self.hoursentry.grid(row=0, column=1, padx=(0, 10), sticky='ew')
        self.hoursentry.focus_set()  # Sets default cursor position to 'Hours' entry

        self.minuteslabel = tk.Label(self.entryframe, text='Minutes:', font=mainfont)
        self.minuteslabel.grid(row=1, column=0, padx=(0, 10), sticky='e')

        self.minutesentry = tk.Entry(self.entryframe, font=mainfont, width=10)
        self.minutesentry.grid(row=1, column=1, padx=(0, 10), sticky='ew')

        self.entryframe.pack(padx=10, pady=10)

        # Making shutdown and restart toggles
        self.radioframe = tk.Frame(self.root)
        self.radioframe.columnconfigure(0, weight=1, pad=20)
        self.radioframe.columnconfigure(1, weight=1, pad=20)

        self.restartvar = tk.StringVar()
        self.restartvar.set('shutdown')

        shutdownbutton = tk.Radiobutton(self.radioframe, text='shutdown', variable=self.restartvar, value='shutdown',
                                        font=mainfont)
        shutdownbutton.grid(row=0, column=0)

        restartbutton = tk.Radiobutton(self.radioframe, text='restart', variable=self.restartvar, value='restart',
                                       font=mainfont)
        restartbutton.grid(row=0, column=1)

        self.radioframe.pack(pady=10)

        # Making Start and Cancel buttons
        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        self.startbutton = tk.Button(self.buttonframe, text='Start', command=self.start, width=10)
        self.startbutton.grid(row=0, column=0)

        self.cancelbutton = tk.Button(self.buttonframe, text='Cancel', command=self.cancel, width=10)
        self.cancelbutton.grid(row=0, column=1)

        self.buttonframe.pack(padx=10, pady=10, side=tk.RIGHT)

    def display(self):
        """Displays the window"""

        self.root.mainloop()

    def start(self):
        """Start button instruction"""

        # Check if user inputted a number
        try:
            hours = int(self.hoursentry.get() or 0)
        except ValueError:
            hourslabeltext = self.hourslabel.cget('text')
            messagebox.showinfo('Error', f'Please input an integer in the \'{hourslabeltext}\' entry')
            return

        try:
            minutes = int(self.minutesentry.get() or 0)
        except ValueError:
            minuteslabeltext = self.minuteslabel.cget('text')
            messagebox.showinfo('Error', f'Please input an integer in the \'{minuteslabeltext}\' entry')
            return

        totalseconds = (hours * 3600) + (minutes * 60)

        # Check if user inputted values greater than 0
        if totalseconds <= 0:
            messagebox.showinfo('Error', 'Please input values greater than 0')
            return

        shutdowntype = self.restartvar.get()  # Get which radiobutton was selected
        shutdowntags = {'shutdown': '-s', 'restart': '-r'}
        tag = shutdowntags[shutdowntype]

        # Execute command line task
        command = f'shutdown {tag} -t {totalseconds}'
        run(command)

        self.root.quit()  # Closes the window

    def cancel(self):
        """Cancel button instruction"""

        self.root.quit()  # Closes the window


if __name__ == '__main__':
    window = MyGUI()
    window.display()
