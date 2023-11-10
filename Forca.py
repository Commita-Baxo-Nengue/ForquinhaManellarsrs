import random


def escolher_palavra(palavras):
    return random.choice(palavras).upper()


def inicializar_jogo():
    print("♡.﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀.♡*")
    print("       Bem-vindo ao jogo da Forca!\n")
    print(
        "‧̍̊·̊‧̥°̩̥˚̩̩̥͙°̩̥‧̥·̊‧̍̊ ♡ °̩̥˚̩̩̥͙°̩̥ ·͙*̩̩͙˚̩̥̩̥*̩̩̥͙·̩̩̥͙*̩̩̥͙˚̩̥̩̥*̩̩͙‧͙ °̩̥˚̩̩̥͙°̩̥ ♡ ‧̍̊·̊‧̥°̩̥˚̩̩̥͙°̩̥‧̥·̊‧̍̊ \n"
    )


def jogar_forca(palavra_sorteada, dicas):
    vidas = 6
    letras_erradas = []
    letras_corretas = []
    espacos = ['_'] * len(palavra_sorteada)

    print(f'\nIsso é um jogo de forca e você possui {vidas} vidas')

    while vidas > 0 and ''.join(espacos) != palavra_sorteada:
        print("\nPalavra:", ' '.join(espacos))
        print("Vidas restantes:", vidas)

        print("Letras erradas:", ', '.join(letras_erradas))

        escolha = input(
            '\nDigite uma letra ou "DICA" para receber uma dica: ').upper()

        if escolha == "DICA":
            dica = dicas[palavra_sorteada]
            print(f"Dica: {dica}")
            continue

        # caso o jogador insira mais de uma letra
        if len(escolha) != 1 or not escolha.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        if escolha in letras_erradas or escolha in letras_corretas:
            print('Você já tentou essa letra.')
        elif escolha in palavra_sorteada:
            print('Parabéns, você acertou uma letra!')
            for i in range(len(palavra_sorteada)):
                if escolha == palavra_sorteada[i]:
                    espacos[i] = escolha
            letras_corretas.append(escolha)
        else:  # adicionar letras erradas na lista de letras erradas e tirar 1 vida.
            print('Você errou a letra.')
            letras_erradas.append(escolha)
            vidas -= 1

    if ''.join(espacos) == palavra_sorteada:
        print("VOCÊ GANHOU ٩ʕ◕౪◕ʔو ! ! ")
        print("A palavra era:", palavra_sorteada)
    else:
        print(f'GAME OVER! Tente novamente. A palavra era: {palavra_sorteada}')


if __name__ == "__main__":
    palavras = {
        "VALORANT": "FPS ruim.",
        "MINECRAFT": "Um famoso jogo sandbox de construção.",
        "FORTNITE": "Battle royale de cria(ança).",
        "NIOH": "Souls like muito difícil.",
        "PONG": "Um dos primeiros jogos eletrônicos do mundo.",
        "LOL": "Jogo de esquisito.",
        "TETRIS": "Jogo de empilhar blocos.",
        "APEX": "Tipo fortnite mas de nerd.",
        "CSGO": "FPS bom.",
        "HEARTHSTONE": "Jogo de cartas que ninguém joga.",
        "DOTA": "Lol só que pior ainda.",
        "ROBLOX": "Jogo de criança mas bom.",
        "CROSSFIRE": "FPS muito bom.",
        "OVERWATCH": "FPS de poderzinho bom",
        "GTA": "Oh shit here we go again.",
        "BIOSHOCK": "Jogo com estilo muito art deco.",
        "CUPHEAD": "Chicrinho e Caneco.",
        "CIVILIZATION": "Sid Meier criou.",
        "UNDERTALE": "Tem uma fanbase esquisita.",
        "CELESTE": "Jogo da menininha que tem crises + polvo.",
        "HADES": "Jogo de dungeon muito bom.",
        "DETROIT": "Jogo de escolha de robôs triste.",
        "BLOODBORNE": "Jogo de nerd MUITO NERD.",
        "SEKIRO": "Jogo de samurai muito louco.",
        "STRAY": "GTA de gatinhos fofos",
        "PUBG": "Fortnite sem graça",
        "DAYZ": "Zumbi",
        "PERSONA": "Jogo de anime que ninguém joga",
        "FNAF": "5 noites com frederico",

    }

    palavra_sorteada = escolher_palavra(list(palavras.keys()))
    inicializar_jogo()
    jogar_forca(palavra_sorteada, palavras)