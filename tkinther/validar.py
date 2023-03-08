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
    def __init__ (self,caract):
        self.__caracteres = caract
        
    
    
    def generar(self, x):
        minusculas = string.ascii_lowercase
        caracteres_esp = string.punctuation
        letras = string.ascii_letters
        contraseña = ''
        esp = messagebox.askyesno('Caracteres especiales','¿Desea usar caracteres especiales en su contraseña?')
        mayus = messagebox.askyesno('Mayusculas','¿Desea usar mayusuclas en su contraseña?')
        if x=="" :
            self.__caracteres=8
        if esp==True and mayus == True:
            alfabeto = caracteres_esp + letras
            for i in range (self.__caracteres):
                contraseña+=''.join(secrets.choice(alfabeto))
            return contraseña
        if esp==False and mayus == True:
            alfabeto = letras
            for i in range (self.__caracteres):
                contraseña+=''.join(secrets.choice(alfabeto))
            return contraseña
        if esp==True and mayus == False:
            alfabeto = caracteres_esp + minusculas
            for i in range (self.__caracteres):
                contraseña+=''.join(secrets.choice(alfabeto))
            return contraseña
        if esp==False and mayus == False:
            alfabeto = minusculas
            for i in range (self.__caracteres):
                contraseña+=''.join(secrets.choice(alfabeto))
            return contraseña
        
        
        
    #def validarContra():
        