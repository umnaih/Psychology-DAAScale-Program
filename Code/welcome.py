import tkinter as tk

from first_page import FirstPage

class Welcome(tk.Frame):
     def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent) #the start is the parent
         self.winfo_toplevel().title("DASS program")
         label = tk.Label(self, text='''Please read each statement and select the choice which
                 indicates how much statement applies to you over the past week.
There are no right or wrong answers. 
         Do not spend too much time on any statement.               ''',font=('Helvetica 20 bold'))
         label.pack(padx=280, pady=210)
         buttonStart = tk.Button(self, text="Start", font=('Helvetica 15 bold'),
                                 command=lambda:controller.show_frame(FirstPage) ,bg="Beige", height=0, width=10)
         buttonStart.pack()