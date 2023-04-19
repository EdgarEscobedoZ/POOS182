from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controladorFerreteria import *

controlador = controladorBD()

def ejectutaInsert():
    controlador.guardarUsuario(varMat.get(), varCant.get())
    varMat.set('')
    varCant.set('')
def ejecutarSelectU3():
    rsUsuario = controlador.buscarRegistro(varAct.get())
    varNom1.set('')
    varCor1.set('')
    if (rsUsuario):
        for usu in rsUsuario:
            varNom1.set(usu[1])
            varCor1.set(usu[2])
    else:
        messagebox.showinfo('No encontrado', 'Usuario no existe en BD')
        
def ejecutarModi():
    messagebox.askyesno('Confirmación','¿Seguro que quiere actualizar esta información?')
    controlador.actualizarRegistro(varAct.get(), varNom1.get(), varCor1.get())
    varAct.set('')
    varNom1.set('')
    varCor1.set('')
    
def ejecutarConsul():
    rsConsul = controlador.consultarUsuario()
    tree.delete(*tree.get_children())
    for fila in rsConsul:
        tree.insert('',tk.END, values=fila)

ventana = Tk()
ventana.title('BD Ferretería')
ventana.geometry('500x300')

panel= ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)

#Agregar Usuarios
titulo = Label(pestana1, text='Registro Materiales', fg='blue', font=('Modern', 18)).pack()

varMat= tk.StringVar()
lblMat= Label(pestana1, text='Material: ').pack()
txtMat= Entry(pestana1, textvariable=varMat).pack()

varCant= tk.StringVar()
lblCant= Label(pestana1, text='Cantidad: ').pack()
txtCant= Entry(pestana1, textvariable=varCant).pack()

btnGuardar= Button(pestana1, text='Guardar registro', command=ejectutaInsert).pack()

#Actualizar Usuarios
titulo2 = Label(pestana2, text='Actualizar Usuarios', fg = 'black', font=('Modern', 18)).pack()

varAct= tk.StringVar()
lblP2=Label(pestana2,text='Identificador de Registro:').pack()
txtP2= Entry(pestana2,textvariable=varAct).pack()

btnBusqueda= Button(pestana2,text='Buscar', command=ejecutarSelectU3).pack()

varNom1= tk.StringVar()
lblNom1= Label(pestana2, text='Material: ').pack()
txtNom1= Entry(pestana2, textvariable=varNom1).pack()

varCor1= tk.StringVar()
lblCor1= Label(pestana2, text='Cantidad: ').pack()
txtCor1= Entry(pestana2, textvariable=varCor1).pack()


btnAct= Button(pestana2,text='Actualizar', command=ejecutarModi).pack()

#Consultar Registros
titulo3 = Label(pestana3, text='Consultar Registros', fg = 'purple', font=('Modern', 18)).pack()
tree = ttk.Treeview(pestana3, column=("c1", "c2", "c3"), show='headings')

tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="ID")

tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Material")

tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Cantidad")

tree.pack()

btnConsul= Button(pestana3,text='Consultar', command=ejecutarConsul).pack()



panel.add(pestana1, text='Agregar Registro')
panel.add(pestana2, text='Actualizar Registro')
panel.add(pestana3, text='Consultar Registros')

ventana.mainloop()