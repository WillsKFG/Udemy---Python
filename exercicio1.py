#Estou realizando esse exercício para relembrar coisas que já aprendi anteriomente,
#estou fazendo isso para acompanhar o curso da udemy

#vou fazer de um jeito um pouco mais elaborado que o da aula pra ficar mais produtivo
#desativei completar o código pra não ficar mais fácil
#eu fiz de uma maneira mais estranha pra poder utilizar mais tipos de variáveis

from datetime import date

nome = str("-")
sobnome = str("-")
anoNasc = None
idade = None
altura = None
maiorIdade = None

def nome_completo(nome, sobrenome):
    return nome + " " + sobrenome.title()
def entradaDados():
    global nome, sobnome, anoNasc, altura, idade
    nome = str(input("Digite seu nome: "))
    sobnome = str(input("Digite seu sobrenome completo: "))
    anoNasc = int(input("Digite o ano de seu nascimento: "))
    altura = float(input("Digite sua altura: "))
    idade = date.today().year - anoNasc

entradaDados()

nomeComp = nome_completo(nome, sobnome)

print(f'''
Seu nome completo é: {nomeComp},
Você possui {idade} anos de idade,
E sua altura é {altura}''')

if idade >= 18:
    print("\nVocê é maior de idade!\n")
else:
    print("\nVocê é menor de idade!\n")