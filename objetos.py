from personaje import *

#Creamos una instancia Heroe de la clase Personaje 
Heroe = Personaje()

#usamos los atributos
print('El personaje se llama '+ Heroe.nombre)
print('Pertenece a la especie '+Heroe.especie)
print('y una altura de '+ str(Heroe.altura))

#3. Usar los métodos
Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargarArma(37)