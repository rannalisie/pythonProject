def perguntar () :
    return ("O que deseja realizar\n +"
              "<I> - Para Inserir um usuario\n"+
              "<P> - Para Pesquisar um usuario\n"+
              "<E> - Para Ecluir um usuario\n"+
              "<L> - Para Listar um usuario: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite a ultima data de acesso: "),
                                                   input("Qual a ultima estação acessada: ").upper()]

    salvar(dicionario)
def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))