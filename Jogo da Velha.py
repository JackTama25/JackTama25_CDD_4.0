class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [" " for _ in range(9)]
        self.jogador_atual = "X"

    def imprimir_tabuleiro(self):
        for linha in range(3):
            print("|".join(self.tabuleiro[linha*3:(linha+1)*3]))
            if linha < 2:
                print("-----")

    def verificar_vencedor(self, jogador):
        combinacoes_vencedoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]
        ]
        for combinacao in combinacoes_vencedoras:
            if all(self.tabuleiro[i] == jogador for i in combinacao):
                return True
        return False

    def tabuleiro_cheio(self):
        return all(celula != " " for celula in self.tabuleiro)

    def fazer_movimento(self, posicao):
        if self.tabuleiro[posicao] == " ":
            self.tabuleiro[posicao] = self.jogador_atual
            return True
        return False

    def trocar_jogador(self):
        self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def jogar(self):
        while True:
            self.imprimir_tabuleiro()
            try:
                movimento = int(input(f"Jogador {self.jogador_atual}, digite seu movimento (1-9): ")) - 1
                if self.fazer_movimento(movimento):
                    if self.verificar_vencedor(self.jogador_atual):
                        self.imprimir_tabuleiro()
                        print(f"Jogador {self.jogador_atual} vence!")
                        break
                    elif self.tabuleiro_cheio():
                        self.imprimir_tabuleiro()
                        print("Empate!")
                        break
                    self.trocar_jogador()
                else:
                    print("Célula já está ocupada. Tente novamente.")
            except (ValueError, IndexError):
                print("Movimento inválido. Tente novamente.")

jogo = JogoDaVelha()
jogo.jogar()
