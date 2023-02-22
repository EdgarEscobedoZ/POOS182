from personaje import *

#1. Solicitar datos
print('')
print('### Solicitud Datos Heroe ###')
especieH=input('Escribe la especie del Heroe ')
nombreH=input('Escribe el nombre del Heroe ')
alturaH=float(input('Escribe la altura del Heroe '))
recargaH= int(input('Ingresa las balas para el Heroe '))

print('')
print('### Solicitud Datos Villano ###')
especieV=input('Escribe la especie del Villano ')
nombreV=input('Escribe el nombre del Villano ')
alturaV=float(input('Escribe la altura del Villano '))
recargaV= int(input('Ingresa las balas para el Villano '))

#2. Creamos los objetos
Heroe=Personaje(especieH, nombreH, alturaH)
Villano=Personaje(especieV, nombreV, alturaV)


#3. Usamos los metodos y atributos del Heroe
print('')
print('### Atributos del Heroe ###')
print('El personaje se llama '+ Heroe.nombre)
print('Pertenece a la especie '+Heroe.especie)
print('y una altura de '+ str(Heroe.altura))

Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargarArma(recargaH)

#4. Usar los metodos y atributos del villano
print('')
print('### Atributos del Villano ###')
print('El personaje se llama '+ Villano.nombre)
print('Pertenece a la especie '+Villano.especie)
print('y una altura de '+ str(Villano.altura))

Villano.correr(True)
Villano.lanzarGranadas()
Villano.recargarArma(recargaV)

