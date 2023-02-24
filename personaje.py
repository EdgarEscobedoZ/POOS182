class Personaje:
    
    # agregamos el constructtor del personaje
    def __init__ (self, esp, nom, alt):
        #Atributos
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt
    
    #metodos
    def correr(self, status):
        if (status):
            print("El personaje "+ self.__nombre + " está corriendo")
        else:
            print("El personaje "+ self.__nombre + " se detuvo")            
            
    def lanzarGranadas(self):
        print("El personaje " + self.__nombre +' lanzó la granada')
        
    def recargarArma(self,municion):
        cargador=10
        cargador=cargador + municion
        print('El arma recargada tiene '+str(cargador)+" balas")
        
    #Gets y sets 
    
    def getEspecie(self):
        return self.__especie
    def setEspecie(self, esp):
        self.__especie=esp
        
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nom):
        self.__nombre=nom
    
    def getAltura(self):
        return self.__altura
    def setAltura(self, alt):
        self.__altura=alt
    
    def __pensar(self):
        print('Estoy pensando........ ')