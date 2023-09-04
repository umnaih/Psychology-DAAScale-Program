import tkinter as tk

from results import Results
import constants
import answers


class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        v = tk.IntVar()
        v1 = tk.IntVar()
        v2 = tk.IntVar()
        v3 = tk.IntVar()
        v4 = tk.IntVar()
        v5 = tk.IntVar()
        v6 = tk.IntVar()

        tk.Label(self,
                 text="""15) I felt I was close to panic
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=30, pady=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v, value=value).grid(column=value, row=0)

        tk.Label(self,
                 text="""\n16)  I was unable to become enthusiastic about anything
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v1, value=value).grid(column=value, row=1)

        tk.Label(self,
                 text="""\n17) I felt I was not worth much as a person
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v2, value=value).grid(column=value, row=2)

        tk.Label(self,
                 text="""\n18) I felt that I was rather touchy
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v3, value=value).grid(column=value, row=3)

        tk.Label(self,
                 text="""\n19) I was aware of the action of my heart in the absence of physical exertion 
            (e.g. sense of heart rate increase, heart missing a beat)
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v4, value=value).grid(column=value, row=4)

        tk.Label(self,
                 text="""\n20) I felt scared without any good reason
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v5, value=value).grid(column=value, row=5)

        tk.Label(self,
                 text="""\n21) I felt that life was meaningless
        please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v6, value=value).grid(column=value, row=6)

        btnNext = tk.Button(self, text='Next Page',
                            command=lambda: self.q15_q21Calculation(controller, v, v1, v2, v3, v4, v5, v6),
                            font=('Helvetica 15 '))
        btnNext.grid(column=3, row=8)

    def q15_q21Calculation(self, controller, v, v1, v2, v3, v4, v5, v6):
        q15_val = v.get()
        q16_val = v1.get()
        q17_val = v2.get()
        q18_val = v3.get()
        q19_val = v4.get()
        q20_val = v5.get()
        q21_val = v6.get()

        answers.anxietyArray.append(q15_val)
        answers.depressionArray.append(q16_val)
        answers.depressionArray.append(q17_val)
        answers.stressArray.append(q18_val)
        answers.anxietyArray.append(q19_val)
        answers.anxietyArray.append(q20_val)
        answers.depressionArray.append(q21_val)

        controller.show_frame(Results)

