import tkinter as tk
from subprocess import run


class MyGUI:
    def __init__(self):

        mainfont = ('Arial', 10)

        self.root = tk.Tk()
        self.root.geometry()
        self.root.title('Shutdown timer')

        self.entryframe = tk.Frame(self.root)
        self.entryframe.rowconfigure(0, pad=10, weight=1)
        self.entryframe.rowconfigure(1, pad=10, weight=1)
        self.entryframe.columnconfigure(0, pad=10, weight=1)
        self.entryframe.columnconfigure(1, pad=10, weight=1)

        hourslabel = tk.Label(self.entryframe, text='Hours:', font=mainfont)
        hourslabel.grid(row=0, column=0, padx=(0, 10), sticky='e')

        self.hoursentry = tk.Entry(self.entryframe, font=mainfont)
        self.hoursentry.grid(row=0, column=1, padx=(0,10), sticky='ew')
        self.hoursentry.focus_set()

        minuteslabel = tk.Label(self.entryframe, text='Minutes:', font=mainfont)
        minuteslabel.grid(row=1, column=0, padx=(0, 10), sticky='e')

        self.minutesentry = tk.Entry(self.entryframe, font=mainfont, width=10)
        self.minutesentry.grid(row=1, column=1, padx=(0,10), sticky='ew')

        self.entryframe.pack(padx=10, pady=10)

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

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        self.startbutton = tk.Button(self.buttonframe, text='Start', command=self.start, width=10)
        self.startbutton.grid(row=0, column=0)

        self.cancelbutton = tk.Button(self.buttonframe, text='Cancel', command=self.cancel, width=10)
        self.cancelbutton.grid(row=0, column=1)

        self.buttonframe.pack(padx=10, pady=10, side=tk.RIGHT)

    def display(self):
        self.root.mainloop()

    def start(self):
        hours = int(self.hoursentry.get() or 0)
        minutes = int(self.minutesentry.get() or 0)
        totalseconds = (hours * 3600) + (minutes * 60)

        shutdowntype = self.restartvar.get()
        shutdowntags = {'shutdown': '-s', 'restart': '-r'}
        tag = shutdowntags[shutdowntype]

        command = f'shutdown {tag} -t {totalseconds}'
        run(command)
        self.root.quit()

    def cancel(self):
        self.root.quit()


window = MyGUI()
window.display()
