import socket
import sys
import json

ACTION_SEARCH = 'search'
ACTION_UPDATE = 'update'
ACTION_CREATE = 'create'
ACTION_DELETE = 'delete'

def visualize(sock):
  company_name = input("Digite o nome da empresa para visualizar os efluentes: ")
  message = dict(
    action=ACTION_SEARCH,
    value=company_name
  )

  json_message = json.dumps(message, ensure_ascii=False).encode('utf-8')
  sock.send(json_message)

  response = sock.recv(2048).decode()
  print(f"Efluentes: {response}")

def update(sock):
  id = input('Digite o id do efluente para alterar: ')
  nome = input('Digite o nome que deseja (em branco para manter): ')
  ph_emissao = input('Digite o ph emissao que deseja (em branco para manter): ')
  ph_permitido = input('Digite o ph permitido que deseja (em branco para manter): ')

  value = dict(
    id=id,
    nome=nome if nome != '' else None,
    ph_emissao=float(ph_emissao) if ph_emissao != '' else None,
    ph_permitido=float(ph_permitido) if ph_permitido != '' else None
  )
  message = dict(
    action=ACTION_UPDATE,
    value=value
  )

  json_message = json.dumps(message, ensure_ascii=False).encode('utf-8')
  sock.send(json_message)

  response = sock.recv(1024).decode()
  print(f"Resposta: {response}")

def create(sock: socket):
  nome = input('Digite o nome do efluente (obrigatório): ')
  ph_emissao = input('Digite o ph emissao do efluente (obrigatório): ')
  ph_permitido = input('Digite o ph permitido do efluente (obrigatório): ')
  empresa = input('Digite a empresa que emitiu o efluente (obrigatório): ')

  value = dict(
    nome=nome,
    ph_emissao=float(ph_emissao),
    ph_permitido=float(ph_permitido),
    empresa=empresa
  )
  message = dict(
    action=ACTION_CREATE,
    value=value
  )

  json_message = json.dumps(message, ensure_ascii=False).encode('utf-8')
  sock.send(json_message)

  response = sock.recv(1024).decode()
  print(f"Resposta: {response}")

def delete(sock: socket):
  id = input('Digite o id do efluente para deletar: ')

  confirm = input('Tem certeza? s / n: ')

  if confirm == 's':
    message = dict(
      action=ACTION_DELETE,
      value=id
    )

    json_message = json.dumps(message, ensure_ascii=False).encode('utf-8')
    sock.send(json_message)

    response = sock.recv(1024).decode()
    print(f"Resposta: {response}")
  else:
    print("Operação cancelada")

host, port = sys.argv[1], int(sys.argv[2])

menu_text = f"Escolha uma das opções:\n[0]: Visualizar Efluentes\n[1]: Editar Efluente\n[2]: Criar Efluente\n[3]: Deletar Efluente\n[q]: Sair\n"  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
  client_socket.connect((host, port))
  print(f"Conectado ao servidor {host}:{port}")
  
  option = input(menu_text)

  while option != 'q':
    if int(option) == 0:
      visualize(client_socket)
    elif int(option) == 1:
      update(client_socket)
    elif int(option) == 2:
      create(client_socket)
    elif int(option) == 3:
      delete(client_socket)
    else:
      break

    option = input(menu_text)