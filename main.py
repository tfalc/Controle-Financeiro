import receita.calculos as calculos


def main():
    entrada = input('Digite R para receita ou D para despesa')
    if entrada == 'R' or entrada == 'r':
        calculos.receita()
    elif entrada == 'D' or entrada == 'd':
        calculos.despesa()
    else:
        print('Entrada inválida. Tente novamente.')
        main()


if __name__ == '__main__':
    main()
    print('Para sair, digite S')
    if input() == 'S' or input() == 's':
        exit()
    else:
        main()
