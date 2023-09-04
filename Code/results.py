import tkinter as tk
import welcome
import answers

class Results(tk.Frame):
    def show_result(self):

        depressionResult, anxietyResult, stressResult = self.calculateResults()
        result = stressResult + "\n" + anxietyResult + "\n" + depressionResult

        resultLabel = tk.Label(self, text=result,font=('Helvetica 18 bold'))

        resultLabel.pack(padx=20, pady=20)
        result_shown = True

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self)

        label = tk.Label(self,
                         text="\nResults\n                                                                 ",
                         font=('Helvetica 40 bold'))

        label.pack(padx=280, pady=120)
        label.config(width=0, height=5)
        buttonGetResult = tk.Button(self, text="Get Result", font=('Helvetica 15 bold'),
                                    command=lambda: self.show_result(), bg="Beige", height=0, width=10)
        buttonGetResult.pack()


    def calculateResults(self):

        sumDepression = answers.calculateSum(answers.depressionArray)
        sumAnxiety = answers.calculateSum(answers.anxietyArray)
        sumstress = answers.calculateSum(answers.stressArray)

        DepressionResult = ''
        AnxietyResult = ''
        StressResult = ''

        if sumAnxiety >= 0 and sumAnxiety <= 13:
            AnxietyResult = "Your score indicates that you are experiencing minimal anxiety."
        elif sumAnxiety >= 14 and sumAnxiety <= 16:
            AnxietyResult = "Your score indicates that you are experiencing mild anxiety."
        elif sumAnxiety >= 17 and sumAnxiety <= 28:
            AnxietyResult = "Your score indicates that you are experiencing moderate anxiety "
        elif sumAnxiety >= 29 and sumAnxiety <= 34:
            AnxietyResult = "Your score indicates that you are experiencing sever anxiety "
        else:
            AnxietyResult = "Your score indicates that you are experiencing extremely severe anxiety "

        if sumstress >= 0 and sumstress <= 28:
            StressResult = "Your score indicates that you are experiencing minimal stress."
        elif sumstress >= 29 and sumstress <= 34:
            StressResult = "Your score indicates that you are experiencing mild stress."
        elif sumstress >= 35 and sumstress <= 38:
            StressResult = "Your score indicates that you are experiencing moderate stress "
        elif sumstress >= 38 and sumstress <= 44:
            StressResult = "Your score indicates that you are experiencing sever stress "
        else:
            StressResult = "Your score indicates that you are experiencing extremely severe stress "

        if sumDepression >= 0 and sumDepression <= 16:
            DepressionResult = "Your score indicates that you are experiencing minimal depression."
        elif sumDepression >= 17 and sumDepression <= 19:
            DepressionResult = "Your score indicates that you are experiencing mild depression."
        elif sumDepression >= 20 and sumDepression <= 22:
            DepressionResult = "Your score indicates that you are experiencing moderate depression "
        elif sumDepression >= 23 and sumDepression <= 27:
            DepressionResult = "Your score indicates that you are experiencing sever depression "
        else:
            DepressionResult = "Your score indicates that you are experiencing extremely severe depression "

        return DepressionResult, AnxietyResult, StressResult





