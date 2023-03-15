from tkinter import *
import tkinter as tk
from validar import *

ventana = Tk()


ventana.title("Password")
ventana.geometry("600x400")
ventana.configure(bg='black')

frame= Frame(bg="black")

label= Label(frame, text= "Generador de contraseñas",bg='black', fg="#FF3399", font="Arial, 30", pady="40")

input_label = Label(frame, text='Ingrese la cantidad de caracteres\n(Ej. 10)',bg='black',fg="white", font="Arial, 16")
input= Entry(frame, font="Arial, 16",)
password= Entry(frame, font="Arial, 16")
password_label= Label(frame, text='Contraseña generada',bg='black',fg="white", font="Arial, 16")

label.grid(row=0, column=0, columnspan=2, sticky="news")
input_label.grid(row=1,column=0)

input.grid(row=1,column=1, pady="20")
password.grid(row=3, column=1, pady="20")
password_label.grid(row=3,column=0)

contraseña = generacion()

def generar():
    password.delete(0, tk.END)
    variable = int(input.get())
    contraseña.validarContra(variable)
    a=contraseña.generar()
    password.insert(0, a)   

def verificar():
    contraseña.seguridad()

botonGen = Button(frame,text="Generar", bg="#FF3399", fg="White",command=generar, font="Arial, 16")
botonGen.grid(row=2,column=0,columnspan=2,pady="30")
botonVerificar = Button(frame,text="Verificar seguridad", bg="#FF3399", fg="White",command=verificar, font="Arial, 16")
botonVerificar.grid(row=4,column=0,columnspan=2,pady="30")

frame.pack()
ventana.mainloop()
