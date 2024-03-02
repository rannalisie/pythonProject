arquivos = open("primeiro_arquivo.txt", "w")

arquivos.write("Meu primeiro arquivo! Ai que festa!")

arquivos.close()

with open("primeiro_arquivo.txt", "a") as arquivos:
    arquivos.write("\nHakuna Matata")
