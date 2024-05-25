class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.andando = False
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo.")
        elif self.andando:
            print(f"{self.nome} não pode comer pois está andando.")
        elif self.falando:
            print(f"{self.nome} não pode comer pois está falando.")
        else:
            print(f"{self.nome} está comendo {alimento}.")
            self.comendo = True

    def parar_comer(self):
        if self.comendo:
            print(f"{self.nome} parou de comer.")
            self.comendo = False
        else:
            print(f"{self.nome} não está comendo.")

    def falar(self):
        if self.falando:
            print(f"{self.nome} já está falando.")
        elif self.comendo:
            print(f"{self.nome} não pode falar pois está comendo.")
        elif self.andando:
            print(f"{self.nome} não pode falar pois está andando.")
        else:
            print(f"{self.nome} está falando.")
            self.falando = True

    def parar_falar(self):
        if self.falando:
            print(f"{self.nome} parou de falar.")
            self.falando = False
        else:
            print(f"{self.nome} não está falando.")

    def andar(self):
        if self.andando:
            print(f"{self.nome} já está andando.")
        elif self.comendo:
            print(f"{self.nome} não pode andar pois está comendo.")
        elif self.falando:
            print(f"{self.nome} não pode andar pois está falando.")
        else:
            print(f"{self.nome} está andando.")
            self.andando = True

    def parar_andar(self):
        if self.andando:
            print(f"{self.nome} parou de andar.")
            self.andando = False
        else:
            print(f"{self.nome} não está andando.")
