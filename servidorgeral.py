import socket

def servidorgeral():
    # Configura o servidor de operações distribuídas
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 8000))
    s.listen(1)

    while True:
        # Aguarda uma conexão do cliente
        conn, addr = s.accept()

        # Recebe a requisição do cliente
        conta = conn.recv(1024).decode()
        operacao, valores = conta.split(',', 1)
        valores = [float(valor) for valor in valores.split(',')]

        # Encaminha a requisição para o servidor de operação correspondente
        resultado = encaminhar_para_servidor(operacao, valores)

        # Envia a resposta para o cliente
        conn.send(resultado.encode())

        # Fecha a conexão
        conn.close()

def somaousub(operacao, valores):
    # Estabelece conexão com o servidor correspondente
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if operacao == 'soma':
        s.connect(('localhost', 8001))
    elif operacao == 'subtracao':
        s.connect(('localhost', 8002))

    # Envia a requisição para o servidor correspondente
    conta = f"{operacao},{','.join(str(valor) for valor in valores)}"
    s.send(conta.encode())

    # Recebe a resposta do servidor correspondente
    resultado = s.recv(1024).decode()

    # Fecha a conexão com o servidor correspondente
    s.close()

    return resultado

servidorgeral()
