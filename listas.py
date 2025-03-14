#ejemplos listas
import  random

def visalizar_la_lista(la_lista):
    for elemento in range(0,len(la_lista)):
     print(la_lista[elemento],'\t', end=" ")
     if (elemento +1)%10==0:
        print()

def obtener_lista_pares(la_lista):
   lista_numero_pares=[]
   for i in range(0,len(la_lista)):
      if la_lista[i] % 2 ==0:
         lista_numero_pares.append(la_lista[i])
   return lista_numero_pares

def obtener_lista_impares(la_lista):
   lista_numero_impares=[]
   for i in range(0,len(la_lista)):
      if la_lista[i] % 2 != 0:
         lista_numero_impares.append(la_lista[i])
   return lista_numero_impares

print('programa para generar 100 numeros aleatorios')
la_lista=[]
for i in range(0,100):
    la_lista.append(random.randint(0,100))

print('la lista es: ')
visalizar_la_lista(la_lista)

#Lista de los numero pares
lista_pares=obtener_lista_pares(la_lista)
print('la lista con los numero pares es: ')
visalizar_la_lista(la_lista)

#lista de los numero impares 
lista_impares=obtener_lista_impares(la_lista)
print('la lista con los numero impares es: ')
visalizar_la_lista(la_lista)
