from tkinter import *

root = Tk()
address = r"C:\Users\C605\Desktop\marvel.txt"
root.geometry("700x700")
Output = Text(root, height=100, width=100, bg="light cyan")


def readFile():
    Output.delete("1.0", 'end-1c')
    f = open(address)
    x = f.read()
    x.split()
    Output.insert(END, x)
    Output.pack()


def calculateFreqs():
    Output.delete("1.0", 'end-1c')
    f = open(address)
    x = f.read()
    x = x.split()
    x2 = []
    for i in x:
        if i not in x2:
            x2.append(i)
    for i in range(0, len(x2)):
        str = 'Frequency of {} is : {}\n'.format(x2[i], x.count(x2[i]))
        Output.insert(END, str)
    Output.pack()


button1 = Button(root, text="READ", command=readFile)
button1.pack()
button2 = Button(root, text="CALCULATE", command=calculateFreqs)
button2.pack()

root.mainloop()
