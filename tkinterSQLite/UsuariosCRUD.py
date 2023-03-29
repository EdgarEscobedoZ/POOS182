from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controladorBD import *

# Instancia: Puente entre los dos archivos
controlador = controladorBD()

#Metodo que usa mi objeto controlador para insertar
def ejectutaInsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varContra.get())
#Funcion que usa mi objeto controlador para buscar 1 usuario
def ejecutarSelectU():
    rsUsu = controlador.consultarUsuario(varBus.get())
    textBus.delete('1.0', END)
    
    #Iteramos el contenido de la consulta y lo guardamos en CADENA 
    for usu in rsUsu:
        cadena = str(usu[0])+' '+usu[1]+ ' '+usu[2] + ' '+ str(usu[3])
    if (rsUsu):
        textBus.insert(INSERT, cadena)
    else:
        messagebox.showinfo('No encontrado', 'Usuario no existe en BD')

ventana = Tk()
ventana.title('CRUD de usuarios')
ventana.geometry('500x300')

panel= ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)

# Pestaña1: Formulario de registro
titulo = Label(pestana1, text='Registro Usuarios', fg='blue', font=('Modern', 18)).pack()

varNom= tk.StringVar()
lblNom= Label(pestana1, text='Nombre: ').pack()
txtNom= Entry(pestana1, textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(pestana1, text='Correo: ').pack()
txtCor= Entry(pestana1, textvariable=varCor).pack()

varContra= tk.StringVar()
lblContra= Label(pestana1, text='Contraseña: ').pack()
txtContra= Entry(pestana1, textvariable=varContra).pack()

btnGuardar= Button(pestana1, text='Guardar usuario', command=ejectutaInsert).pack()

#Pestaña 2: Buscar Usuario

titulo2= Label(pestana2, text='Buscar Usuario', fg='green', font=('Modern', 18)).pack()

varBus= tk.StringVar()
lblid=Label(pestana2,text='Identificador de Usuario:').pack()
txtid= Entry(pestana2,textvariable=varBus).pack()
btnBusqueda= Button(pestana2,text='Buscar', command=ejecutarSelectU).pack()

subBus= Label(pestana2, text='Resgistrado:', fg='blue',font=('Modern', 15)).pack()
textBus= tk.Text(pestana2, width=52, height=5)
textBus.pack()

panel.add(pestana1, text='Agregar usuarios')
panel.add(pestana2, text='Buscar usuario')
panel.add(pestana3, text='Consultar usuarios')
panel.add(pestana4, text='Actualizar usuario')


ventana.mainloop()
