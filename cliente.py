import socket

def infos(operacao, valores):
    # Estabelece conexão com o servidor de operações distribuídas
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8000))

    # Formata a requisição com a operação e os valores
    conta = f"{operacao},{','.join(str(valor) for valor in valores)}"
    s.send(conta.encode())

    # Recebe a resposta do servidor de operações distribuídas
    resultado = s.recv(1024).decode()

    # Exibe o resultado na tela do cliente
    print(f"Resultado: {resultado}")

    # Fecha a conexão
    s.close()

# Interface de linha de comando
entrada = input("Op,N1,N2: ")
operacao, *valores = entrada.split(',')
valores = [float(valor) for valor in valores]

infos(operacao, valores)
