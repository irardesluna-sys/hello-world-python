dia_da_semana = int(input("Informe um dia da semana entre 1 e 7"))

match dia_da_semana:
    case 1| 2 | 3 | 4 | 5 :
        print("Dia de semana")
    case 6 | 7 :
        print("Fim de semana")
    case _:
        print("Dia Inválido")
