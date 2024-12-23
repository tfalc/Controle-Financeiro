from application.revenue_service import RevenueService
from application.transaction_service import TransactionService
from infrastructure.keyboard_listener import KeyboardListener
from infrastructure.data_manager import DataManager
import matplotlib.pyplot as plt
import pandas as pd


def show_graph():
    # Carregar os dados do arquivo CSV
    df = pd.read_csv('dados.csv', delimiter=';')

    # Criar o gráfico
    fig, ax = plt.subplots()
    df.groupby('Tipo')['Valor'].sum().plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=90)
    ax.set_ylabel('')
    ax.set_title('Receitas e Despesas')

    # Exibir o gráfico
    plt.show()


def main():
    try:
        while True:
            if KeyboardListener.is_pressed('esc'):
                print("Programa encerrado pelo usuário")
                break

            transaction_type = input(
                "Digite o tipo de transação 'r' para receitas, 'd' para despesas, ou 't' para exibir a tabela de dados: ").lower()
            try:
                if transaction_type == 'r':
                    description = input("Qual o nome/descrição da receita?")
                    date_str = input("Qual a data da transação (dd/mm/aaaa)?")
                    value = float(input("Qual o valor da transação?"))
                    service = RevenueService(description, date_str, value)
                    print(service.validate_and_save())
                elif transaction_type == 'd':
                    description = input("Qual o nome/descrição da despesa?")
                    date_str = input("Qual a data da transação (dd/mm/aaaa)?")
                    value = float(input("Qual o valor da transação?"))
                    service = TransactionService(description, date_str, value)
                    print(service.validate_and_save())
                elif transaction_type == 't':
                    DataManager.show_table()
                    show_graph()
                else:
                    raise ValueError("Tipo de transação inválida!")
            except ValueError as e:
                print(f"Erro: {e}")

    except KeyboardInterrupt:
        print("Programa encerrado pelo usuário.")


if __name__ == "__main__":
    main()
