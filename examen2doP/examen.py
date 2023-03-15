from tkinter import Tk, Button, Frame, Label, Entry
from proceso import *

ventana = Tk()
usuario = validacion()
ventana.title("Login")
ventana.geometry("600x400")
ventana.configure(bg='black')

frame= Frame(bg="black")

label= Label(frame, text= "Matricula",bg='black', fg="#FF3399", font="Arial, 30", pady="40")
Nombre_label = Label(frame, text='Nombre',bg='black',fg="white", font="Arial, 16")
nombre= Entry(frame, font="Arial, 16")
apellidoP= Entry(frame, font="Arial, 16")
apellidoP_label= Label(frame, text='Apellido Paterno',bg='black',fg="white", font="Arial, 16")
apellidoM= Entry(frame, font="Arial, 16")
apellidoM_label= Label(frame, text='Apellido Materno',bg='black',fg="white", font="Arial, 16")
apellidoM= Entry(frame, font="Arial, 16")
apellidoM_label= Label(frame, text='Apellido Materno',bg='black',fg="white", font="Arial, 16")
año= Entry(frame, font="Arial, 16")
año_label= Label(frame, text='Fecha de Nacimiento',bg='black',fg="white", font="Arial, 16")
carrera= Entry(frame, font="Arial, 16")
carrea_label= Label(frame, text='Carrera',bg='black',fg="white", font="Arial, 16")

label.grid(row=0, column=0, columnspan=2, sticky="news")
Nombre_label.grid(row=1,column=0)
nombre.grid(row=1,column=1, pady="20")
apellidoP.grid(row=2, column=1, pady="20")
apellidoP_label.grid(row=2,column=0)
apellidoM.grid(row=3, column=1, pady="20")
apellidoM_label.grid(row=3,column=0)
año.grid(row=4, column=1, pady="20")
año_label.grid(row=4,column=0)
carrera.grid(row=5, column=1, pady="20")
carrea_label.grid(row=5,column=0)

def matricula():
    a=nombre.get()
    b=apellidoP.get()
    c=apellidoM.get()
    d= año.get()
    e= carrera.get()
    usuario.matri(a, b, c, d, e)

boton = Button(frame,text="Login", bg="#FF3399", fg="White", command= matricula, font="Arial, 16")
boton.grid(row=6,column=0,columnspan=2,pady="30")

frame.pack()
ventana.mainloop()