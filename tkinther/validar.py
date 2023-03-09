from tkinter import messagebox
import string
import secrets
class validacion:
    
    def __init__ (self):
        self.__usuario = "pepe"
        self.__contraseña = "1234"
    
    def validar(self,user, contra):
        return user == self.__usuario and contra == self.__contraseña
    
    
    
class generacion:
    def __init__ (self):
        self.__caracteres = 8
        self.__especial = False
        self.__mayusculas = False
        
    def validarContra(self, a):
        if a>8:
            self.__caracteres=a
        else:
            self.__caracteres = 8
        
    def generar(self):
        minusculas = string.ascii_lowercase
        caracteres_esp = string.punctuation
        letras = string.ascii_letters
        contraseña = ''
        self.__especial = messagebox.askyesno('Caracteres especiales','¿Desea usar caracteres especiales en su contraseña?')
        self.__mayusculas = messagebox.askyesno('Mayusculas','¿Desea usar mayusuclas en su contraseña?')
        
        if self.__especial==True and self.__mayusculas == True:
            alfabeto = caracteres_esp + letras
            for i in range (self.__caracteres):
                contraseña+=''.join(secrets.choice(alfabeto))
            return contraseña
        if self.__especial==False and self.__mayusculas == True:
            alfabeto = letras
            for i in range (self.__caracteres):
                contraseña+=''.join(secrets.choice(alfabeto))
            return contraseña
        if self.__especial==True and self.__mayusculas == False:
            alfabeto = caracteres_esp + minusculas
            for i in range (self.__caracteres):
                contraseña+=''.join(secrets.choice(alfabeto))
            return contraseña
        if self.__especial==False and self.__mayusculas == False:
            alfabeto = minusculas
            for i in range (self.__caracteres):
                contraseña+=''.join(secrets.choice(alfabeto))
            return contraseña
        
    def seguridad(self):
        if self.__caracteres>=10:
            if self.__especial==True:
                if self.__mayusculas == True:
                    messagebox.showinfo('Información', 'La contraseña es muy segura')
                else:
                    messagebox.showinfo('Información', 'La contraseña es segura')
            if self.__especial==False:
                if self.__mayusculas == True:
                    messagebox.showinfo('Información', 'La contraseña es segura')
                else:
                    messagebox.showinfo('Información', 'La contraseña es medianamente segura')
        if self.__caracteres<10:
            if self.__especial==True:
                if self.__mayusculas == True:
                    messagebox.showinfo('Información', 'La contraseña es segura')
                else:
                    messagebox.showinfo('Información', 'La contraseña es medianamente segura')
            if self.__especial==False:
                if self.__mayusculas == True:
                    messagebox.showinfo('Información', 'La contraseña medianamente segura')
                else:
                    messagebox.showinfo('Información', 'La contraseña no es muy segura')