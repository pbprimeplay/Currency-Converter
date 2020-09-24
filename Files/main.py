#Made by Pradyun Beerla
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

items = []
with open("Assets/conversionData.txt") as f:
	lines = f.readlines()

currencyDict = {}
for line in lines:
	parsed = line.split("\t")
	currencyDict[parsed[0]] = parsed[1]

for names in currencyDict.keys():
	items.append(names)

root = Tk()
root.title("Currency Converter")
root.geometry('345x180')
root.iconbitmap("Assets/ProgramIcon.ico")
root.resizable(False, False)

answer = Label(root)
answer.place(x=120, y=145)

variable1 = StringVar(root)
variable1.set("Select Currency")

variable2 = StringVar(root)
variable2.set("Select Currency")

def convert():
	conval1 = currency1.get()
	conval2 = currency2.get()
	converted = float(moneyVal.get())/float(currencyDict[conval1]) * float(currencyDict[conval2])
	conv = f"{converted:.2f}"
	formatted = conv+' '+conval2 + 's'

	answer.place_forget()

	answer.config(text=formatted, fg="green")
	answer.place(x=120, y=145)

titleText = Label(root, text='Currency Converter', bg='white', fg="black")
titleText.place(x=120, y=5)
fontStyle1 = tkFont.Font(titleText, titleText.cget("font"))
fontStyle1.configure(underline = True)
titleText.config(font=fontStyle1)

currency1 = ttk.Combobox(root, textvariable=variable1, values=items)
currency1.place(x=10, y=40)

fontStyle2 = tkFont.Font(size=30)
to = Label(root, text="↠", font=fontStyle2, fg='red')
to.place(x=160, y=26)

currency2 = ttk.Combobox(root, textvariable=variable2, values=items)
currency2.place(x=190, y=40)

moneyVal = Entry(root)
moneyVal.place(x=110, y=80)

enter = Button(root, text="Enter", command=convert)
enter.place(x=150, y=110)

root.mainloop()
