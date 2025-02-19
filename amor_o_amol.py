casos=int(input(""))

for __ in range(casos):
    entrada=input("").split(" ")
    
    nova_paraula=""
    sortida=[]

    for paraula in entrada:
        for letra in paraula:
            match letra:
                case "l":
                    nova_paraula+="r"
                case "L":
                    nova_paraula+="R"
                case "r":
                    nova_paraula+="l"
                case "R":
                    nova_paraula+="L"
                case _:
                    nova_paraula+=letra

        sortida.append(nova_paraula+" ")
        nova_paraula=""
    
    print("".join(sortida))