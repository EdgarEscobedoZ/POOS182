
class validacion:
    def __init__ (self):
        self.__nombre = ""
        self.__apellidoP = ""
        self.__apellidoM = ""
        self.__añoC = "2023"
        self.__añoN = ""
        self.__carrera = ""
        
    def matri(self, a, b, c, d, e):
        self.__nombre = a
        self.__apellidoP = b
        self.__apellidoM = c
        self.__añoN = d
        self.__carrera = e
        for i in range (3,2,1):
            print(self.__añoC[i])
            print(self.__añoN[i])
        print(self.__nombre[0])
        print(self.__apellidoP[0])
        print(self.__apellidoM[0])
        print(self.__carrera[0])
        
        