import pandas as pd
import persistencia.gerencia_dados
from persistencia import gerencia_dados
import datetime


def receita():
    descricao = input("Qual o nome da receita? ")
    data = input("Qual a data da receita? ")
    valor = float(input("Qual o valor da receita? "))
    gerencia_dados.salva_dados(['Receita', descricao, data, valor])
    return ['Receita', descricao, data, valor]


def despesa():
    descricao = input("Qual o nome da despesa? ")
    data = input("Qual a data da despesa? ")
    valor = float(input("Qual o valor da despesa? "))
    gerencia_dados.salva_dados(['Despesa', descricao, data, valor])
    return ['Despesa', descricao, data, valor]
