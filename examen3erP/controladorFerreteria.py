from tkinter import messagebox
import sqlite3

class controladorBD:
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion = sqlite3.connect(r'C:\Users\Edgar\OneDrive\Documentos\GitHub\POOS182\examen3erP\Ferreteria.db')
            return conexion
        except sqlite3.OperationalError:
            print('No se puede conectar')
            
    def guardarUsuario(self, material, cantidad):
        
        conx=self.conexionBD()
        if (cantidad == '' or material == ''):
            messagebox.showwarning('Aguas!!', 'Formulario incompleto')
            conx.close()
        else:
            cursor= conx.cursor()
            datos=(material, cantidad)
            sqlInsert=' insert into MatConstruccion(material, cantidad) values(?,?)'
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", 'Registro guardado')
        
    def buscarRegistro(self, id):
        conx = self.conexionBD()
        if(id==''):
            messagebox.showwarning('Cuidado','Escribe un identificador')
            conx.close()
        else:
            try:
                cursor= conx.cursor()
                sqlSelect = 'select * from MatConstruccion where IDMat= '+id
                
                cursor.execute(sqlSelect)
                RSusuario= cursor.fetchall()
                conx.close()
                return RSusuario
            except sqlite3.OperationalError:
                print('Error de consulta')
                
    def actualizarRegistro(self,id, material, cantidad):
        conx= self.conexionBD()
        if(id==''):
            messagebox.showwarning('Cuidado','Escribe un identificador')
            conx.close()
        if (material == '' or cantidad == ''):
            messagebox.showwarning('Aguas!!', 'Formulario incompleto')
        else:
            try:
                cursor = conx.cursor()
                datos=(material, cantidad)
                sqlUpdate = 'update MatConstruccion set Material=?, Cantidad=? where IDMat= '+id
                cursor.execute(sqlUpdate,datos)
                conx.commit()
                conx.close()
                messagebox.showinfo('Info','Información actualizada')
                
            except sqlite3.OperationalError:
                print('Error de consulta')
    
    def consultarRegistro(self):
        conx = self.conexionBD()
        try:
            cursor= conx.cursor()
            sqlSelect = 'SELECT * FROM MatConstruccion'
            cursor.execute(sqlSelect)
            RSconsul= cursor.fetchall()
            conx.close()
            return RSconsul
        except sqlite3.OperationalError:
            print('Error de consulta')
            conx.close()