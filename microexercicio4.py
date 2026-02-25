temperatura = int(input("Qual a temperatura em graus celsius? "))

if temperatura > 30:
    print("Muito Quente")
elif temperatura > 20:
    print("Agradável")
elif temperatura > 10:
    print("Frio")
else:
    print("Muito frio")