from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import time
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.exact import solve_tsp_brute_force
from python_tsp.heuristics import solve_tsp_local_search
distance_matrix = np.array([
    [0,  10, 11, 12, 13, 14],
    [10,  0, 15,  16, 17, 18],
    [11,  15, 0,  19, 20, 21],
    [12, 16, 19, 0, 22, 23],
    [13, 17, 20, 22, 0, 24],
    [14, 18, 21, 23, 24, 0]

])
def click1():
    newWindow = Toplevel(master)
    newWindow.title("Heuristique vue en cours")
    newWindow.geometry("900x750")
    newWindow.resizable(False, False)
    load = Image.open("demo.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(newWindow, image=render)
    img.image = render
    img.pack()
    start = time.time()
    permutation, distance = solve_tsp_local_search(distance_matrix)
    end = time.time()
    elapsed = end - start
    for i in range(len(permutation)):
        permutation[i]+=1
    Label(newWindow, text=f"Le cycle hamiltonien approché est :  {permutation}", font=('Arial', 20, 'bold')).pack()
    Label(newWindow, text=f"La distance approché = {distance}", font=('Arial', 20, 'bold')).pack()
    Label(newWindow, text=f"Le temps d'execution = {elapsed:.20} ms", font=('Arial', 20, 'bold')).pack()

def click2():
    newWindow = Toplevel(master)
    newWindow.title("Methode exacte")
    newWindow.geometry("900x750")
    newWindow.resizable(False, False)
    load = Image.open("demo.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(newWindow, image=render)
    img.image = render
    img.pack()
    start = time.time()
    permutation, distance = solve_tsp_brute_force(distance_matrix)
    end = time.time()
    elapsed = end - start
    for i in range(len(permutation)):
        permutation[i]+=1
    Label(newWindow, text=f"Le cycle hamiltonien de cout minimal est :  {permutation}", font=('Arial', 20, 'bold')).pack()
    Label(newWindow, text=f"La distance optimale = {distance}", font=('Arial', 20, 'bold')).pack()
    Label(newWindow, text=f"Le temps d'execution = {elapsed:.20} ms", font=('Arial', 20, 'bold')).pack()

master = Tk()
master.geometry('600x500')
master.title("TP4 TPGO")
master.resizable(False, False)
Label(master, text="Probleme du voyageur de commerce", font=('Arial', 20, 'bold')).pack()
st = Style()
st.configure('W.TButton', background='#345', foreground='black', font=('Arial', 14))
load = Image.open("voyageur.jpg")
render = ImageTk.PhotoImage(load)
img = Label(master, image=render)
img.image = render
img.pack()
Button(master, text='Heuristique vue en cours', style='W.TButton', command=click1).pack()
Button(master, text='Methode exacte', style='W.TButton', command=click2).pack()
Button(master, text='Quitter', style='W.TButton', command=master.destroy).pack()
master.mainloop()
