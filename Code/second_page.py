import tkinter as tk

from third_page import ThirdPage
import constants
import answers

class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        v = tk.IntVar()
        v1 = tk.IntVar()
        v2 = tk.IntVar()
        v3 = tk.IntVar()
        v4 = tk.IntVar()
        v5 = tk.IntVar()
        v6 = tk.IntVar()

        tk.Label(self, text="""8) I felt that I was using a lot of nervous energy
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=35, pady=25).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v, value=value).grid(column=value, row=0)

        tk.Label(self,
                 text="""\n9)  I was worried about situations in which I might panic and make a fool of myself
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v1, value=value).grid(column=value, row=1)

        tk.Label(self,
                 text="""\n10) I felt that I had nothing to look forward to 
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v2, value=value).grid(column=value, row=2)

        tk.Label(self,
                 text="""\n11) I found myself getting agitated
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v3, value=value).grid(column=value, row=3)

        tk.Label(self,
                 text="""\n12) I found it difficult to relax
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v4, value=value).grid(column=value, row=4)

        tk.Label(self,
                 text="""\n13) I felt down-hearted and blue
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v5, value=value).grid(column=value, row=5)

        tk.Label(self,
                 text="""\n14) I was intolerant of anything that kept me from getting on with what I was doing
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v6, value=value).grid(column=value, row=6)

        btnNext = tk.Button(self, text='Next Page',
                            command=lambda: self.q8_q14Calculation(controller, v, v1, v2, v3, v4, v5, v6),
                            font=('Helvetica 15 '))
        btnNext.grid(column=3, row=8)

    def q8_q14Calculation(self, controller, v, v1, v2, v3, v4, v5, v6):
        q8_val = v.get()
        q9_val = v1.get()
        q10_val = v2.get()
        q11_val = v3.get()
        q12_val = v4.get()
        q13_val = v5.get()
        q14_val = v6.get()

        answers.stressArray.append(q8_val)
        answers.anxietyArray.append(q9_val)
        answers.depressionArray.append(q10_val)
        answers.stressArray.append(q11_val)
        answers.stressArray.append(q12_val)
        answers.depressionArray.append(q13_val)
        answers.stressArray.append(q14_val)

        controller.show_frame(ThirdPage)