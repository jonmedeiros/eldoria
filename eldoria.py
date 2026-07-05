from funcoes import *



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

    break