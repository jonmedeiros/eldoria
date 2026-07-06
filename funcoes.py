import textwrap
import time
import sys
import os
from colorama import Fore, Style, init
from personagens import *

init(autoreset=True)

"""
---------------- INTERFACE -----------

"""

# --- TILEMAP ---
VAZIO    = 0  # 🟫 andável
AGUA     = 1  # 🟦 bloqueado
ARVORE   = 2  # 🌳 bloqueado
COGUMELO = 3  # 🍄 portal floresta
PALMEIRA = 4  # 🌴 bloqueado
CASA     = 5  # 🏡 portal casa
LOJA     = 6  # 🏪 portal loja
GOBLIN = 7  # 👹 goblin

TILES = {
    VAZIO:    "🟫",
    AGUA:     "🟦",
    ARVORE:   "🌳",
    COGUMELO: "🍄",
    PALMEIRA: "🌴",
    CASA:     "🏡",
    LOJA:     "🏪",
    GOBLIN: "👹",
}

ANDAVEL = {VAZIO}
PORTAIS = {COGUMELO: "floresta", CASA: "casa", LOJA: "loja", GOBLIN: "goblin"}

MAPA_ACAMPAMENTO = [
    [ARVORE,   ARVORE,   COGUMELO, VAZIO,    COGUMELO, ARVORE,   ARVORE,   ARVORE  ],
    [AGUA,     AGUA,     AGUA,     VAZIO,    AGUA,     PALMEIRA, LOJA,     PALMEIRA],
    [AGUA,     AGUA,     AGUA,     VAZIO,    VAZIO,    AGUA,     VAZIO,    AGUA    ],
    [PALMEIRA, CASA,     PALMEIRA, AGUA,     VAZIO,    AGUA,     VAZIO,    AGUA    ],
    [AGUA,     VAZIO,    VAZIO,    VAZIO,    VAZIO,    VAZIO,    VAZIO,    AGUA    ],
    [ARVORE,   ARVORE,   ARVORE,   ARVORE,   ARVORE,   ARVORE,   ARVORE,   ARVORE  ],
]

MAPA_FLORESTA = [
    [ARVORE,     ARVORE,   ARVORE,   ARVORE,   ARVORE,   ARVORE,   ARVORE,   ARVORE  ],
    [ARVORE,     VAZIO,    VAZIO,    GOBLIN,    VAZIO,    VAZIO,    VAZIO,    ARVORE  ],
    [ARVORE,     VAZIO,    VAZIO,    VAZIO,    VAZIO,    VAZIO,    VAZIO,    ARVORE  ],
    [ARVORE,     VAZIO,    VAZIO,    VAZIO,    VAZIO,    VAZIO,    VAZIO,    ARVORE  ],
    [ARVORE,     VAZIO,    VAZIO,    VAZIO,    VAZIO,    VAZIO,    VAZIO,    ARVORE  ],
    [ARVORE,     ARVORE,   ARVORE,   ARVORE,   ARVORE,   ARVORE,   ARVORE,   ARVORE  ],

]


ICONE_JOGADOR = "🧙"


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def desenhar_mapa(mapa, pos_jogador, titulo=""):
    limpar()
    print(Fore.YELLOW + titulo.center(40) + Style.RESET_ALL)
    print(Fore.YELLOW + "─" * 30 + Style.RESET_ALL)
    for i, linha in enumerate(mapa):
        linha_str = ""
        for j, tile in enumerate(linha):
            if [i, j] == pos_jogador:
                linha_str += ICONE_JOGADOR
            else:
                linha_str += TILES[tile]
        print(linha_str)
    print(Fore.YELLOW + "─" * 30 + Style.RESET_ALL)
    print(Fore.CYAN + "  W/A/S/D para mover  |  Q para sair" + Style.RESET_ALL)


def acampamento(personagem):
    pos = [5, 2]

    while True:
        desenhar_mapa(MAPA_ACAMPAMENTO, pos, "  🏕️   ACAMPAMENTO  🏕️  ")
    
        cmd = input("  > ").strip().lower()

        if cmd == "q":
            break

        movimentos = {"w": [-1, 0], "s": [1, 0], "a": [0, -1], "d": [0, 1]}

        if cmd not in movimentos:
            continue

        dl, dc = movimentos[cmd]
        nova_linha = pos[0] + dl
        nova_col   = pos[1] + dc

        if not (0 <= nova_linha < len(MAPA_ACAMPAMENTO) and 0 <= nova_col < len(MAPA_ACAMPAMENTO[0])):
            continue

        destino = MAPA_ACAMPAMENTO[nova_linha][nova_col]
        portal  = PORTAIS.get(destino)

        if portal:
            limpar()
            if portal == "casa":
                print(Fore.GREEN + "🏡 Você entrou na cabana. Descanse um pouco..." + Style.RESET_ALL)
            elif portal == "loja":
                print(Fore.CYAN + "🏪 Você entrou na loja. Bem-vindo, aventureiro!" + Style.RESET_ALL)
            elif portal == "floresta":
                print(Fore.RED + "🍄 Você adentrou a floresta... O Abismo Carmesim está próximo." + Style.RESET_ALL)
                time.sleep(2)
                floresta(personagem)
                
            time.sleep(2)
            break

        elif destino in ANDAVEL:
            pos = [nova_linha, nova_col]

def floresta(personagem):

    from banco import user_dados

    nivel_atual = user_dados["nivel"]

    pos = [4, 1]

    while True:
        desenhar_mapa(MAPA_FLORESTA, pos, "  🌲   FLORESTA  🌲  ")
    
        cmd = input("  > ").strip().lower()

        if cmd == "q":
            break

        movimentos = {"w": [-1, 0], "s": [1, 0], "a": [0, -1], "d": [0, 1]}

        if cmd not in movimentos:
            continue

        dl, dc = movimentos[cmd]
        nova_linha = pos[0] + dl
        nova_col   = pos[1] + dc

        if not (0 <= nova_linha < len(MAPA_FLORESTA) and 0 <= nova_col < len(MAPA_FLORESTA[0])):
            continue

        destino = MAPA_FLORESTA[nova_linha][nova_col]
        portal  = PORTAIS.get(destino)

        if portal:
            limpar()
            if portal == "goblin":
                print(Fore.GREEN + "BATALHAA" + Style.RESET_ALL)


                from sistema_de_batalha import gerar_batalha

                gerar_batalha(nivel_atual)

            time.sleep(2)
            break

        elif destino in ANDAVEL:
            pos = [nova_linha, nova_col]

def dialogo(texto, velocidade, cor=""):
    texto = textwrap.fill(texto, width=70)

    if cor:
        sys.stdout.write(cor)

    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)

    if cor:
        sys.stdout.write(Style.RESET_ALL)

    print()

def historia():

    print(Fore.YELLOW + "🌲🌲🌲  ⚔️  ECOS DE ELDORIA  ⚔️  🌲🌲🌲".center(60) + Style.RESET_ALL)
    print(Fore.YELLOW + "═" * 55 + Style.RESET_ALL)
    print()

    dialogo(
        "🏰 Eldoria era um reino protegido por três ordens antigas: "
        "os ⚔️  Guardiões da Lâmina, os 🌙 Sentinelas da Lua e os ☀️  Arcanistas do Sol. "
        "Um dia, uma fenda chamada 🔥 Abismo Carmesim abriu-se nas ruínas do antigo castelo "
        "e passou a liberar 👹 monstros sem parar. Cada noite torna a fenda mais forte, "
        "e cada exploração empurra o herói mais fundo na maldição.",
        velocidade=0.03, cor=Fore.WHITE
    )
    print()

    dialogo(
        "🗺️  O herói deve explorar o Abismo Carmesim, derrotar os 💀 monstros "
        "e descobrir a origem da fenda. Ele deve escolher sabiamente entre as ordens antigas, "
        "cada uma oferecendo ✨ habilidades únicas e desafios diferentes. "
        "A jornada é perigosa, mas a recompensa é grande: salvar 🏰 Eldoria da destruição iminente.",
        velocidade=0.03, cor=Fore.CYAN
    )
    print()
    print(Fore.YELLOW + "═" * 55 + Style.RESET_ALL)
    print()


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

def dados_usuario():

    jogador = str(input("Qual o seu nome? "))

    if jogador.isalpha():
        print(f"Seja bem vindo {jogador}!")
        return jogador
    else:
        print("Nome inválido. Por favor, insira apenas letras.")
        return dados_usuario()


def intro_jornada(nome_jogador):
    print()
    print(Fore.RED + "🔥" * 27 + Style.RESET_ALL)
    print(Fore.RED + "  ⚠️   A JORNADA COMEÇA  ⚠️  ".center(55) + Style.RESET_ALL)
    print(Fore.RED + "🔥" * 27 + Style.RESET_ALL)
    print()

    partes = [
        (
            Fore.WHITE,
            f"🚪 Após escolher sua ordem, {nome_jogador} deixa os portões da capital "
            f"🏰 Eldoria para trás. O caminho até o 🔥 Abismo Carmesim é silencioso, "
            f"marcado por 🌲 árvores secas, 🪨 pedras rachadas e antigas bandeiras rasgadas pelo vento."
        ),
        (
            Fore.MAGENTA,
            "😈 A cada passo, o ar fica mais pesado. Ao longe, uma luz vermelha pulsa "
            "entre as ruínas do 🏰 antigo castelo, como se a própria terra estivesse ferida."
        ),
        (
            Fore.CYAN,
            f"🏕️  Depois de horas de caminhada, {nome_jogador} encontra o último acampamento "
            f"dos sobreviventes. Ali estão 👳 mercadores, ⚒️  ferreiros, 🧪 curandeiros e "
            f"aventureiros feridos que tentaram entrar no Abismo, mas poucos conseguiram voltar."
        ),
    ]

    

    for cor, parte in partes:
        dialogo(parte, velocidade=0.03, cor=cor)
        print()

    time.sleep(0.6)
    print(Fore.YELLOW + "─" * 55 + Style.RESET_ALL)
    dialogo("👳 Um velho sentinela se aproxima e diz:", velocidade=0.04, cor=Fore.YELLOW)
    print()
    dialogo(
        '"Então você é o novo escolhido... Escute bem. ⚠️  A partir daqui, '
        'cada exploração pode ser a sua última. Os 👹 monstros ficam mais fortes a cada '
        '⏳ noite, e o Abismo não perdoa os despreparados."',
        velocidade=0.05, cor=Fore.YELLOW
    )
    print()
    dialogo("Ele aponta para uma trilha escura além do acampamento.", velocidade=0.04, cor=Fore.WHITE)
    print()
    dialogo(
        '"Prepare seus ⚔️  equipamentos, compre 🧪 suprimentos se tiver 💰 ouro, '
        'e quando estiver pronto, siga para a entrada do 🔥 Abismo Carmesim. '
        '🏰 Eldoria depende de você."',
        velocidade=0.05, cor=Fore.YELLOW
    )
    print()
    print(Fore.YELLOW + "─" * 55 + Style.RESET_ALL)
    print()
    dialogo(
        f"🌟 {nome_jogador} respira fundo, observa o 🏕️  acampamento pela última vez "
        f"e entende que sua verdadeira jornada começa agora...",
        velocidade=0.05, cor=Fore.GREEN
    )
    print()
    time.sleep(0.5)
    print(Fore.RED + "🔥" * 27 + Style.RESET_ALL)
    print()


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
