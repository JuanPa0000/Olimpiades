casos = int(input())

for _ in range(casos):

    hora_sortida, n = input().split()
    n = int(n)
    
    h, m = map(int, hora_sortida.split(":"))
    sortida_en_minuts = (h - 6) * 60 + m
    
    millor_ruta = None
    millor_diferencia = float('inf')
    
    for _ in range(n):

        codi, temps_normal, retard = input().split()
        temps_normal = int(temps_normal)
        retard = int(retard)
        
        temps_arribada = sortida_en_minuts + temps_normal + retard
        
        diferencia = abs(temps_arribada - 150)
        
        if temps_arribada <= 150 and diferencia < millor_diferencia:
            millor_diferencia = diferencia
            millor_ruta = codi
    
    if millor_ruta:
        print(millor_ruta)
    else:
        print("NO ARRIBA")
