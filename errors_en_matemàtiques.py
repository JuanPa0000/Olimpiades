casos=int(input(""))

for _ in range(casos):

    len_solucio=int(input())
    entrada_solucio=input()

    len_resposta=int(input())
    entrada_resposta=input()

    solucio=[]
    resposta=[]

    no_aparece=0
    sobren=0

    for n in entrada_solucio:
        solucio.append(int(n))

    for n in entrada_resposta:
        resposta.append(int(n))

    for p,i in enumerate(solucio):
        if resposta.count(i)==0:
            no_aparece+=1
            
        elif solucio[p:].count(i)>resposta.count(i):
            no_aparece+=solucio[p:].count(i)>resposta.count(i)

    for p,e in enumerate(resposta):
        if solucio.count(e)==0:
            sobren+=1
        elif resposta[p:].count(e)>solucio.count(e):
            sobren+=resposta[p:].count(e)-solucio.count(e)

    print(no_aparece+(sobren*5))