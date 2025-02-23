casos = int(input())

for _ in range(casos):

    n, m, k = map(int, input().split())

    blanques = list(map(int, input().split()))
    negres = list(map(int, input().split()))
    
    valor_peça_negra = k
    
    i = 0  
    j = 0  
    
    while i < n and j < m:
        valor_peça_negra -= blanques[i]
        i += 1
        

        if j < m:
            valor_peça_negra += negres[j]
            j += 1

        if valor_peça_negra < 0:
            print("??")
            break
    else:
        if valor_peça_negra > 0:
            print("!!") 
        elif valor_peça_negra == 0:
            print("!?") 