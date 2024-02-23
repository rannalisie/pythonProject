nome = []
telefone = []
cidade = []
regiao = []
resposta = "S"
while resposta == "S":
    nome_input = input("Nome: ")
    if nome_input.strip() == "":
        print("Nome não pode estar vazio. Por favor, insira um nome válido.")
        continue
    nome.append(nome_input)

    telefone_input = input("Telefone: ")
    if len(telefone_input) != 9:
        print("Número de telefone inválido. Por favor, insira um número com 9 dígitos.")
        continue
    telefone.append(float(telefone_input))

    cidade.append(input("Cidade: "))
    regiao.append(input("Região: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0, len(nome)):
    print("\nNome..: ", (indice + 1))
    print("Nome.........: ", nome[indice])
    print("Telefone........: ", telefone[indice])
    print("Cidade.......: ", cidade[indice])
    print("Região.: ", regiao[indice])