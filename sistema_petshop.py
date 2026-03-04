# Nome do usuário

import sys


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

# Grupo de Risco

if idade_do_pet > 10 and peso_do_pet < 2:
    print("Seu Pet está no grupo de Risco")

 # Serviço

servico = input("Qual serviço você deseja para seu pet ? ")

if not servico: 
    print("Dado Inválido")
    sys.exit() # Para o programa aqui
else:
    print("Ok, seguiremos com o atendimento.")

# Telefone do Cliente

telefone = input("Qual o seu telefone")

if not telefone:
    print("Dado Inválido")
else:
    print("Vamos para próxima fase do atendimento.")

#Tipo do Pet

tipo_de_pet = int(input("Considerando que Cachorro > 1, Gato > 2 e Aves > 3, qual número corresponde ao seu animal ? "))

if tipo_de_pet == 1:
    print("Vamos seguir com o atendimento do seu Cachorro")
elif tipo_de_pet == 2:
    print("Vamos Seguir com o atendimento do seu gato")
elif tipo_de_pet == 3:
    print("Vamos seguir com o atendimento da sua ave")
else:
    print("Animal inválido")
    sys.exit() # Para o programa aqui

# Plano do cliente 


