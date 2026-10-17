class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def set_nome(self, nome):
        self.nome = nome

    def set_salario(self, salario):
        if salario > 0:
            self.salario = salario
        else:
            print("Erro: o salario deve ser maior que zero.")

    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Salario: R$", self.salario)


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento, bonus, quantidade_funcionarios):
        super().__init__(nome, salario)
        self.departamento = departamento
        self.bonus = bonus
        self.quantidade_funcionarios = quantidade_funcionarios

    def get_departamento(self):
        return self.departamento

    def get_bonus(self):
        return self.bonus

    def get_quantidade_funcionarios(self):
        return self.quantidade_funcionarios

    def set_departamento(self, departamento):
        self.departamento = departamento

    def set_bonus(self, bonus):
        if bonus >= 0:
            self.bonus = bonus
        else:
            print("Erro: o bonus nao pode ser negativo.")

    def set_quantidade_funcionarios(self, quantidade_funcionarios):
        if quantidade_funcionarios >= 0:
            self.quantidade_funcionarios = quantidade_funcionarios
        else:
            print("Erro: a quantidade de funcionarios nao pode ser negativa.")

    def mostrar_dados(self):
        super().mostrar_dados()
        print("Departamento:", self.departamento)
        print("Bonus: R$", self.bonus)
        print("Quantidade de funcionarios:", self.quantidade_funcionarios)

    def calcular_salario_total(self):
        return self.salario + self.bonus
    
    
#main 
#from classes import Funcionario, Gerente


#def main():
#    funcionario1 = Funcionario("Carlos", 2500.0)
#    funcionario2 = Funcionario("Mariana", 3200.0)
#
#    print("=== FUNCIONARIOS ===")
#
#   funcionario1.mostrar_dados()
#   print(funcionario1.get_nome())
#   print(funcionario1.get_salario())
#
#   funcionario1.set_nome("Carlos Silva")
#   funcionario1.set_salario(2800.0)
#   funcionario1.mostrar_dados()
#
#   funcionario2.mostrar_dados()
#    print(funcionario2.get_nome())
#    print(funcionario2.get_salario())
#
#    funcionario2.set_nome("Mariana Souza")
#    funcionario2.set_salario(3500.0)
#    funcionario2.mostrar_dados()

#    gerente1 = Gerente("Roberto", 5000.0, "Tecnologia", 1500.0, 8)
#    gerente2 = Gerente("Fernanda", 6000.0, "Financeiro", 2000.0, 5)
#
#    print("\n=== GERENTES ===")

#    gerente1.mostrar_dados()
#    print(gerente1.get_nome())
#    print(gerente1.get_salario())
#    print(gerente1.get_departamento())
#    print(gerente1.get_bonus())
#    print(gerente1.get_quantidade_funcionarios())

#   gerente1.set_nome("Roberto Lima")
#    gerente1.set_salario(5500.0)
#    gerente1.set_departamento("Desenvolvimento")
#    gerente1.set_bonus(1800.0)
#    gerente1.set_quantidade_funcionarios(10)
#    gerente1.set_bonus(-500.0)
#    gerente1.set_quantidade_funcionarios(-2)
#    gerente1.mostrar_dados()
#    print("Salario total:", gerente1.calcular_salario_total())

#    gerente2.mostrar_dados()
#    print(gerente2.get_nome())
#    print(gerente2.get_salario())
#    print(gerente2.get_departamento())
#    print(gerente2.get_bonus())
#    print(gerente2.get_quantidade_funcionarios())

#    gerente2.set_nome("Fernanda Alves")
#    gerente2.set_salario(6500.0)
#    gerente2.set_departamento("Controladoria")
#    gerente2.set_bonus(2500.0)
#    gerente2.set_quantidade_funcionarios(7)
#    gerente2.mostrar_dados()
#    print("Salario total:", gerente2.calcular_salario_total())

#    print("\n=== TESTE DE HERANCA ===")

#    funcionario1.mostrar_dados()
#    gerente1.mostrar_dados()


#if __name__ == "__main__":
#    main()