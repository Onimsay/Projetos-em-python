import random

def jogodobixo(dificuldade):
    print("Bem vindo ao Jogo do Bicho!")
    print(f"Você tem {dificuldade} chutes para acertar um número entre 1 e 100.")
    print("Boa sorte!")

    Nc = random.randint(1, 100)
    chutes = dificuldade

    while chutes > 0:
        Nu = int(input("Digite um número (1 a 100): "))

        if Nu == Nc:
            print("Parabéns! Você acertou!")
            break

        if Nu < Nc:
            if Nc - Nu <= 10:
                print("Chuto baixo mais ta perto")
            else:
                print("Você chutou muito baixo.")
        else:
            if Nu - Nc <= 10:
                print("Chuto alto mais ta perto.")
            else:
                print("Você chutou muito alto.")

        chutes -= 1

    if chutes == 1 and dificuldade == 2:
        print("Dica: " + str())
        
            

    if chutes == 0:
        print(f"Você não acertou. O número era: {Nc}")
        print("Você gostaria de tentar novamente?")
        jogar_novamente = input("Digite 'S' para jogar novamente ou 'N' para sair: ").lower()
        
        if jogar_novamente =='s':
            main()
        
        
def main():
    print("Escolha a dificuldade:")
    print("1. Modo Fácil (30 chutes)")
    print("2. Modo Médio (10 chutes)")
    print("3. Modo Difícil (5 chutes)")
    print("4. Modo Impossível (2 chutes)")

    dificuldade_level = int(input("Digite o número da dificuldade: "))

    if dificuldade_level == 1:
        jogodobixo(30)
    elif dificuldade_level == 2:
        jogodobixo(10)
    elif dificuldade_level == 3:
        jogodobixo(5)
    elif dificuldade_level == 4:
        jogodobixo(2)
    else:
        print("Opção inválida. Por favor, escolha uma dificuldade válida.")
        

if __name__ == "__main__":
    main()
