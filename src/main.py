from src.medicationService import adicionar_medicamento, listar_medicamentos, marcar_como_tomado
from src.api import consultar_cep, formatar_endereco

def menu():
    print("\n=== MediReminder CLI ===")
    print("1. Adicionar medicamento")
    print("2. Listar medicamentos")
    print("3. Marcar como tomado")
    print("4.Consultar CEP do paciente")
    print("5. Sair")

while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        horario = input("Horário (ex: 08:00): ")
        adicionar_medicamento(nome, horario)
        print("Adicionado!")

    elif opcao == "2":
        meds = listar_medicamentos()
        for m in meds:
            status = "✔" if m["tomado"] else "✘"
            print(f"{m['nome']} - {m['horario']} [{status}]")

    elif opcao == "3":
        nome = input("Nome: ")
        if marcar_como_tomado(nome):
            print("Marcado!")
        else:
            print("Não encontrado")

    elif opcao == "4":
        cep = input("Digite o CEP do paciente (somente números): ")
        dados = consultar_cep(cep)
        if dados:
            print("\n  Endereço encontrado:")
            print(f"  {formatar_endereco(dados)}")
        else:
            print("  CEP não encontrado ou inválido.")

    elif opcao == "5":
        break
