nota1 = float(input("Inserir nota 1 "))
nota2 = float(input("Inserir nota 2 "))

if (nota1 + nota2)/2 >= 7:
    print("Aprovado")
elif (nota1 + nota2)/2 >= 4 < 7:
    print("Prova Final")
else:
    print("Reprovado")
