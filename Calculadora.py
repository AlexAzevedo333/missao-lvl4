class Calculadora:
    def __init__(self):
        self.__valorA = 0
        self.__valorB = 0
        self.__operacao = ""

    @property
    def valorA(self):
        return self.__valorA

    @valorA.setter
    def valorA(self, valorA):
        self.__valorA = valorA

    @property
    def valorB(self):
        return self.__valorB

    @valorB.setter
    def valorB(self, valorB):
        self.__valorB = valorB

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    # Método para validar a operação
    def validarOperacao(self):
        return self.__operacao in ['+', '-', '*', '/']

    def calcular(self):
        if not self.validarOperacao():
            print("Operação inválida!")
            exit()

        if self.__operacao == '+':
            return self.__valorA + self.__valorB
        elif self.__operacao == '-':
            return self.__valorA - self.__valorB
        elif self.__operacao == '*':
            return self.__valorA * self.__valorB
        elif self.__operacao == '/':
            if self.__valorB == 0:
                print("Divisão por zero não é permitida!")
                exit()
            return self.__valorA / self.__valorB

    def mostrarResultado(self):
        print(str(self.__valorA) + ' ' + self.__operacao + ' ' + str(self.__valorB) + ' = ' + str(self.calcular()))

    def capturarDados(self):
        self.valorA = float(input("Digite o valor A: "))
        self.valorB = float(input("Digite o valor B: "))
        self.operacao = input("Digite a operação (+, -, *, /): ")