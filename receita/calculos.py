import pandas as pd


def entrada():
    while True:
        try:
            valor = float(input("Digite um valor: "))
            if valor < 0:
                raise ValueError
            return valor
        except ValueError:
            print("Por favor, digite um valor positivo.")
