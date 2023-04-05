from tkinter import messagebox
import sqlite3
import bcrypt


class controladorBD:
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion = sqlite3.connect(r'C:\Users\Edgar\OneDrive\Documentos\GitHub\POOS182\TkinterSQLite\DBUsuarios.db')
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
    
    def buscarUsuario(self, id):
        
        #1. Realizar conexion BD
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacio
        if(id==''):
            messagebox.showwarning('Cuidado','Escribe un identificador')
            conx.close()
        else:
            #3. Ejecutar la consulta
            try:
                #4. Preparamos lo necesario
                cursor= conx.cursor()
                sqlSelect = 'select * from tbRegistrados where id= '+id
                
                #5. Ejectutamos, guardamos la consulta y cerramos conexion
                cursor.execute(sqlSelect)
                RSusuario= cursor.fetchall()
                conx.close()
                return RSusuario
                
            except sqlite3.OperationalError:
                print('Error de consulta')
                
    def consultarUsuario(self):
        conx = self.conexionBD()
        try:
            cursor= conx.cursor()
            sqlSelect = 'SELECT * FROM tbRegistrados'
            cursor.execute(sqlSelect)
            RSconsul= cursor.fetchall()
            conx.close()
            return RSconsul
        except sqlite3.OperationalError:
            print('Error de consulta')
            conx.close()
            
    def eliminarUsuario(self, id):
        
        #1. Realizar conexion BD
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacio
        if(id==''):
            messagebox.showwarning('Cuidado','Escribe un identificador')
            conx.close()
        else:
            #3. Ejecutar la consulta
            try:
                #4. Preparamos lo necesario
                cursor= conx.cursor()
                sqlDelete = 'delete from tbRegistrados where id= '+id
                
                #5. Ejectutamos, guardamos la consulta y cerramos conexion
                cursor.execute(sqlDelete)
                conx.commit()
                #cursor.fetchall()
                conx.close()
                
            except sqlite3.OperationalError:
                print('Error de consulta')
                
    def actualizarUsuario(self,id, nombre, correo, contra):
        conx= self.conexionBD()
        
        if(id==''):
            messagebox.showwarning('Cuidado','Escribe un identificador')
            conx.close()
        if (nombre == '' or correo == '' or contra == ''):
            messagebox.showwarning('Aguas!!', 'Formulario incompleto')
        else:
            #3. Ejecutar la consulta
            try:
                #4. Preparamos lo necesario
                cursor= conx.cursor()
                conH = self.encriptarContra(contra)
                datos=(nombre,correo,conH)
                sqlDelete = 'update tbRegistrados set nombre=?,correo=?,contra=? where id= '+id
                
                #5. Ejectutamos, guardamos la consulta y cerramos conexion
                cursor.execute(sqlDelete,datos)
                conx.commit()
                #cursor.fetchall()
                conx.close()
                messagebox.showinfo('Info','Información actualizada')
                
            except sqlite3.OperationalError:
                print('Error de consulta')