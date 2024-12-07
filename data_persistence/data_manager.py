# Importa a biblioteca pandas, que é utilizada para manipulação e análise de dados de forma eficiente
import pandas as pd  

# Importa o módulo tkinter para criar interfaces gráficas
import tkinter as tk

# Importa o widget `ttk`, que contém uma série de widgets mais modernos para criar interfaces mais elegantes
from tkinter import ttk  

# Função para salvar dados em um arquivo CSV
def save(date):
    # Abre (ou cria, se não existir) o arquivo `dados.csv` no modo "a" (append), para adicionar conteúdo ao final do arquivo
    with open("dados.csv", "a") as arquivo:
        # Une todos os elementos da lista `date` em uma única string, usando `;` como delimitador
        linha = ";".join(str(date_) for date_ in date)  
        # Escreve a linha resultante no arquivo, adicionando uma quebra de linha no final
        arquivo.write(f"{linha}\n")

def get_data(transaction_type, column_type):
    """
      Lêr os dados do arquivo dados.csv, filtrar pelo tipo de transação (Receita ou Despesa), e retornar
      Args:
        transaction_type (str): "Receita ou Despesa"
      Returns:
        df
    """
    try:
        # Lê o arquivo dados.csv e remove as linhas vazias
        df = pd.read_csv("dados.csv", delimiter=";", header=None, names=["Transação", "Descrição", "Data", "Valor"])
        df = df.dropna()

        # Converter a coluna 'Valor' para float
        df["Valor"] = df["Valor"].astype(float)

        # Filtrar pelo tipo de transação
        filtered = df[df["Transação"] == transaction_type]

        # Retornar a coluna solicitada
        if column_type in filtered.columns:
            return filtered[column_type]
        else:
            raise ValueError(f"A coluna '{column_type}' não existe.")
    except FileNotFoundError:
        # Mensagem de erro caso o arquivo `dados.csv` não seja encontrado
        print("Arquivo 'dados.csv' não encontrado!")
        return  # Interrompe a execução da função
    except pd.errors.EmptyDataError:
        # Mensagem de erro caso o arquivo `dados.csv` esteja vazio ou contenha apenas delimitadores
        print("Arquivo 'dados.csv' está vazio ou contém apenas delimitadores.")
        return  # Interrompe a execução da função
    except Exception as e:
        # Mensagem de erro genérica para qualquer outra exceção que possa ocorrer
        print(f"Ocorreu um erro: {e}")
        return  # Interrompe a execução da função
# Função para exibir os dados salvos em uma tabela
def show_table():
    try:
        # Tenta ler o arquivo CSV `dados.csv` usando pandas
        # `delimiter=";"` define que os campos são separados por ponto e vírgula
        # `header=None` indica que o arquivo não tem cabeçalho
        # `names=["Transação", "Descrição", "Data", "Valor"]` define os nomes das colunas manualmente
        df = pd.read_csv("dados.csv", delimiter=";", header=None, names=["Transação", "Descrição", "Data", "Valor"])
        # Remove as linhas vazias que possam existir no DataFrame
        df = df.dropna()  
    except FileNotFoundError:
        # Mensagem de erro caso o arquivo `dados.csv` não seja encontrado
        print("Arquivo 'dados.csv' não encontrado!")
        return  # Interrompe a execução da função
    except pd.errors.EmptyDataError:
        # Mensagem de erro caso o arquivo `dados.csv` esteja vazio ou contenha apenas delimitadores
        print("Arquivo 'dados.csv' está vazio ou contém apenas delimitadores.")
        return  # Interrompe a execução da função
    except Exception as e:
        # Mensagem de erro genérica para qualquer outra exceção que possa ocorrer
        print(f"Ocorreu um erro: {e}")
        return  # Interrompe a execução da função

    # Cria uma janela principal do tkinter
    root = tk.Tk()
    # Define o título da janela
    root.title("Tabela de Receitas e Despesas")

    # Cria um frame dentro da janela para organizar o layout
    frame = ttk.Frame(root)
    # Expande o frame para preencher todo o espaço disponível
    frame.pack(fill="both", expand=True)

    # Cria um widget Treeview (uma espécie de tabela) para exibir os dados do DataFrame
    tree = ttk.Treeview(frame, columns=list(df.columns), show="headings")  # Corrige a palavra `colums` para `columns`
    
    # Define os títulos das colunas na tabela
    for col in df.columns:  # Corrige `dataframe` para `df`
        tree.heading(col, text=col)  # Define o nome da coluna para cada título
        tree.column(col, width=150)  # Define a largura das colunas

    # Insere os dados do DataFrame na tabela linha por linha
    for index, row in df.iterrows():  # Corrige `dataframe` para `df`
        tree.insert("", "end", values=list(row))  # Insere os valores da linha atual na tabela

    # Expande a tabela para preencher todo o espaço disponível na janela
    tree.pack(fill="both", expand=True)

    # Inicia o loop principal do tkinter para exibir a interface gráfica e manter a janela aberta
    root.mainloop()
