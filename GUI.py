import tkinter as tk
import shutdown
from tkinter import messagebox  # Needs explicit import


class ShutdownTypes:
    SHUTDOWN = 'shutdown'
    RESTART = 'restart'
    SLEEP = 'sleep'


class GUI:
    def __init__(self):
        mainfont = ('Arial', 10)

        self.root = tk.Tk()
        self.root.title('Shutdown timer')

        # Making frame for hours and minutes entries and labels
        self.entryframe = tk.Frame(self.root)
        self.entryframe.rowconfigure(0, pad=5, weight=1)
        self.entryframe.rowconfigure(1, pad=5, weight=1)
        self.entryframe.rowconfigure(2, pad=5, weight=1)
        self.entryframe.columnconfigure(0, pad=20, weight=1)
        self.entryframe.columnconfigure(1, pad=80, weight=1)

        # Hours row
        self.hourslabel = tk.Label(self.entryframe, text='Hours:', font=mainfont)
        self.hourslabel.grid(row=0, column=0, padx=(0, 10), sticky='e')

        self.hoursentry = tk.Entry(self.entryframe, font=mainfont, width=10)
        self.hoursentry.grid(row=0, column=1, padx=(0, 10), sticky='ew')
        self.hoursentry.focus_set()  # Sets default cursor position to 'Hours' entry

        # Minutes row
        self.minuteslabel = tk.Label(self.entryframe, text='Minutes:', font=mainfont)
        self.minuteslabel.grid(row=1, column=0, padx=(0, 10), sticky='e')

        self.minutesentry = tk.Entry(self.entryframe, font=mainfont, width=10)
        self.minutesentry.grid(row=1, column=1, padx=(0, 10), sticky='ew')

        # Seconds row
        self.secondslabel = tk.Label(self.entryframe, text='Seconds:', font=mainfont)
        self.secondslabel.grid(row=2, column=0, padx=(0, 10), sticky='e')

        self.secondsentry = tk.Entry(self.entryframe, font=mainfont, width=10)
        self.secondsentry.grid(row=2, column=1, padx=(0, 10), sticky='ew')

        self.entryframe.pack(padx=10, pady=10)  # Packing the frame

        # Shutdown/Restart/Sleep Radio Buttons
        self.radioframe = tk.Frame(self.root)
        self.radioframe.columnconfigure(0, weight=1, pad=10)
        self.radioframe.columnconfigure(1, weight=1, pad=10)
        self.radioframe.columnconfigure(2, weight=1, pad=10)

        self.var = tk.StringVar()
        self.var.set(ShutdownTypes.SHUTDOWN)  # Setting default shutdown type

        shutdownbutton = tk.Radiobutton(self.radioframe, text=ShutdownTypes.SHUTDOWN, variable=self.var,
                                        value=ShutdownTypes.SHUTDOWN, font=mainfont)
        shutdownbutton.grid(row=0, column=0)

        restartbutton = tk.Radiobutton(self.radioframe, text=ShutdownTypes.RESTART, variable=self.var,
                                       value=ShutdownTypes.RESTART, font=mainfont)
        restartbutton.grid(row=0, column=1)

        sleepbutton = tk.Radiobutton(self.radioframe, text=ShutdownTypes.SLEEP, variable=self.var,
                                     value=ShutdownTypes.SLEEP, font=mainfont)
        sleepbutton.grid(row=0, column=2)

        self.radioframe.pack(pady=10)

        # Start and Cancel buttons
        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        self.startbutton = tk.Button(self.buttonframe, text='Start', command=self.start, width=10)
        self.startbutton.grid(row=0, column=0)

        self.cancelbutton = tk.Button(self.buttonframe, text='Cancel', command=self.root.destroy, width=10)
        self.cancelbutton.grid(row=0, column=1)

        self.buttonframe.pack(padx=10, pady=10, side=tk.RIGHT)

        # Keyboard commands
        self.root.bind('<Return>', self.enter_key_function)
        self.root.bind('<Escape>', self.esc_key_function)

    @staticmethod
    def genericerror() -> None:
        """Generic error message incase anything goes wrong"""
        messagebox.showinfo('Error', 'Something went wrong. Please try again')

    def start(self) -> None:
        """Start button function"""
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

        try:
            seconds = int(self.secondsentry.get() or 0)
        except ValueError:
            secondslabeltext = self.secondslabel
            messagebox.showinfo('Error', f'Please input an integer in the \'{secondslabeltext}\' entry')
            return

        totalseconds = hours*3600 + minutes*60 + seconds

        # Check if user inputted values greater than 0
        if totalseconds <= 0:
            messagebox.showinfo('Error', 'Please input values greater than 0')
            return

        shutdowntype = self.var.get()  # Get which radiobutton was selected

        self.root.destroy()  # Closes the window

        match shutdowntype:
            case ShutdownTypes.SHUTDOWN:
                shutdown.shutdown(totalseconds)
            case ShutdownTypes.RESTART:
                shutdown.shutdown(totalseconds)
            case ShutdownTypes.SLEEP:
                shutdown.sleep(totalseconds)
            case _:
                self.genericerror()
                return

    def enter_key_function(self, _) -> None:
        self.start()

    def esc_key_function(self, _) -> None:
        self.root.destroy()


def main():
    window = GUI()
    window.root.mainloop()


if __name__ == '__main__':
    main()
