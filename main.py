import tkinter as tk
from tkinter import *
import os
from time import strftime



root = tk.Tk()
root.title("Seu relógio")
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 300)
root.configure(background = "#282a36")


def get_name():
    nome_usuário = os.getlogin()
    name.config(text="Ola, " + nome_usuário)
 
def get_data():
    data_atual = strftime("%a, %d, %b, %Y")
    data.config(text= data_atual)

def get_hora():
    hora_atual = strftime("%H:%M:%S")
    hora.config(text=hora_atual)
    hora.after(1000, get_hora)



tela = tk.Canvas(root, width=600, height=60 ,bg="#282a36", bd=0, highlightthickness=0, relief="ridge" )
tela.pack()
name = Label(root, bg="#282a36", fg="#8e27ea" , font=("Montserrat" , 16))
name.pack()
data = Label(root, bg="#282a36", fg="#8e27ea" , font=("Montserrat" , 14))
data.pack(pady=2)
hora = Label(root, bg="#282a36", fg="#8e27ea" , font=("Montserrat" , 64, "bold"))
hora.pack(pady=2)


get_name()

get_data()

get_hora()



root.mainloop() 










