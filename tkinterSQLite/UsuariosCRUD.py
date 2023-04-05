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
    rsUsu = controlador.buscarUsuario(varBus.get())
    textBus.delete('1.0', END)

    #Iteramos el contenido de la consulta y lo guardamos en CADENA 
    for usu in rsUsu:
        cadena = str(usu[0])+' '+usu[1]+ ' '+usu[2] + ' '+ str(usu[3])
    if (rsUsu):
        textBus.insert(INSERT, cadena)
    else:
        messagebox.showinfo('No encontrado', 'Usuario no existe en BD')

def ejecutarSelectU2():
    rsUsuario = controlador.buscarUsuario(varElim.get())
    tree2.delete(*tree2.get_children())

    #Iteramos el contenido de la consulta y lo guardamos en CADENA 
    for usu in rsUsuario:
        cadena = tree2.insert('',tk.END, values=usu)
    if (rsUsuario):
        textBus.insert(INSERT, cadena)
    else:
        messagebox.showinfo('No encontrado', 'Usuario no existe en BD')
        
def ejecutarConsul():
    rsConsul = controlador.consultarUsuario()
    tree.delete(*tree.get_children())
    for fila in rsConsul:
        tree.insert('',tk.END, values=fila)

def ejecutarModi():
    rsConsul = controlador.consultarUsuario()
    tree.delete(*tree.get_children())
    for fila in rsConsul:
        tree.insert('',tk.END, values=fila)

def ejecutarEliminarU():
    #Iteramos el contenido de la consulta y lo guardamos en CADENA 
    ask = messagebox.askyesno('Pregunta', '¿Seguro que quiere eliminar el usuario?')
    if ask == True:
        controlador.eliminarUsuario(varElim.get())
        tree2.delete(*tree2.get_children())
        messagebox.showinfo('Info', 'Usuario Eliminado')
    else:
        messagebox.showerror('Error', 'Usuario no Eliminado')

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
txtContra= Entry(pestana1, textvariable=varContra, show='*').pack()

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

#Pestaña 3: Consultar Usuario
titulo3 = Label(pestana3, text='Consultar Usuarios', fg = 'purple', font=('Modern', 18)).pack()
tree = ttk.Treeview(pestana3, column=("c1", "c2", "c3", 'c4'), show='headings')

tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="ID")

tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Nombre")

tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Correo")

tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="Contra")

tree.pack()
btnConsul= Button(pestana3,text='Consultar', command=ejecutarConsul).pack()

#Pestaña 4
titulo3 = Label(pestana4, text='Actualizar Usuarios', fg = 'black', font=('Modern', 18)).pack()

varElim= tk.StringVar()
lblP4=Label(pestana4,text='Identificador de Usuario:').pack()
txtP4= Entry(pestana4,textvariable=varElim).pack()
btnBusqueda= Button(pestana4,text='Buscar', command=ejecutarSelectU2).pack()
btnElim= Button(pestana4,text='Eliminar', command=ejecutarEliminarU).pack()

tree2 = ttk.Treeview(pestana4, column=("c1", "c2", "c3", 'c4'), show='headings')

tree2.column("#1", anchor=tk.CENTER)
tree2.heading("#1", text="ID")

tree2.column("#2", anchor=tk.CENTER)
tree2.heading("#2", text="Nombre")

tree2.column("#3", anchor=tk.CENTER)
tree2.heading("#3", text="Correo")

tree2.column("#4", anchor=tk.CENTER)
tree2.heading("#4", text="Contra")

tree2.pack()

panel.add(pestana1, text='Agregar usuarios')
panel.add(pestana2, text='Buscar usuario')
panel.add(pestana3, text='Consultar usuarios')
panel.add(pestana4, text='Actualizar usuario')


ventana.mainloop()
