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
            print("El personaje "+ self.nombre + " se detuvo")