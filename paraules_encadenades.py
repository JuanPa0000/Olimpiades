casos = int(input())  

for _ in range(casos):
    len_lista = int(input()) 
    lista = input().split()  

    connexions = {}
    for paraula in lista:
        primera = paraula[0]
        ultima = paraula[-1]
        if primera not in connexions:
            connexions[primera] = []
        connexions[primera].append(paraula)

    guanyador = ""

    while lista:
        jugada_valida = False
        for i, paraula in enumerate(lista):
            primera = paraula[0]
            if primera in connexions and connexions[primera]:
                jugada_valida = True
                lista.remove(paraula)  
                break
        
        if not jugada_valida:
            guanyador = "Xesc" if len(lista) % 2 == 0 else "Biel"
            break
        else:
            guanyador = "Biel" if len(lista) % 2 == 0 else "Xesc"

    print(guanyador)
