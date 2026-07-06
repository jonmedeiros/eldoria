from funcoes import *
from banco import user_dados



"""
banco de imagens -------



"""


print("• ⚔️  ECOS DE ELDORIA  ⚔️  •".center(50, "🌲"))




while True:
    
    while True:
        decisao = int(input("1 - Iniciar Jogo \n 2 - Manual \n 3 - Ranking \n 4 - Exit "))

        match decisao:
            case 1:
                break
            case 2:
                print("Em breve...")
            case 3:
                print("Em breve...")
            case 4:
                exit()
    
    historia()

    personagem_escolhido = escolher_personagem()

    nome_do_jogador = dados_usuario()

    user_dados["personagem"] = personagem_escolhido["nome"]
    user_dados["username"]   = nome_do_jogador

    intro_jornada(nome_do_jogador)

    acampamento(personagem_escolhido)
    break
        