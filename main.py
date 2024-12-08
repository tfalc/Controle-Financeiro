import revenue.calculation as revenue
import expense.calculation as expense
import data_persistence.data_manager as data

def main():
    while True:
        transaction_type = input("Digite 'r' para adicionar receita, 'd' para adicionar despesa, 't' para exibir a tabela de dados, 's' para saldo, ou 'q' para sair:").lower()
        try:
          if transaction_type == 'r':
            revenue.calc()
          elif transaction_type == 'd':
            expense.calc()
          elif transaction_type == 't':
            data.show_table()
            expense.calc()
          elif transaction_type == 's':
            expense_total_value = expense.get_total_value() # Valor total de despesas
            revenue_total_value = revenue.get_total_value() # Valor total de receitas
            balance = revenue_total_value - expense_total_value
            # Imprimir os dados de receita, despesas e o saldo total
            print(f"Despesas Totais: {expense_total_value:.2f}")
            print(f"Receitas Totais: {revenue_total_value:.2f}")
            print(f"Saldo: {balance:.2f}")
          elif transaction_type == 'q':
            print("\nPrograma encerrado pelo usuário.")
            exit()
          else:
            raise ValueError("Tipo de transação inválida!")
        except ValueError as e:
          print(f"Erro: {e}")

if __name__ == "__main__":
    main()