class Personaje:
    
    # agregamos el constructtor del personaje
    def __init__ (self, esp, nom, alt):
        #Atributos
        self.especie = esp
        self.nombre = nom
        self.altura = alt
    
    #metodos
    def correr(self, status):
        if (status):
            print("El personaje "+ self.nombre + " está corriendo")
        else:
            print("El personaje "+ self.nombre + " se detuvo")            
            
    def lanzarGranadas(self):
        print("El personaje " + self.nombre +' lanzó la granada')
        
    def recargarArma(self,municion):
        cargador=10
        cargador=cargador + municion
        print('El arma recargada tiene '+str(cargador)+" balas")