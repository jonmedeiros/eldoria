import textwrap
from personagens import *

def historia():

    historia = """Eldoria era um reino protegido por tres ordens antigas: os Guardioes da Lâmina, os Sentinelas da Lua e os Arcanistas do Sol. Um dia, uma fenda chamada Abismo Carmesim abriu-se nas ruinas do antigo castelo e passou a liberar monstros sem parar. Cada noite torna a fenda mais forte, e cada exploracao empurra o heroi mais fundo na maldicao."""
    print("")
    print("")
    print(textwrap.fill(historia, width=80))
    print("")
    print("")
    historia2 = """O heroi deve explorar o Abismo Carmesim, derrotar os monstros e descobrir a origem da fenda. Ele deve escolher sabiamente entre as ordens antigas, cada uma oferecendo habilidades únicas e desafios diferentes. A jornada é perigosa, mas a recompensa é grande: salvar Eldoria da destruição iminente."""

    print(textwrap.fill(historia2, width=80))
    print("")
    print("")

def escolher_personagem():
    print("Escolha seu personagem:")
    print("1 - Guerreiro")
    print("2 - Arqueiro")
    print("3 - Mago")
    escolha = int(input("Digite o número do personagem para ver os detalhes: "))

    match escolha:
        case 1:
            personagem = personagens["guerreiro"]
            tab_status(personagem)
        case 2:
            personagem = personagens["arqueiro"]
            tab_status(personagem)
        case 3:
            personagem = personagens["mago"]
            tab_status(personagem)
        case _:
            print("Escolha inválida. Por favor, tente novamente.")
    
    print(f"Você escolheu o personagem:", personagem["nome"])

    print(f"Deseja confirmar essa escolha? ")

    decisao_final = int(input("1 - SIM \n 2 - Ver/Escolher outro personagem: "))

    if decisao_final == 1:
        print(f"Você escolheu o {personagem['nome']} como personagem!")
        return personagem
    else:
        return escolher_personagem()
    


def tab_status(personagem):
    print("=" * 32)
    print("🧙 STATUS DO PERSONAGEM")
    print("═" * 32)

    icones = {
        "nome": "👤",
        "vida": "❤️",
        "mana": "🔮",
        "ataque": "⚔️",
        "defesa": "🛡️",
        "velocidade": "💨",
        "descricao": "📖"
    }

    for atributo, valor in personagem.items():
        print(f"{icones[atributo]} {atributo.capitalize()}: {valor}")




   


