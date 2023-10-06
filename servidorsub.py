import socket

def servidor_subtracao():
    # Configura o servidor de subtração
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 8002))
    s.listen(1)

    while True:
        # Aguarda uma conexão do servidor de operações distribuídas
        conn, addr = s.accept()

        # Recebe a requisição do servidor de operações distribuídas
        conta = conn.recv(1024).decode()
        operacao, *valores = conta.split(',')
        valores = [float(valor) for valor in valores]

        # Realiza a subtração
        resultado = str(valores[0] - sum(valores[1:]))

        # Envia a resposta para o servidor de operações distribuídas
        conn.send(resultado.encode())

        # Fecha a conexão
        conn.close()

servidor_subtracao()
