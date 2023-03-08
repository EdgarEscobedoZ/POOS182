from tkinter import *
from validar import *

ventana = Tk()


ventana.title("Password")
ventana.geometry("600x400")
ventana.configure(bg='black')

frame= Frame(bg="black")

label= Label(frame, text= "Generador de contraseñas",bg='black', fg="#FF3399", font="Arial, 30", pady="40")
input_label = Label(frame, text='Ingrese la cantidad de caracteres',bg='black',fg="white", font="Arial, 16")
input= Entry(frame, font="Arial, 16",)
password= Entry(frame, font="Arial, 16")
password_label= Label(frame, text='Contraseña generada',bg='black',fg="white", font="Arial, 16")

label.grid(row=0, column=0, columnspan=2, sticky="news")
input_label.grid(row=1,column=0)
input.grid(row=1,column=1, pady="20")
password.grid(row=3, column=1, pady="20")
password_label.grid(row=3,column=0)

def login():
    variable = int(input.get())
    contraseña = generacion(variable)
    a=contraseña.generar(variable)
    password.insert(0, a)        

botonLogin = Button(frame,text="Generar", bg="#FF3399", fg="White",command=login, font="Arial, 16")
botonLogin.grid(row=2,column=0,columnspan=2,pady="30")

frame.pack()
ventana.mainloop()
