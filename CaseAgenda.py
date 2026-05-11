
import json

agenda = []

def salvar_agenda():
    with open('agenda.json', 'w') as arquivo:
        json.dump(agenda, arquivo)
    print("Agenda salva com sucesso!")

def carregar_agenda():
    global agenda
    try:
        with open('agenda.json', 'r') as arquivo:
            agenda = json.load(arquivo)
        print("Agenda carregada com sucesso!")
        return agenda
    except FileNotFoundError:
        print("Nenhuma agenda encontrada")
        return []

def adicionar_contato(nome, telefone, email):
    # Validação simples
    if not nome.strip():
        print("Nome inválido.")
        return

    try:
        telefone = int(telefone)
    except ValueError:
        print("Telefone deve conter apenas números.")
        return

    if "@" not in email or "." not in email:
        print("Email inválido.")
        return

    contato = {
        'nome': nome.strip(),
        'telefone': telefone,
        'email': email.strip()
    }
    agenda.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")

def exibir_contatos():
    print("\nContatos na Agenda:")
    for contato in agenda:
        print("Nome:", contato['nome'])
        print("Telefone:", contato['telefone'])
        print("Email:", contato['email'])

def editar_contato():
    nome = input("Nome do contato que deseja editar: ")

    for contato in agenda:
        if contato['nome'] == nome:
            print("1. Editar Telefone")
            print("2. Editar Email")
            print("3. Editar Nome")
            print("4. Editar Email e Telefone")
            option = input("Digite a opção: ")

            if option == "1":
                novo_tel = input("Novo número de telefone: ")
                try:
                    contato['telefone'] = int(novo_tel)
                except ValueError:
                    print("Telefone inválido.")
            elif option == "2":
                novo_email = input("Novo email: ")
                if '@' in novo_email and '.' in novo_email:
                    contato['email'] = novo_email.strip()
                else:
                    print("Email inválido.")
            elif option == "3":
                novo_nome = input("Novo nome: ")
                if novo_nome.strip():
                    contato['nome'] = novo_nome.strip()
                else:
                    print("Nome inválido.")
            elif option == "4":
                novo_tel = input("Novo número de telefone: ")
                novo_email = input("Novo email: ")
                try:
                    contato['telefone'] = int(novo_tel)
                    if '@' in novo_email and '.' in novo_email:
                        contato['email'] = novo_email.strip()
                    else:
                        print("Email inválido.")
                except ValueError:
                    print("Telefone inválido.")
            else:
                print("Opção inválida.")
                return

            print("Contato atualizado com sucesso!")
            return

    print("Contato não encontrado.")

def remover_contato():
    nome = input("Digite o nome do contato que deseja remover: ")
    for contato in agenda:
        if contato['nome'] == nome:
            agenda.remove(contato)
            print("Contato removido.")
            return
    else:
        print("Contato não encontrado!\n")

# Carrega os dados ao iniciar
carregar_agenda()

# Menu principal
while True:
    print("\n-- Menu da Agenda --")
    print("1. Adicionar Contato")
    print("2. Exibir Agenda")
    print("3. Editar Contato")
    print("4. Remover Contato")
    print("5. Salvar Agenda")
    print("6. Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(nome, telefone, email)
    elif opcao == "2":
        exibir_contatos()
    elif opcao == "3":
        editar_contato()
    elif opcao == "4":
        remover_contato()
    elif opcao == "5":
        salvar_agenda()
    elif opcao == "6":
        print("Encerrando...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}
