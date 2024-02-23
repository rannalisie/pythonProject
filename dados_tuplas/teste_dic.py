# Criando um dicionário vazio
meu_dicionario = {}

# Adicionando elementos ao dicionário (= recebe)
meu_dicionario['chave1'] = 'valor1'
meu_dicionario['chave2'] = 'valor2'
meu_dicionario['chave3'] = 'valor3'

# Acessando elementos do dicionário
print("O valor da chave 'chave1' é:", meu_dicionario['chave1'])

# Modificando um valor no dicionário
meu_dicionario['chave2'] = 'novo_valor'

# Deletando um par chave-valor do dicionário
del meu_dicionario['chave3']

# Verificando se uma chave existe no dicionário
if 'chave3' in meu_dicionario:
    print("A chave 'chave3' existe no dicionário.")
else:
    print("A chave 'chave3' não existe no dicionário.")

# Iterando sobre as chaves do dicionário
print("Chaves do dicionário:")
for chave in meu_dicionario:
    print(chave)

# Iterando sobre os valores do dicionário
print("Valores do dicionário:")
for valor in meu_dicionario.values():
    print(valor)

# Iterando sobre os pares chave-valor do dicionário
print("Pares chave-valor do dicionário:")
for chave, valor in meu_dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")