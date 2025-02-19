casos = int(input())
for _ in range(casos):
    n = int(input())
    moviments = input().split()
    
    fila_inicial = int(moviments[0][1]) - 1
    columna_inicial = ord(moviments[0][0]) - ord('A')
    valid = True
    
    for i in range(1, len(moviments)):
        fila_final = int(moviments[i][1]) - 1
        columna_final = ord(moviments[i][0]) - ord('A')
        
        if not ((abs(fila_inicial - fila_final) == 2 and abs(columna_inicial - columna_final) == 1) or  (abs(fila_inicial - fila_final) == 1 and abs(columna_inicial - columna_final) == 2)):
            valid = False
            break
        
        fila_inicial = fila_final
        columna_inicial = columna_final
    
    if valid:
        print("Valid")
    else:
        print("Invalid")
