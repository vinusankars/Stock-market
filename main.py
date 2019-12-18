from StockValue import Data
import tkinter
from tkinter import messagebox as tkMessageBox

data=Data()
data.collect()

def print_data() :

    data.collect()
    s = ''
    for i in data.world_market :
        s += i + ' - ' + str(data.world_market[i]) + '\n'
    tkMessageBox.showinfo('World Market',s)
                   

def print_curr() :

    data.collect()
    s = ''
    for i in data.currencies :
        s += i + ' - ' + str(data.currencies[i]) + '\n'
    tkMessageBox.showinfo('Currency',s)  

window = tkinter.Tk()
window.title('Stock Market')
window.geometry('500x600')
window.wm_iconbitmap('vss.ico')
window.configure(background = "#aaaaff")

currency = tkinter.Button(window, text = 'Currency', command = print_curr)
market =  tkinter.Button(window, text = 'Market', command = print_data)

currency.pack()
market.pack()
window.mainloop()
