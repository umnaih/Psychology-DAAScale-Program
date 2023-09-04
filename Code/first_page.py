import tkinter as tk
from second_page import SecondPage
import constants
import answers

class FirstPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        v = tk.IntVar()
        v1 = tk.IntVar()
        v2 = tk.IntVar()
        v3 = tk.IntVar()
        v4 = tk.IntVar()
        v5 = tk.IntVar()
        v6 = tk.IntVar()

        tk.Label(self, text=""" 1) I found it hard to wind down
    please choose the corresponding answer :                                                                             """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20,pady=15).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v, value=value).grid(column=value, row=0)

        tk.Label(self,
                 text="""\n     2) I was aware of dryness of my mouth
             please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v1, value=value).grid(column=value, row=1)

        tk.Label(self,
                 text="""\n     3) I could not seem to experience any positive feeling at all
            please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v2, value=value).grid(column=value, row=2)

        tk.Label(self,
                 text="""\n     4) experienced breathing difficulty
            (e.g. excessively rapid breathing,breathlessness in the absence of physical exertion)
            please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v3, value=value).grid(column=value, row=3)

        tk.Label(self,
                 text="""\n     5) I found it difficult to work up the initiative to do things
            please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v4, value=value).grid(column=value, row=4)

        tk.Label(self,
                 text="""\n     6) I tended to over-react to situations
            please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v5, value=value).grid(column=value, row=5)

        tk.Label(self,
                 text="""\n     7) I experienced trembling (e.g. in the hands)
            please choose the corresponding answer :                                                                            """,
                 font=('Helvetica 15 '),
                 justify=tk.LEFT,
                 padx=20).grid()

        for (text, value) in constants.values.items():
            tk.Radiobutton(self, text=text, font=('Helvetica 15 '), variable=v6, value=value).grid(column=value, row=6)

        btnNext = tk.Button(self, text='Next Page',
                            command=lambda: self.q1_q7Calculation(controller, v, v1, v2, v3, v4, v5, v6),
                            font=('Helvetica 15 '))
        btnNext.grid(column=3, row=8)

    def q1_q7Calculation(self, controller, v, v1, v2, v3, v4, v5, v6):
        q1_val = v.get()
        q2_val = v1.get()
        q3_val = v2.get()
        q4_val = v3.get()
        q5_val = v4.get()
        q6_val = v5.get()
        q7_val = v6.get()

        answers.stressArray.append(q1_val)
        answers.anxietyArray.append(q2_val)
        answers.depressionArray.append(q3_val)
        answers.anxietyArray.append(q4_val)
        answers.depressionArray.append(q5_val)
        answers.stressArray.append(q6_val)
        answers.anxietyArray.append(q7_val)

        controller.show_frame(SecondPage)
