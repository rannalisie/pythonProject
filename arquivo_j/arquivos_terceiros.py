with open("economic-indicators.csv", "r") as arquivos_terceiros:
    total=0
    for linha in arquivos_terceiros.readlines()[1:-1]:
        total=total+float(linha.split(",")[3])
    print("O total de voos é: ", total)


