class CalculadoraIMC:
    def __init__(self, nome, peso, altura, genero):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.genero = genero

    def calcular_imc(self):
        if self.altura == 0 or self.peso == 0:
            raise ValueError("Altura e peso devem ser diferentes de zero.")
        
        imc = self.peso / (self.altura ** 2)
        return imc

    def classificar_imc(self):
        imc = self.calcular_imc()
        if imc < 17:
            return "Muito abaixo do peso."
        elif 17 <= imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 25:
            return "Peso normal"
        elif 25 <= imc < 30:
            return "Acima do peso"
        elif 30 <= imc < 35:
            return "Obesidade I"
        elif 35 <= imc < 40:
            return "Obesidade II"
        else:
            return "Obesidade III"

    def calcular_peso_ideal(self):
        if self.genero.lower() == "homem":
            return (72.7 * self.altura) - 58
        elif self.genero.lower() == "mulher":
            return (62.1 * self.altura) - 44.7
        else:
            return "Nenhum gênero reconhecido"