import tkinter as tk
from welcome import Welcome
from first_page import FirstPage
from second_page import SecondPage
from third_page import ThirdPage
from results import Results


class Main(tk.Tk):
    def __init__(self, * args, **kwargs):
        tk.Tk.__init__(self, * args, **kwargs)
        container = tk.Frame(self)

        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Welcome, FirstPage, SecondPage, ThirdPage, Results):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=4, column=5)

        self.show_frame(Welcome)

    def show_frame(self, cont):
      frame = self.frames[cont]
      frame.tkraise()

app= Main()
app.mainloop()