from tkinter import *
import tkinter as tk
from tkinter import filedialog
import main

root = Tk()
root.title("projet ACP")
root.geometry("800x200")
url = None
x = ''
norme = tk.IntVar()
n_norme = tk.IntVar()
def open_file ():
    global url
    url = filedialog.askopenfilename(title= "open csv file", filetypes = (("csv files", "*.csv"),))
    lab.config(text = "le lien est :"+ str(url))

def lancer():
    global url
    if url == None or url == '':
        lab.config(text = "vous devez choisir le data set puis lancer le programme")
    else:
        if norme.get() == 1:
            main.main(url, True)
        else:
            main.main(url, False)




button = Button(root, text = "open file", command = open_file)
button.pack()

lanceur = Button(root, text = "lancer le programme", command = lancer)
lanceur.pack()

lab = Label(root, text = x)
lab.pack()


norme_button =  tk.Checkbutton(root, text='Normé',variable=norme, onvalue=1, offvalue=0)
norme_button.pack()

n_norme_button = tk.Checkbutton(root, text='Non Normé',variable=n_norme, onvalue=1, offvalue=0)

n_norme_button.pack()
root.mainloop()
