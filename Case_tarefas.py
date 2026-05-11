import json
tarefas=[]

def salvar_tarefas():
  with open("tarefas.json", "w") as arquivo:
    json.dump(tarefas, arquivo)
  print("Tarefas salvas com sucesso!")
def carregar_tarefas():
  try:
    with open("tarefas.json", "r") as arquivo:
      tarefas = json.load(arquivo)
      print("Tarefas carregadas com sucesso!")
      return tarefas
  except:
    print("Nenhum arquivo de tarefas encontrado! Começando nova lista")
    return []

def adicionar_tarefa(nome, prioridade):
  tarefa= {
        'nome': nome,
        'prioridade': prioridade
    }
  tarefas.append(tarefa)
  print("Tarefa adicionada")

def listar_tarefas():
  print("Lista de tarefas")
  for tarefa in tarefas:
    print(f"- {tarefa['nome']} (Prioridade {tarefa['prioridade']})")
def remover_tarefa(nome):
  for tarefa in tarefas:
    if tarefa['nome'] == nome:
      tarefas.remove(tarefa)
      print("Tarefa removida")
      break
  else:
    print("Tarefa não encontrada")

tarefas = carregar_tarefas()

while True:
  print("**Menu de Opções **")
  print("1. Adiconar Tarefa")
  print("2. Lista de tarefas")
  print("3. Remover Tarefas")
  print("4. Salvar tarefas")
  print("5. Sair")
  opcao= input("Escolha uma opção:")

  if opcao=="1":
    nome=input("Digite o nome da tarefa:")
    prioridade = input("Digite a prioridade da tarefa:")

    adicionar_tarefa(nome, prioridade)
  elif opcao=="2":
    listar_tarefas()

  elif opcao=="3":
    nome=input("Digite o nome da tarefa para ser removida:")
    remover_tarefa(nome)

  elif opcao=="4":
    salvar_tarefas()

  elif opcao.lower()=="5":
    print("Saindo do programa...")
    break

  else:
    print("Opção inválida. Tente novamente.")
