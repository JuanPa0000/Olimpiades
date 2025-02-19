casos, max_consultes, paraula = input().split()
casos, max_consultes = int(casos), int(max_consultes)
pags = []
for i in range(casos):
    
    input()
    primera, darrera = input().split()
    pags.append((primera, darrera))

esquerra, dreta = 0, casos - 1

while esquerra <= dreta:
    
    mig = (esquerra + dreta) // 2
    primera, darrera = pags[mig]
    
    print(f"? {mig + 1}", flush=True)

    if primera <= paraula <= darrera:
        print(f"! {mig + 1}", flush=True)
        break
    
    elif paraula < primera:
        dreta = mig - 1
    
    else:
        esquerra = mig + 1

