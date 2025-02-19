casos=int(input(""))
lista=[]

for _ in range(casos):

    entrada=int(input(""))
    lista.append(entrada)

for posicion,elemento in enumerate(lista):

    if lista[posicion-1] % 2 != 0:
        print((elemento//2)+1)
        
    else:
        print(elemento//2)