class Jogo:
    def __init__(self, nome, preco, jogadores, nota):
        self.nome = nome
        self.preco = preco
        self.jogadores = jogadores
        self.nota = nota

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco

    def get_jogadores(self):
        return self.jogadores

    def get_nota(self):
        return self.nota

    def set_nome(self, nome):
        self.nome = nome

    def set_preco(self, preco):
        self.preco = preco

    def set_jogadores(self, jogadores):
        self.jogadores = jogadores

    def set_nota(self, nota):
        self.nota = nota

    def aumentar_preco(self, valor):
        self.preco = self.preco + valor

    def aplicar_desconto(self, porcentagem):
        desconto = self.preco * porcentagem / 100
        self.preco = self.preco - desconto


jogo1 = Jogo("Minecraft", 100.0, 4, 9)
jogo2 = Jogo("GTA V", 120.0, 30, 8)
jogo3 = Jogo("EA FC", 200.0, 2, 7)

print("Jogo 1")
print("Nome:", jogo1.get_nome())
print("Preço:", jogo1.get_preco())
print("Jogadores:", jogo1.get_jogadores())
print("Nota:", jogo1.get_nota())

print("\nJogo 2")
print("Nome:", jogo2.get_nome())
print("Preço:", jogo2.get_preco())
print("Jogadores:", jogo2.get_jogadores())
print("Nota:", jogo2.get_nota())

print("\nJogo 3")
print("Nome:", jogo3.get_nome())
print("Preço:", jogo3.get_preco())
print("Jogadores:", jogo3.get_jogadores())
print("Nota:", jogo3.get_nota())

jogo1.set_nome("Minecraft Java")
jogo1.set_preco(110.0)
jogo1.set_jogadores(8)
jogo1.set_nota(10)

jogo2.set_nome("GTA Online")
jogo2.set_preco(130.0)
jogo2.set_jogadores(32)
jogo2.set_nota(9)

jogo3.set_nome("EA FC 26")
jogo3.set_preco(220.0)
jogo3.set_jogadores(4)
jogo3.set_nota(8)

valor = float(input("\nDigite o valor do aumento: "))
jogo1.aumentar_preco(valor)

print("Novo preço do jogo 1:", jogo1.get_preco())

desconto = float(input("\nDigite a porcentagem de desconto: "))
jogo2.aplicar_desconto(desconto)

print("Novo preço do jogo 2:", jogo2.get_preco())

print("\nDados finais")

print("\nJogo 1")
print(jogo1.get_nome())
print(jogo1.get_preco())
print(jogo1.get_jogadores())
print(jogo1.get_nota())

print("\nJogo 2")
print(jogo2.get_nome())
print(jogo2.get_preco())
print(jogo2.get_jogadores())
print(jogo2.get_nota())

print("\nJogo 3")
print(jogo3.get_nome())
print(jogo3.get_preco())
print(jogo3.get_jogadores())
print(jogo3.get_nota())