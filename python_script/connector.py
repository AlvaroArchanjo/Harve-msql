import mysql.connector

conn = mysql.connector.connect(
    user='root',
    password='jr',
    host='127.0.0.1',
    database='meu_banco',
    port='3307'
)

# if conn.is_connected():
#     print('CONECTAMOS!!!') 


print("Este é o melhor jogo de Pedra, Papel e Tesoura!")

print("Por favor insira seu nome:")
nome_jogador = input()

# import random
# computador = random 

while True
    print("Escolha sua jogada: PEDRA, PAPEL ou TESOURA")

    jogador = input()

    print("Asua jogada foi:", jogador)

    computador = "PEDRA"

    if computador == "PEDRA":
        if jogador == "PEDRA":
            resultado = "EMPATE"
        else:
            if jogador == "PAPEL":
                resultado = "VITORIA"
            else:
                resultado = "DERROTA"

    print(resultado)

    cursor = conn.cursor()
    query = f"""
        INSERT INTO contagem_jogos (nome_player, jogada_player, jogada_cpu, resultado)
    VALUES ('{nome_jogadorr}', '{jogador}', '{computador}', '{resultado[0]}')
    """

    cursor.execute(query)
    conn.commit()
    cursor.close()
    print("Deseja continuar jogando (Y/N)?")
    continuar = input()
    if continuar =="N":
