from tkinter import messagebox
import string
import secrets
class validacion:
    def __init__(self):
        self.__nombre = ""
        self.__apellidoP = ""
        self.__apellidoM = ""
        self.__añoN = ""
        self.__carrera = ""
        
    def matri(self, a, b, c, d, e):
        ini = a.split()
        ini2= b.split()
        ini3= c.split()
        ini4= d.split()
        ini5 = e.split()
        random = ''
        for i in ini:
            self.__nombre = self.__nombre+ i[0]
        for i in ini2:
            self.__apellidoP = self.__apellidoP+ i[0]
        for i in ini3:
            self.__apellidoM = self.__apellidoM+ i[0]
        for i in ini4:
            self.__añoN = self.__añoN + i[2] + i[3]
        for i in ini5:
            self.__carrera = self.__carrera + i[0] + i[1] + i[2]
            
        for i in range (3):
            random += ''.join(secrets.choice(string.digits))
            
        message='23'+self.__añoN,self.__nombre.upper()+ self.__apellidoP.upper()+ self.__apellidoM.upper()+ random + self.__carrera.upper()
        messagebox.showinfo('info', message)
        
            
        
        
        