#coding utf-8

print('Progama para demostrar el funcionamiento y manipulacion de una lista')

una_lista=[15,20,40,0,-30]
print('Mi lista tiene los valores: ', una_lista)
print(f'Mi lista tiene {len(una_lista)} valores')
print('\nMi Lista colocando un elemnto por linea:')

#Ciclo for simplificado
for elemento in una_lista:
    print(elemento)

for elemento in range(0,len(una_lista)):
    print(f' En la posicion {elemento} esta el valor {una_lista[elemento]}')


#Cambiar el valor de un elemnto de la lista
una_lista[3]=10
print(f'La lisra con elemnto actualizado es ', una_lista)
#Agregae un valor
una_lista.append(12)
print(f'La lista con elemento añadido es ', una_lista)
#Usando ciclo while 
posicion=0
while posicion < len(una_lista):
    print(f'En la posicion {posicion} esta eel valor {una_lista[posicion]}')
    posicion+=1

#remover un elemento de la lista
una_lista.remove(10)
print('La lista con elemento removido es', una_lista)

una_lista.pop(3)
print('La lista con elemento "popeado" es', una_lista)

#extender
una_lista.extend([5,1000,-24])
print('la lista extendida es ', una_lista)
