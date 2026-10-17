class Produto:
    def __init__(self, nome, preco_compra, preco_venda, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade = quantidade

    def get_nome(self):
        return self.nome

    def get_preco_compra(self):
        return self.preco_compra

    def get_preco_venda(self):
        return self.preco_venda

    def get_quantidade(self):
        return self.quantidade

    def set_nome(self, nome):
        self.nome = nome

    def set_preco_compra(self, preco_compra):
        if preco_compra >= 0:
            self.preco_compra = preco_compra
        else:
            print("Erro: o preço de compra não pode ser negativo.")

    def set_preco_venda(self, preco_venda):
        if preco_venda >= self.preco_compra:
            self.preco_venda = preco_venda
        else:
            print("Erro: o preço de venda não pode ser menor que o preço de compra.")

    def set_quantidade(self, quantidade):
        if quantidade >= 0:
            self.quantidade = quantidade
        else:
            print("Erro: a quantidade não pode ser negativa.")

    def mostra_dados(self):
        print("Nome:", self.nome)
        print("Preço de compra: R$", self.preco_compra)
        print("Preço de venda: R$", self.preco_venda)
        print("Quantidade em estoque:", self.quantidade)

    def aumentar_quantidade(self, aumento):
        if aumento > 0:
            self.quantidade += aumento
            print("Quantidade atualizada com sucesso.")
        else:
            print("Erro: o aumento deve ser maior que zero.")

    def calcular_lucro(self):
        return self.preco_venda - self.preco_compra

    def calcular_valor_estoque(self):
        return self.preco_venda * self.quantidade


def main():
    produto1 = Produto("Teclado", 80.0, 120.0, 10)
    produto2 = Produto("Mouse", 30.0, 50.0, 20)
    produto3 = Produto("Monitor", 600.0, 850.0, 5)
    produto4 = Produto("Fone de ouvido", 45.0, 75.0, 15)

    produtos = [produto1, produto2, produto3, produto4]

    for produto in produtos:
        produto.mostra_dados()
        print("Lucro por unidade: R$", produto.calcular_lucro())
        print("Valor total do estoque: R$", produto.calcular_valor_estoque())
        print()

    print("Consultando os atributos do primeiro produto:")
    print(produto1.get_nome())
    print(produto1.get_preco_compra())
    print(produto1.get_preco_venda())
    print(produto1.get_quantidade())

    print("\nAlterando os atributos do primeiro produto:")
    produto1.set_nome("Teclado Gamer")
    produto1.set_preco_compra(90.0)
    produto1.set_preco_venda(150.0)
    produto1.set_quantidade(12)
    produto1.mostra_dados()

    print("\nTestando o preço de venda com valor válido:")
    produto1.set_preco_venda(160.0)
    print("Preço de venda:", produto1.get_preco_venda())

    print("\nTestando o preço de venda com valor inválido:")
    produto1.set_preco_venda(50.0)
    print("Preço de venda:", produto1.get_preco_venda())

    print("\nTestando o aumento de quantidade:")
    aumento = int(input("Digite a quantidade que deseja adicionar ao estoque: "))
    produto1.aumentar_quantidade(aumento)
    produto1.mostra_dados()


if __name__ == "__main__":
    main()