from tkinter import messagebox
import sqlite3
import bcrypt


class controladorBD:
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion = sqlite3.connect(r'C:\Users\Edgar\OneDrive\Documentos\GitHub\POOS182\TkinterSQLite\DBUsuarios.db')
            print('Conectado a la BD')
            return conexion
        except sqlite3.OperationalError:
            print('No se puede conectar')
            
            
    def guardarUsuario(self, nombre, correo, contra):
        #1. Mandar llamar una conexion
        conx=self.conexionBD()
        
        #2. Validar vacios
        if (nombre == '' or correo == '' or contra == ''):
            messagebox.showwarning('Aguas!!', 'Formulario incompleto')
            conx.close()
        else:
            #3. Realizar el insert a la BD
            #4. Preparamos las variables necesarias
            cursor= conx.cursor()
            conH = self.encriptarContra(contra)
            datos=(nombre,correo,conH)
            sqlInsert=' insert into tbRegistrados(nombre,correo,contra) values(?,?,?)'
            
            #5. Ejecutamos el insert
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", 'Usuario guardado')
            
    def encriptarContra(self,con):
        
        #Preparamos la contraseña y la sal para hash
        conPlana = con
        conPlana = conPlana.encode() #convierte el string a bytes
        sal = bcrypt.gensalt()
        
        #Encriptamos
        conHa = bcrypt.hashpw(conPlana, sal)
        print(conHa)
        
        #Regresamos la contraseña encriptada
        return conHa
        