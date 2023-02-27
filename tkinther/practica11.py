from tkinter import Tk, Button, Frame

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
botonAzul= Button(seccion1, text="boton azul", fg="blue")
botonAzul.place(x=60,y=60, width= 100, height= 60)

botonAmarillo= Button(seccion2, text="boton Amarillo", bg="yellow", fg="red")
botonAmarillo.grid(row=1, column=1)

botonNegro= Button(seccion2, text="boton Negro", bg="black", fg="White")
botonNegro.grid(row = 0, column =0)

botonVerde= Button(seccion3, text="boton Verde", bg="green", fg="White")
botonVerde.pack()

ventana.mainloop()