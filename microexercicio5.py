sabor_de_suco = int(input("Qual a bebida que você deseja ? "))

match sabor_de_suco:
    case 1:
        print("Café")
    case 2:
        print("Chá")
    case 3:
        print("Suco")
    case _:
        print("Bebida Indisponível")
    
