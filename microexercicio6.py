nota1 = float(input("Inserir nota 1 "))
nota2 = float(input("Inserir nota 2 "))
media = (nota1 + nota2)/2

if media >= 7:
    print("Aprovado por média")
elif media >=4 < 7:
    print("Prova Final")
else:
    print("Reprovado")
    