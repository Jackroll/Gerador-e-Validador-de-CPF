import re

def valida_cpf(cpf):
    cpf = str(cpf)


    cpf=re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) < 11:
        return False

    novo_cpf = cpf[:-2]                             #Recebe o valor digitado menos os dois digitos
    reverso = 10                                    #Variável usada para multiplicar pelos digitos do CPF
    total = 0                                       #Armazena a soma das multiplicações dos digitos do CPF pela variável reverso
    for index in range(19):                         #Laço que faz iteração, 1º de 10 a 2 e 2º de 11 a 2
        if index > 8:                               #enquanto index for menor que 8 faz a 1º iteração
            index -= 9                              #após index for maior que 8 sofre um decrescimo de 9, para recomeçar do 0 e começar a 2º iteração

        total += int(novo_cpf[index])*reverso      #Armazena a soma das multiplicações dos digitos do CPF pela variável reverso
        #x= int(novo_cpf[index])*reverso
        #print(f'{index} * {reverso} = {x}')

        reverso -= 1                                #Decresce uma unidade cada iteração, para fazer a correta multiplicação pelo digito do cpf
        if reverso < 2:                             #quando o reverso passar a ser menor que 2, reverso recebe o valor 11 para começar a 2º itereção
            reverso = 11
            d = 11 - (total % 11)                   #d armazena o resultado da conta 11 - (resto da divisão de total com 11)

            if d > 9:                               #se d for maior que 9, d = digito 1 = 0, caso contrario d = o próprio resultado da conta, d=d
                d = 0
            total = 0
            novo_cpf += str(d)                      #é acrescentado o digito ao valor do CPF, como a variável recebe uma str o valor de 'D' deve ser convertido

    if novo_cpf == cpf:                             # se o valor do novo CPF, for igual ao digitado o CPF é válido
        return True
    else:
        return False


