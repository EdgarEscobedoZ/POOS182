class validacion:
    
    def __init__ (self):
        self.__usuario = "pepe"
        self.__contraseña = "1234"
    
    def validar(self,user, contra):
        return user == self.__usuario and contra == self.__contraseña
    