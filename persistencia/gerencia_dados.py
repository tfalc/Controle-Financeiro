import receita.calculos as calculos


def salva_dados(dados):
    with open("dados.csv", "a") as arquivo:
        for dado in dados:
            arquivo.write(f"{dado};")
        arquivo.write("\n")
