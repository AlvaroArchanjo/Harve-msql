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
query = """
    INSERT INTO contagem_jogos (nome_player, jogada_player, jogada_cpu, resultado)
VALUES ('jogador', 'PEDRA', 'PEDRA', 'E')
"""

cursor.execute(query)
conn.commit()
cursor.close()
