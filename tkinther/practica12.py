from tkinter import Tk, Button, Frame, messagebox, Label, Entry
from validar import *

ventana = Tk()
usuario = validacion()
ventana.title("Login")
ventana.geometry("600x400")
ventana.configure(bg='black')

frame= Frame(bg="black")

label= Label(frame, text= "Login",bg='black', fg="#FF3399", font="Arial, 30", pady="40")
user_label = Label(frame, text='Username',bg='black',fg="white", font="Arial, 16")
user= Entry(frame, font="Arial, 16")
password= Entry(frame, font="Arial, 16")
password_label= Label(frame, text='Password',bg='black',fg="white", font="Arial, 16")

label.grid(row=0, column=0, columnspan=2, sticky="news")
user_label.grid(row=1,column=0)
user.grid(row=1,column=1, pady="20")
password.grid(row=2, column=1, pady="20")
password_label.grid(row=2,column=0)

def login():
        username = user.get()
        contra = password.get()
        if usuario.validar(username, contra):
            messagebox.showinfo('Login', 'Usuario correcto')
        else:
            messagebox.showinfo('Login', 'Usuario incorrecto')

botonLogin = Button(frame,text="Login", bg="#FF3399", fg="White", command= login, font="Arial, 16")
botonLogin.grid(row=3,column=0,columnspan=2,pady="30")

frame.pack()
ventana.mainloop()

