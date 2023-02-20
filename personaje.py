class Personaje:
    
    #Atributos
    especie = "Humano"
    nombre = "MasterChief"
    altura = 2.70
    
    #metodos
    def correr(self, status):
        if (status):
            print("El personaje "+ self.nombre + " está corriendo")
        else:
            print("El personaje "+ self.nombre + " se detuvo")            print("El personaje "+ self.nombre + " se detuvo")
            
    def lanzarGranadas(self):
        print("El personaje " + self.nombre +' lanzó la granada')
        
    def recargarArma(self,municion):
        cargador=10
        cargador=cargador + municion
        print('El arma recargada tiene '+cargador+" balas")