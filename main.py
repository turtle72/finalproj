import tkinter as tk
import datetime

name = ''
password = ''

window = tk.Tk()
window.geometry("600x600")
IsNewACC = False

def getInf():
    name = userNameB.get()
    password = passwordNameB.get()
    print(name)

def cBoard():
    for widgets in window.winfo_children():
        widgets.destroy()

def nAccGUI():
    cBoard()

def nBoard():
    userName.pack()
    userNameB.pack()
    passwordName.pack()
    passwordNameB.pack()
    enterInf.pack()

def makeacc(u,p,l):
    with open(f'/users/{u}', 'r+') as file:
        file.write(f'{u}#{p}#{datetime.date.today()}#{l}')
    
userName = tk.Label(text='Username:')
userNameB = tk.Entry()

passwordName = tk.Label(text='Password:')
passwordNameB = tk.Entry()

enterInf = tk.Button(text='Enter Information', command=getInf)
 
newAccount = tk.Button(text='New Account', command=cBoard)










userName.pack()
userNameB.pack()
passwordName.pack()
passwordNameB.pack()
enterInf.pack()
newAccount.pack()

window.mainloop()