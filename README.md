## Pré Requisitos
 - PostgreSQL
 - Python

## Script do banco de dados
Executar o script do arquivo `initial_script.sql` no banco de dados postgresql, para obter o banco, tabela e dados necessários para o funcionamento da aplicação.

## Executar o Programa

### Servidor
Para ter o servidor funcionando, execute o seguinte comando: `python3 socket_server.py <host> <port>` ou `python socket_server.py <host> <port>`, a depender da sua instalação do Python.
`<host>`: Ip onde será executado o servidor, ex: 127.0.0.1, 192.168.0.5
`<port>`: Porta onde o socket irá ser executado, ex: 3333, 5000, 7300

### Cliente
Para ter o cliente funcionando, execute o seguinte comando: `python3 socket_client.py <server_host> <server_port>` ou `python socket_client.py <server_host> <server_port>`
`<server_host>`: Ip onde o servidor está executando, ex: 127.0.0.1, 192.168.0.5
`<server_port>`: Porta onde o servidor está executando, ex: 3333, 5000, 7300