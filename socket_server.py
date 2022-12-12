import socket
import sys
import psycopg2
import json
import selectors
import types

ACTION_SEARCH = 'search'
ACTION_UPDATE = 'update'
ACTION_CREATE = 'create'
ACTION_DELETE = 'delete'

DB_NAME='projeto_final_rec'
DB_HOST='localhost'
DB_USER='e2bagile'
DB_PASS='e2bagile'
DB_PORT=28137

database_connection = psycopg2.connect(database=DB_NAME,
  host=DB_HOST,
  user=DB_USER,
  password=DB_PASS,
  port=DB_PORT)

cursor = database_connection.cursor()

sel = selectors.DefaultSelector()

def close_socket_connection(sock: socket, address: str):
  print(f"Closing connection to {address}")
  sel.unregister(sock)
  sock.close()

def json_decode(encoded_json):
  decoded = json.loads(encoded_json)

  return decoded

def json_encode(data_to_encode):
  encoded = json.dumps(data_to_encode, ensure_ascii=False).encode('utf-8')

  return encoded

def map_to_object(dbo: tuple):
  return dict(
    id=dbo[0],
    nome=dbo[1],
    ph_emissao=dbo[2],
    ph_permitido=dbo[3],
    empresa=dbo[4]
  )

def search_by_company(company):
  cursor.execute(f"SELECT * FROM efluentes WHERE empresa = '{company}' ORDER BY id")

  dbos = cursor.fetchall()

  return list(map(lambda dbo: map_to_object(dbo), dbos))

def update_by_id(obj):
  id = obj['id']
  nome = obj['nome']
  ph_emissao = obj['ph_emissao']
  ph_permitido = obj['ph_permitido']
  
  parameters = []

  if nome is not None:
    parameters.append(f"nome='{nome}'")
  if ph_emissao is not None:
    parameters.append(f"ph_emissao={ph_emissao}")
  if ph_permitido is not None:
    parameters.append(f"ph_permitido={ph_permitido}")
  
  if len(parameters) > 0:
    set_query = ",".join(parameters)
    cursor.execute(f"UPDATE efluentes SET {set_query} WHERE id={id}")
    database_connection.commit()

def create(obj):
  nome = obj['nome']
  ph_emissao = obj['ph_emissao']
  ph_permitido = obj['ph_permitido']
  empresa = obj['empresa']

  cursor.execute(f"INSERT INTO efluentes VALUES (DEFAULT, '{nome}', {ph_emissao}, {ph_permitido}, '{empresa}')")
  database_connection.commit()

def delete_by_id(id: str):
  cursor.execute(f"DELETE FROM efluentes WHERE id={id}")
  database_connection.commit()

def accept_wrapper(sock):
  new_connection, address = sock.accept()
  print("Connection from: " + str(address))
  new_connection.setblocking(False)
  data = types.SimpleNamespace(address=address, message="")
  events = selectors.EVENT_READ | selectors.EVENT_WRITE
  sel.register(new_connection, events, data=data)

def service_connection(key, mask):
  sock = key.fileobj
  data = key.data

  if mask & selectors.EVENT_READ:
    recv_data = sock.recv(2048).decode()

    if recv_data:
      decoded_data = json_decode(recv_data)
      print(decoded_data)

      if (decoded_data['action'] == ACTION_SEARCH):
        response_data = search_by_company(decoded_data['value'])

        sock.send(json_encode(response_data))
      elif (decoded_data['action'] == ACTION_UPDATE):
        update_by_id(decoded_data['value'])

        sock.send(json_encode(dict(message='Atualizado com sucesso')))
      elif (decoded_data['action'] == ACTION_CREATE):
        create(decoded_data['value'])

        sock.send(json_encode(dict(message='Creado com sucesso')))
      elif (decoded_data['action'] == ACTION_DELETE):
        delete_by_id(decoded_data['value'])

        sock.send(json_encode(dict(message='Deletado com sucesso')))
      else:
        close_socket_connection(sock, data.address)
    else:
      close_socket_connection(sock, data.address)
  if mask & selectors.EVENT_WRITE:
    if data.message:
      print(f"Echoing {data.message!r} to {data.address}")
      sock.send(data.message)

host, port = sys.argv[1], int(sys.argv[2])

server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

server_socket.listen()
print(f"Listening on port {(host, port)}")
server_socket.setblocking(False)
sel.register(server_socket, selectors.EVENT_READ, data=None)

try:
  while True:
    events = sel.select(timeout=None)
    for key, mask in events:
      if key.data is None:
        accept_wrapper(key.fileobj)
      else:
        service_connection(key, mask)
except KeyboardInterrupt:
  print("Caught keyboard interrupt, exiting")
finally:
  sel.close()