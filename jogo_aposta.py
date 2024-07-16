import random

def apostar():
    print("Bem-vindo ao jogo de apostas!")
    saldo = 100  # Saldo inicial do jogador
    
    while True:
        print(f"\nSeu saldo atual é: ${saldo}")
        aposta = int(input("Quanto você quer apostar? (Digite 0 para sair): "))
        
        if aposta == 0:
            print("Obrigado por jogar! Saindo do jogo...")
            break
        elif aposta > saldo:
            print("Aposta inválida! Você não tem saldo suficiente.")
            continue
        
        numero_jogador = int(input("Aposte em um número entre 1 e 10: "))
        
        if numero_jogador < 1 or numero_jogador > 10:
            print("Número inválido! Escolha um número entre 1 e 10.")
            continue
        
        numero_sorteado = random.randint(1, 10)
        print(f"Número sorteado: {numero_sorteado}")
        
        if numero_jogador == numero_sorteado:
            ganho = aposta * 10
            saldo += ganho
            print(f"Parabéns! Você ganhou ${ganho}.")
        else:
            saldo -= aposta
            print("Você perdeu! Tente novamente.")
        
        if saldo <= 0:
            print("Você ficou sem saldo! O jogo acabou.")
            break

if __name__ == "__main__":
    apostar()