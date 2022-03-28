import tkinter as tk
from tkinter.font import BOLD
import qrgenerator as gen

CANVA_SIZE = 600
CANVA_HALF_SIZE = CANVA_SIZE/2
FONT = 'grey50'

def setWindow():
    global win
    
    win = tk.Tk()
    win.title("QR Code Generator")
    win.geometry("1020x620")
    win.configure(bg=FONT) 
    win.resizable(width=False, height=False)

    f1 = tk.font.Font(size=20)
    f2 = tk.font.Font(size=18)

    tex1 = tk.Label(win, text='QR CODE GENERATOR', bg=FONT, anchor=tk.N)
    tex1['font'] = f1
    tex1.grid(row=0, columnspan=2)

    tex2 = tk.Label(win, text='by Alexis BONAMY', bg=FONT, anchor=tk.N)
    tex2['font'] = f2
    tex2.grid(row=1, sticky=tk.N, columnspan=2)



def setEntry():
    global win, entr_data

    label_data = tk.Label(win, text='Données à stocker :', bg=FONT)
    label_data.grid(row=2, sticky=tk.N, columnspan=2)

    entr_data = tk.Entry(win, width=60, relief=tk.GROOVE)
    entr_data.grid(row=2, columnspan=2, padx=10)


def setQuitButton():
    global win

    f = tk.font.Font(size=12)

    but_quit = tk.Button(win, text='Quitter', width=20, height=5, background='grey40', relief=tk.GROOVE, command=win.destroy)
    but_quit['font'] = f
    but_quit.grid(row=3, column=1, sticky=tk.S, padx=5, pady=10)


def setCreateButton():
    global win

    f = tk.font.Font(size=12)

    but_create = tk.Button(win, text='Créer', width=20, height=5, background='grey40', relief=tk.GROOVE, command=reload)
    but_create['font'] = f
    but_create.grid(row=3, column=0, sticky=tk.S, padx=5, pady=10)


def setQRZone():
    global win, can

    can = tk.Canvas(win, width=CANVA_SIZE, height=CANVA_SIZE, bg='grey30')
    image = tk.PhotoImage(file='qrcode.png')
    item = can.create_image(CANVA_HALF_SIZE, CANVA_HALF_SIZE, image=image)
    can.grid(row=0, column=2, rowspan=4, padx=10, pady=10)

    win.mainloop()




def reload():
    global can, entr_data
    can.delete('ALL')

    gen.generate(entr_data.get())

    setQRZone()