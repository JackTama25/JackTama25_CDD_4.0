import random

class Jogando:
    def __init__(self):
        self.opcoes = ["Pedra", "Papel", "Tesoura"]
        self.pontuacao_usuario = 0
        self.pontuacao_computador = 0

    def jogar(self):
        while True:
            usuario = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()
            while usuario not in self.opcoes:
                usuario = input("Opção inválida. Escolha Pedra, Papel ou Tesoura: ").capitalize()

            computador = random.choice(self.opcoes)
            print(f"Computador escolheu {computador}.")

            if usuario == computador:
                print("Empate!")
            elif (usuario == "Pedra" and computador == "Tesoura") or \
                 (usuario == "Papel" and computador == "Pedra") or \
                 (usuario == "Tesoura" and computador == "Papel"):
                print("Você ganhou!")
                self.pontuacao_usuario += 1
            else:
                print("Computador ganhou!")
                self.pontuacao_computador += 1

            print(f"Placar: Você {self.pontuacao_usuario} x {self.pontuacao_computador} Computador")

            jogar_novamente = input("Jogar novamente? (s/n): ").lower()
            while jogar_novamente not in ["s", "n"]:
                jogar_novamente = input("Opção inválida. Jogar novamente? (s/n): ").lower()

            if jogar_novamente == "n":
                break

    def __str__(self):
        return f"Placar final: Você {self.pontuacao_usuario} x {self.pontuacao_computador} Computador"

jogo = Jogando()
jogo.jogar()
print(jogo)
