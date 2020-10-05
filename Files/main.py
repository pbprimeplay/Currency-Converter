#Made by Pradyun Beerla
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

currencyNames = []
#Reading the lines of the data file
with open("Assets/conversionData.txt") as f:
	lines = f.readlines()

currencyDict = {}
#Storing the data in a python dictionary
for line in lines:
	parsed = line.split("\t")
	currencyDict[parsed[0]] = parsed[1]

#Appending names of currencies to a list
for names in currencyDict.keys():
	currencyNames.append(names)

#Creating and formatting the tkinter GUI
root = Tk()
root.title("Currency Converter")
root.geometry('345x180')
root.iconbitmap("Assets/ProgramIcon.ico")
root.resizable(False, False)

#Initialising answer output label beforhand
answer = Label(root, fg="green")

#String Variables for the ttk combobox dropdown element
variable1 = StringVar(root)
variable1.set("Select Currency")

variable2 = StringVar(root)
variable2.set("Select Currency")

#Creating a function which converts values
def convert(conval1, conval2, amount):
	#Formulating the final value
	converted = float(amount)/float(currencyDict[conval1]) * float(currencyDict[conval2])
	#Rounding it upto only 2 decimal places
	conv = f"{converted:.2f}"
	formatted = conv+' '+conval2 + 's'

	answer.place_forget()

	answer.config(text=formatted)
	answer.place(x=180, y=155, anchor="center")

#Title labels
titleText = Label(root, text='Currency Converter', bg='white', fg="black")
titleText.place(x=120, y=5)

#Extra fonts
fontStyle1 = tkFont.Font(titleText, titleText.cget("font"))
fontStyle1.configure(underline = True)
fontStyle2 = tkFont.Font(size=30)

#Adding Font Styles to title
titleText.config(font=fontStyle1)

#First currency dropdown combobox
currency1 = ttk.Combobox(root, textvariable=variable1, values=currencyNames)
currency1.place(x=10, y=40)

to = Label(root, text="↠", font=fontStyle2, fg='red')
to.place(x=160, y=26)

#Second currency dropdown combobox
currency2 = ttk.Combobox(root, textvariable=variable2, values=currencyNames)
currency2.place(x=190, y=40)

#Amount entry input
moneyVal = Entry(root)
moneyVal.place(x=110, y=80)

#Enter/Submission button
enter = Button(root, text="Enter", command=lambda: convert(currency1.get(), currency2.get(), moneyVal.get())
enter.place(x=150, y=110)

#Mainloop
root.mainloop()
