import revenue.calculation as revenue
import expense.calculation as expense
import keyboard
import data_persistence.data_manager as data

def main():
    try:
        while True:
            if keyboard.is_pressed('esc'):
              print("Programa encerrado pelo usuário")
              break
        
            transaction_type = input("Digite o tipo de transação 'r' para receitas, 'd' para despesas, ou 't' para exibir a tabela de dados: ").lower()
            try:
              if transaction_type == 'r':
                revenue.calc()
              elif transaction_type == 'd':
                expense.calc()
              elif transaction_type == 't':
                data.show_table()
              else:
                raise ValueError("Tipo de transação inválida!")
            except ValueError as e:
              print(f"Erro: {e}")

    except KeyboardInterrupt:
        print("Programa encerrado pelo usuário.")
if __name__ == "__main__":
    main()