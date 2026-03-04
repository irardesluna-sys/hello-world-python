# Nome do usuário

nome = input("Inseri seu nome completo: ")
print(f"Bem-vindo ao PetVida,{nome}")


# Idade do Pet

idade_do_pet = int(input("Inserir idade do seu Pet: "))

if idade_do_pet < 2:
    print("Filhote")
elif idade_do_pet > 7:
    print("Idoso")
elif idade_do_pet >= 2 and idade_do_pet <= 7:
    print("Adulto")
else:
    print("Dado incorreto")

# Peso do Pet

peso_do_pet = float(input("Inserir o peso do seu Pet: "))

if peso_do_pet >= 40:
    print("Atendimento Especial")
else:
    print("Atendimento normal")

# Temperatura do Pet

temperatura_do_pet = float(input("Inserir temperatura do seu Pet: "))

if temperatura_do_pet >= 39:
    print("Febre")
else:
    print("Normal")

# Validação no hotelzinho

vacinacao = input("Seu pet é vacinado ? Resposta com Sim ou Não: ")

if vacinacao =="sim" or vacinacao == "Sim":
    vacinacao = True
elif vacinacao == "Não" or vacinacao == "não" or vacinacao == "nao" or vacinacao == "Nao":
    vacinacao = False
else:
    print("Entrada inválida, assumindo Falso.")
    vacinacao = False
    

if idade_do_pet >= 1 and vacinacao is True:
    print("Pode usar o hotelzinho")
else:
    print("Não pode usar o hotelzinho")

