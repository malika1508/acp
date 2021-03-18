from tkinter import *
from tkinter import filedialog
import main

root = Tk()
root.title("projet ACP")
root.geometry("800x200")
url = None
x = ''
def open_file ():
    global url
    url = filedialog.askopenfilename(title= "open csv file", filetypes = (("csv files", "*.csv"),))
    lab.config(text = "le lien est :"+ str(url))

def lancer():
    global url
    if url == None or url == '':
        lab.config(text = "vous devez choisir le data set puis lancer le programme")
    else:
        main.main(url)



button = Button(root, text = "open file", command = open_file)
button.pack()

lanceur = Button(root, text = "lancer le programme", command = lancer)
lanceur.pack()

lab = Label(root, text = x)
lab.pack()

root.mainloop()
