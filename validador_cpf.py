#isso não tem na udemy, achei bom tentar fazer um do zero da minha maneira
def limpar_cpf(texto):
    cpfCapado = ""
    for i in texto:
        if i.isdigit():
            cpfCapado += i
    return cpfCapado

def verificar_tamanho(cpf):
    if (len(cpf)) != 11:
        print("\ndo tamanho errado")
        return False
    else:
        print("\ndo tamanho certo")
        return True

def calculo_validez(onzeCpf, n):
    n = 1
    numeroConta = None
    for i in range(1, n+1):
        i*=1


cpfDigitado = input(str("Digite o CPF a ser validado: "))
cpfLimpo = limpar_cpf(cpfDigitado)
cpfVerificado = verificar_tamanho(cpfLimpo)

print(cpfDigitado, "é", cpfVerificado)

cpfAceito = (calculo_validez[::-1](cpfVerificado))