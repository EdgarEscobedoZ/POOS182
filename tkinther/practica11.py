from tkinter import Tk, Button, Frame, messagebox

#5. agregar funcion de mensaje
def mostrarMensaje():
    messagebox.showinfo("Información", "Te informo que todo fallo con exito")
    messagebox.showerror('Error','Perdon te falle!!')
    print(messagebox.askokcancel('Pregunta', '¿Seguro que quieres guardar algo?'))
    #print(messagebox.askquestion('Pregunta',"probando"))
    #print(messagebox.askretrycancel('Pregunta',"probando"))
    #print(messagebox.askyesno('Pregunta',"probando"))

#6. Funcion agregar botones
def agregarBoton():
    botonVerde.config(text="+", bg="green", fg="white")
    botonNuevo= Button(seccion3, text="Boton Nuevo")
    botonNuevo.pack()

#1. Generar una ventana
ventana = Tk()
ventana.title("Ejemplo 3 frames")
ventana.geometry("600x400")


#2. Agregar Frames
seccion1 = Frame(ventana,bg="red")
seccion1.pack(expand=True, fill='both')

seccion2 = Frame(ventana,bg="grey")
seccion2.pack(expand=True, fill='both')

seccion3 = Frame(ventana, bg="purple")
seccion3.pack(expand=True, fill='both')

#3. Agregamos botones 
botonAzul= Button(seccion1, text="boton azul", fg="blue", bg="#73a9fa", command=mostrarMensaje)
botonAzul.place(x=60,y=60, width= 100, height= 60)

botonAmarillo= Button(seccion2, text="boton Amarillo", bg="#f4fa73", fg="red")
botonAmarillo.grid(row=1, column=1)

botonNegro= Button(seccion2, text="boton Negro", bg="#1a1b16", fg="White")
botonNegro.grid(row = 0, column =0)

botonVerde= Button(seccion3, text="boton Verde", bg="#74fa87", fg="White", command=agregarBoton)
botonVerde.pack()

#4. Posicionamiento de los Widgets

#Metodo Main para la ejecucion de la ventana
ventana.mainloop()