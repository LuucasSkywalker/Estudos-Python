# print("HELLO WORLD")
# x = 10
# print(x)
# nome = 'Lucas'
# nota = 8.8
# print(type(nota))

#Nota_1 = int(input())

a = 1
b = 2
print(b > a ) 
print(type(b))



idade = 16
if idade < 18:
     print("Menor de Idade")
elif idade >= 18 and idade < 65:
     print("Adulto")
else:
     print("Idoso")


#Estrutura de repetição FOR
numeros = [1, 2, 3, 4, 5],
for num in numeros:
     print(num)


#função range() uma ferramenta util pra criar seguências númericas .
for x in range(8):
    print(x)
#Limites inicial e superior em range(parâmetros)
for y in range(2, 7):
    print(y)
 #Resutado da saída será:
 #2
 #3
 #4
 #5
 #6

 #break para controlar iterações de repetição
for numero in range(1, 11): #paramentos no range()fazendo um lop for
    if numero % 2 == 0:  #condição 
        print(numero)
        break  #vai parar a repetição até o número par se atendida
 #a saída será: o primeiro número par encontrado é: 2
 #Nesse exemplo, o loop “for” itera de 1 a 10, mas, assim que encontra o primeiro
 #  número par (2), o comando “break” é acionado. Desse modo, interrompe-se a 
 # execução do loop.


def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(5.6) / len(7.8)

      
    
    media = 8.5

#if media >= 9:
    print("Excelente")
#elif media >= 7 and media < 9:
    print("Bom")
#else:
    print("Precisa melhorar")

    #--------------------------------------------------

    notas = [7.5, 8.0, 0, 9.0]

if not any(nota == 0 for nota in notas):
    print("Nenhuma nota é 0, executando o bloco de código.")
    # Coloque aqui o bloco de código que você deseja executar
else:
    print("Existe uma nota igual a 0, bloco de código não executado.")

    #----------------------------------

def Inserir_Notas():                                           
    ValorNotas = []
    while True:
        nota = float(input("Coloque suas Notas ==> "))
        if len(ValorNotas) == 5:
            break
        ValorNotas.append(nota)
    return ValorNotas

def Medias_Aluno(ValorNotas):
    if not any(nota == 0 for nota in ValorNotas):
      return sum(ValorNotas) / len(ValorNotas)
    else:
      return "Existe uma nota igual a 0, bloco de código não executado."

def condicao_MediaAluno(MediaNotas):
    if MediaNotas >= 8.7:
        return "Quadro de Honra, NOTA EXCELENTE"  
    elif MediaNotas >= 7 and MediaNotas < 8:
        return "Parabéns você foi aprovado"
    else:
        return "Reprovado, estude mais"


def Relatorio_Notas(ValorNotas, MediaNotas, situacao):
    print("\nRelatório Final")
    print("Notas:", ValorNotas)
    print(f"Média: {MediaNotas:.2f}")
    print("Situação:", situacao)

def main():
    print("Insira sua NOTA por favor")
    ValorNotas = Inserir_Notas()
    MediaNotas = Medias_Aluno(ValorNotas)
    situacao = condicao_MediaAluno(MediaNotas)
    Relatorio_Notas(ValorNotas, MediaNotas, situacao)    

if __name__ == "__main__":
    main()


def soma(a,b):
    resultado = a+b
    return print(resultado)

somaRes = soma(5,5)
#ou soma(5,5) igual no JS

cores = ['preto', 'azul', 'verde', 'amarelo', 'vermelho']
for cor in cores:
 print(f'Posição = {cores.index(cor)},{cor}')

 #classes em python e herança 

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
 
    def acelerar(self, incremento):
        self.velocidade += incremento
 
    def frear(self, decremento):
        self.velocidade -= decremento
 
    def status(self):
         return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade:{self.velocidade} km/h'
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia
    def acelerar(self, incremento):
 # Carros podem acelerar mais rápido.
        self.velocidade += incremento + self.potencia
class Bicicleta(Veiculo):
      def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo
      def status(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Tipo: {self.tipo},Velocidade: {self.velocidade} km/h'
 # Criando objetos
carro1 = Carro('Toyota', 'Corolla', 2022, 150)
bicicleta1 = Bicicleta('Trek', 'Mountain Bike', 2021, 'MTB')
# Acelerando e veri cando o status
carro1.acelerar(50)
bicicleta1.acelerar(20)
# Exibindo o status dos veículos
print('Status do Carro:')
print(carro1.status())
print('\nStatus da Bicicleta:')
print(bicicleta1.status())
