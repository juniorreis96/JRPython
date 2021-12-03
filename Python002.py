nomeusuario = str(input('Olá! Qual seu nome?'))

'''if.elif'''#PROGRAMA DE FINANCIAMENTO QUE A PARTIR DO VALOR DA CASA, SALARIO DO CLIENTE E QTD DE ANOS, SABE SE ELE PODE COMPRAR SEM EXCEDER 30% DE SUA RENDA, CASO EXCEDA... SERÁ NEGADO.
print('Olá! Somos o BANCO SAFIRA, muito prazer em lhe atender!')
casavalor = float(input('Qual o valor do imóvel que deseja financiar?: '))
qtdanos = int(input('Em quantos anos deseja simular seu financiamento?: '))
salario = float(input('Qual o seu salário bruto atual?: '))
limiterenda = salario*0.3
limitefin = limiterenda * qtdanos
minrenda = ((casavalor/qtdanos) / 12) * 3.33
jurosanual = float(input('Qual o % de juros anual?: '))
totalcjuros = casavalor * ((1+(jurosanual/100))**qtdanos)

if minrenda > salario:
    print("""
    Sua renda não é suficiente para financiar um imóvel deste valor.
    Para comprar um imóvel nessa faixa de preço( R${:.2f} ), você precisa de no mínimo
    uma renda de R${:.2f}.
    """.format(casavalor, minrenda))

elif salario > minrenda:
    print("""
    PARABÉNS! Você tem renda o suficiente para financiar o imóvel e realizar
    o sonho da casa própria!
    Para financiar uma casa de R${:.2f}, você precisa de no mínimo R${:.2f} de renda bruta e você
    está dentro do requisito.""".format(casavalor, minrenda))
    print('-=-'*10)
    print("""
    A quantidade total a ser pago ao longo de {} anos será de R${:.2f}
    Sendo: R${:.2f} de valor financiado e R${:.2f} originário de juros.
    """.format(qtdanos, totalcjuros,casavalor, totalcjuros-casavalor))

'''if.elif'''#PROGRAMA QUE COMPARA DOIS NÚMEROS E COMPARE-OS, MOSTRANDO QUEM É MAIOR, MENOR OU NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O número {} é maior que o número {}'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior que o número {}'.format(n2, n1))
else:
    print('Ambos números digitados são iguais')

'''if.elif'''#PROGRAMA QUE LE O SEXO E A IDADE DE UMA PESSOA, SE FOR MASCULINO, INDICAR SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR, SE É A HORA EXATA OU JÁ PASSOU DO PRAZO E QUANTO TEMPO FALTA OU PASSOU DO PRAZO.
sexo = str(input('Qual seu sexo? (M/F): ')).strip().upper()
if sexo == "F":
    print('Você não pode se alistar ao serviço militar das forças brasileiras, desculpe!')
elif sexo == "M":
    idade = int(input('Digite sua idade: '))

    if (idade >= 18) and (idade < 19):
        print("""
        Você está na idade certa para o alistamento!
        Prepare RG e comprovante de residência e vá até 
        o posto de alistamente mais próximo""")
    elif idade < 18:
        print('Você está próximo do ano de alistamento! ')
        falta = 18 - idade
        print('Para que você possa se alistar, você deve esperar {} anos'.format(falta))
    elif idade >= 19:
        print('Você já passou da idade de alistamento!!!')
        passou = idade - 18
        print('Você está {} anos em atraso, vai pagar flexão!'.format(passou))

else:
    print("""
    Você sabe ler e escrever, recruta?
    Por que digitou uma opção inválida? 
    Está com medo?""")



'''if.elif'''#CRIAR UM PROGRAMA QUE LEIA TRES NOTAS DE UM ALUNO, DE PESOS DIFERENTES E QUE MOSTRE SE ELE ESTÁ REPROVADO (<5), RECUPERAÇÃO (>5 E <6.9) OU APROVADO (>=7)
nomealuno = str(input('Digite o nome do aluno que iremos avaliar: ')).upper().strip()
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))
media = ((nota1*0.3) + (nota2*0.3) + (nota3*0.4))
if media > 1 and media < 5:
    print("""
    A média final do aluno {} foi de: {:.2f}.
    Ou seja, ele está reprovado nessa matéria!""".format(nomealuno, media))
elif media >= 5 and media <= 6.9:
    print("""
    A média do aluno {} foi de: {:.2f}.
    Ou seja, ele está de recuperação nessa matéria!""".format(nomealuno, media))
elif media >=7 and media <=10:
    print("""
    ÓTIMO! O aluno {} teve média final de: {:.2f}. 
    Foi muito bem e está APROVADO!
    Deseje a ele boas férias!""".format(nomealuno, media))
elif media > 10 or media < 0:
    print('As médias interidas estão fora do padrão da nossa escola.')


'''if.elif'''#PROGRAMA QUE LE A IDADE DE UM ATLETA E INDIQUE SUA CATEGORIA DE ACORDO COM SUA IDADE: ATÉ 9(MIRIM), ATÉ 14(INFANTIL), ATÉ 19(JUNIOR), ATÉ 20 (SÊNIOR), ACIMA DE 20 (MASTER)
nomeatleta = str(input('Digite seu nome: ')).upper().strip()
idade = int(input('Digite sua idade: '))
if idade <= 9:
    print('{}, sua categoria é "MIRIM"!'.format(nomeatleta))
elif idade > 9 and idade <= 14:
    print('{}, sua categoria é "INFANTIL"!'.format(nomeatleta))
elif idade > 14 and idade <= 19:
    print('{}, sua categoria é "JUNIOR"!'.format(nomeatleta))
elif idade > 19 and idade <= 20:
    print('{}, sua categoria é "SÊNIOR"!'.format(nomeatleta))
else:
    print('Você ta velho demais, vai trabalhar vagaba!')

'''if.elif'''#LER 3 SEGUIMENTOS DE RETAS E INDICAR SE ELAS PODEM FORMAR UM TRIÂNGULO. ALÉM DISSO, DIZER SE É EQUILÁTERO (TODOS OS LADOS IGUAIS), ISÓSCELES (DOIS LADO IGUAS) OU ESCALENO (TODOS OS LADOS DIFERENTES)
r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite uma segunda reta: '))
r3 = int(input('Digite uma terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('As três retas podem formar um triângulo!')
    if r1 == r2 and r1 == r3:
        print('E a denominação desse triângulo é: EQUILÁTERO ')
    elif r1 != r2 and r1 !=r3:
        print('E a denominação desse triângulo é: ESCALENO')
    elif (r1 == r2 or r3) or (r2 == r1 or r3) or (r3 == r1 or r2):
        print('E a denominação desse triângulo é: ISÓSCELES')

else:
    print('Essas 3 retas não podem formar um triângulo!')


'''if.elif'''#LER O PESO E A ALTURA DA PESSOA, CALCULE SEU IMC E MOSTRE SEU STATUS DE ACORDO COM A TABELA: ABAIXO DE 18.5 (ABAIXO DO PESO), ENTRE 18.5 E 25(SOBREPESO), 30 ATÉ 40(OBESIDADE) E ACIMA DE 40 (OBESIDADE MÓRBIDA)
peso = float(input('Qual seu peso em KGs?: '))
altura = float(input('Qual sua altura?: '))
imc = peso / (altura*altura)
if imc <= 16.5:
    print("""
    Peso severamente abaixo do normal!
    Você precisa melhorar sua alimentação!""")
elif imc > 16.5 and imc < 18.5:
    print("""
    Peso abaixo do normal! IMC de {:.2f}
    Ainda não está preocupante, se cuide enquanto é tempo!""".format(imc))
elif imc >=18.5 and imc <=24.99:
    print("""
    NORMAL! IMC de {:.2f}
    PARABÉNS! Você está em seu peso ideal!""".format(imc))
elif imc >= 25 and imc <= 29.99:
    print("""
    PRÉ-OBESO! IMC de {:.2f}
    Cuide de sua saúde, não está ideal!""".format(imc))
elif imc >= 30 and imc <=34.99:
    print("""
    OBESIDADE CLASSE I! IMC de {:.2f}
    Os níveis estão alarmantes, cuide-se!""".format(imc))
elif imc >=35 and imc <=39.99:
    print("""
    PÉSSIMO, OBESIDADE CLASSE II! IMC de {:.2f}
    Muito ruim em, você está um "gordassa"!""".format(imc))
elif imc > 40:
    print("""
    VAI MORRER EM BICHO!
    IMC de {}""".format(imc))

'''if.elif'''#PROGRAMA QUE TEM O PREÇO DO PRODUTO E A PARTIR DA FORMA DE PAGAMENTO, ALTERA O SEU VALOR. A VISTA: 10% DE DESCONTO, A VISTA NO CARTÃO: 5% DE DESCONTO, EM ATÉ 2x NO CARTÃO: PREÇO NORMAL, 3x OU MAIS: 20% DE JUROS.
valorprod = float(input('Olá! Qual o valor do produto que deseja comprar? '))
formapag = str(input("""
Qual a forma de pagamento?
[1] - "A VISTA"
[2] - "PARCELADO".""")).upper().strip()
if formapag == 1:
    print("""O seu produto com valor original deR${}, recebeu um desconto!
    Agora seu valor é de R$ {}!""".format(valorprod, valorprod - (valorprod * 0.1)))
elif formapag == 2:
    qtsx = int(input('Em quantas vezes pretende parcelar? '))
    if qtsx == 1:
        print("""O seu produto com valor original de R${}, recebeu um desconto de 5%!'
              Agora seu valor é de R$ {}!""".format(valorprod, valorprod - (valorprod * 0.05)))
    elif qtsx == 2:
        print("""O seu produto com valor original de R${}, não possui desconto nessa forma de pagamento.
        Ou seja, pague o valor cheio""".format(valorprod))
    elif qtsx >= 3 and qtsx <= 5:
        print("""O seu produto com valor original de R${} terá um acrescimo de 20%
        devido ao parcelamento, ou seja, seu valor final é de R${}""".format(valorprod, valorprod + (valorprod * 0.2)))
else:
    print('Você não digitou uma opção válida!')

'''if.elif'''#UM PROGRAMA QUE JOGUE JOKENPÔ COM VC (PEDRA, PAPEL E TESOURA).
import random
from time import sleep

opcoes = ["PEDRA", "PAPEL", "TESOURA"]
escolhamaquina = random.choice(opcoes)
print(escolhamaquina)
print('-=-' * 10)
print("""
Olá, {}!
Vamos jogar JOKENPÔ?""")
print('-=-'*20)
escolhausuario = str(input('Digite sua escolha: ')).upper().strip()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
print('-=-'*20)
if escolhausuario == "PEDRA" or "PAPEL" or "TESOURA":

    if escolhausuario == "PEDRA" and escolhamaquina == "PEDRA":
        print("""
        A escolha da maquina foi {},
        Vocês empataram!""".format(escolhamaquina))
    elif escolhausuario == "PEDRA" and escolhamaquina == "PAPEL":
        print("""
        A escolha da maquina foi {},
        Você perdeu!""".format(escolhamaquina))
    elif escolhausuario == "PEDRA" and escolhamaquina == "TESOURA":
        print("""A escolha da maquina foi {},
        Você ganhou!""".format(escolhamaquina))

    if escolhausuario == "PAPEL" and escolhamaquina == "PAPEL":
        print("""
        A escolha da máquina foi {},
        Vocês empataram!""".format(escolhamaquina))
    elif escolhausuario == "PAPEL" and escolhamaquina == "TESOURA":
        print("""
        A escolha da máquina foi {},
        Você perdeu!""".format(escolhamaquina))
    elif escolhausuario == "PAPEL" and escolhamaquina == "PEDRA":
        print("""
        A escolha da maquina foi {},
        Você ganhou!""".format(escolhamaquina))

    if escolhausuario == "TESOURA" and escolhamaquina == "TESOURA":
        print("""
        A escolha da máquina foi {},
        Vocês empataram!""".format(escolhamaquina))
    elif escolhausuario == "TESOURA" and escolhamaquina == "PEDRA":
        print("""
        A máquina escolheu {},
        Você perdeu!""".format(escolhamaquina))

    elif escolhausuario == "TESOURA" and escolhamaquina == "PAPEL":
        print("""
        A máquina escolheu {},
        Você ganhou!""".format(escolhamaquina))

if escolhausuario != "PEDRA" and escolhausuario != "PAPEL" and escolhausuario != "TESOURA":
    print("""
    Você não escolheu uma opção válida!""")

'''if.elif'''#PROGRAMA QUE LÊ O NÚMERO INTEIRO E DEIXA QUE O USUARIO ESCOLHA A BASE DE CONVERSÃO. 1 P BINÁRIO, 2 P OCTAL E 3 P HEXADECIMAL
numero = int(input('Escola um número para convertermos: '))
print("""
Olá! Convertemos números inteiros para: 
BINÁRIOS [1]
OCTAL [2]
HEXADECIMAL [3]
""")
escolha = int(input('Digite sua escolha: '))
if escolha == 1:
    print('O número inteiro {}, convertido para BINÁRIO resulta em: {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O número inteiro {} convertido para OCTAL resulta em: {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O número inteiro {} convertido para HEXADECIMAL resulta em: {}'.format(numero, hex(numero)[2:]))
else:
    print('Você não escolheu uma opção válida!')


'''for'''#PROGRAMA QUE FAÇA CONTAGEM REGRESSIVA DE 10 ATÉ 0 COM UMA PAUSA DE 1 SEGUNDO ENTRE OS NÚMEROS
import time

for c in range(10, -1, -1):
   print(c)
   time.sleep(1)
print('FELIZ NATAL !!!')

'''for'''#PROGRAMA QUE MOSTRA TODOS OS NÚMEROS PARES ENTRE 1 E 50
for c in range (2, 51,2):
   print(c)
print('Pronto, estamos mostrando apenas os número pares!')

'''for'''#PROGRAMA QUE FAÇA A SOMA ENTRE TODOS OS NÚMEROS IMPARES QUE SÃO MULTIPLOS DE TRES E QUE SE ENCONTRAM NO INTERVALO DE 1 A 500.
mult3 = 0
descartado = 0
for c in range (1, 501, 2):
   print(c)
   confere = c % 3
   if confere == 0:
       mult3 += c

   if confere != 0:
       descartado += c

print('A soma dos números ímpares que são multiplos de 3 é de {} '.format(mult3))
print('E a soma dos números impares que NÃO são multiplos de 3 é de {}'.format(descartado))

'''for'''#FAÇA UMA TABUADA DE UM NÚMERO ESCOLHIDO PELO USUÁRIO SÓ QUE USANDO O LAÇO "FOR"
numero = int(input('Digite o número que faremos a tabuada: '))
multiplicador = int(input('Digite até qual número deseja fazer a multiplicação: '))
iniciomulti = 1
for a in range (0, multiplicador):
    print("""
{} X {} = {}""".format(numero, iniciomulti, iniciomulti))
    iniciomulti += 1

'''for'''#PROGRAMA QUE LEIA 6 NUMEROS E MOSTRE A SOMA APENAS DAQUELES PARES, DESCONSIDERANDO OS ÍMPARES
soma = 0
soma2 = 0
for a in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
    if numero % 2 != 0:
        soma2 += numero

print('A soma dos números pares digitados é de: {}'.format(soma))
print('A soma dos números ímpares digitados é de: {}'.format(soma2))

'''for'''#DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA P.A (PROGRESSÃO ARITMÉTICA). NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A: '))
for a in range(termo, razao*11, razao):
    print(a)

'''for'''#PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO.
numero = int(input('Digite o número que testaremos para primo: '))
if numero > 1:
    for a in range(2, 500):
        if numero % a == 0:
            print('O número {} não é um número primo!'.format(numero))
            break
        elif numero % a != 0:
            print('O número {} é um número primo!'.format(numero))
            break
else:
    print("""Número inválido!
    Lembrando que: o número digitado deve ser inteiro e maior que 1.""")

'''for'''#PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE É UM PALINDROMO. (SENDO PROIBIDO DIGITAR ACENTOS)
palavra = str(input('Olá, digite uma palavra/frase: ')).upper().strip()
checagem = palavra[::-1]
if palavra == checagem:
    print('Está frase é um palindromo')
else:
    print('A frase digitada não é um palindromo')

'''for'''#PROGRAMA QUE LÊ A DATA DE NASCIMENTO DE SETE PESSOAS E NO FINAL MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES. (MAIORIDADE:21 ANOS)
i1 = 0
i2 = 0
for a in range(0, 7):
    idade = int(input('Qual sua idade?: '))
    if idade >= 21:
        i1 += 1
    if idade < 21:
        i2 += 1

print('O número de pessoas maior de idade é de {}'.format(i1))
print('O número de pessoas menor de idade é de {}'.format(i2))


'''for'''#PROGRAMA QUE LÊ O PESO DE 5 PESSOAS E MOSTRA QUAL FOI O MAIOR E O MENOR PESO
todospesos = []
for a in range(0, 5):
    peso = float(input('Qual seu peso: '))
    todospesos.append(peso)
print('O maior peso é o de {:.1f}kg'.format(max(todospesos)))
print('O menor peso é o de {:.1f}kg'.format(min(todospesos)))

'''for'''#programa que avalia n° de pessoas e retorna: MÉDIA DE IDADE, HOMEM E MULHER MAIS VELHO, QUANTOS MAIOR DE 20 ANOS (HOMEM E MULHER)
qtdavaliada = int(input('Quantas pessoas avaliaremos: '))
qtdhomem = 0
qtdmulher = 0
qtdhomem20 = 0
qtdmulher20 = 0
totalidade = 0
totalidadehomem = 0
totalidademulher = 0
nomehomemvelho = ''
idadehomemvelho = 0
nomemulhervelha = ''
idademulhervelha = 0
for p in range (1, qtdavaliada+1):
    nome = str(input('Digite seu nome: ')).strip().upper()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    print('\n')
    totalidade += idade

    if p == 1:
        idadehomemvelho = 0
        nomehomemvelho = ''
        idademulhervelha = 0
        nomemulhervelha = ''
    if sexo == 'M' and idade > idadehomemvelho:
        idadehomemvelho = idade
        nomehomemvelho = nome
    if sexo == 'F' and idade > idademulhervelha:
        idademulhervelha = idade
        nomemulhervelha = nome
    if sexo == 'M' and idade > 20:
        qtdhomem20 += 1
    if sexo == 'F' and idade > 20:
        qtdmulher20 += 1
    if sexo == 'M':
        qtdhomem += 1
    if sexo == 'F':
        qtdmulher += 1

mediaidade = totalidade / qtdavaliada
print('A média de idade é de {:.1f} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(idadehomemvelho, nomehomemvelho))
print('A mulher mais velha tem {} anos e se chama {}'.format(idademulhervelha, nomemulhervelha))
print('A quantidade de homens analisados foi {} e desses, {} tem acima de 20 anos'.format(qtdhomem, qtdhomem20))
print('A quantidade de mulheres analisadas foram {} e dessas, {} tem acima de 20 anos'.format(qtdhomem, qtdmulher20))

'''while'''#PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE "M" OU "F". CASO ESTEJA ERRADO, DEVE DIGITAR NOVAMENTE.
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
while sexo not in "MF":
    sexo = str(input('Opção inválida, digite novamente: '))
print('Sexo ({}) registrado com sucesso.'.format(sexo))

'''while'''#PROGRAMA QUE PENSA DE UM NÚMERO DE 0 A 10 E PEDE QUE SEJA ADIVINHADO. O JOGADOR TENTA ATÉ ADIVINHAR E NO FINAL MOSTRA QUANTAS TENTATIVAS FORAM NECESSÁRIAS.
from random import choice
acerto = 'N'
tentativas = 1

while acerto == 'N':
    numeromaq = range(0, 11)
    escolhido = choice(numeromaq)
    print('DICA: {}'.format(escolhido))
    adivinha = int(input('Adivinhe o número: '))
    if adivinha == escolhido:
        acerto = 'S'
        print('-=-'*10)
        print('Você acertou, PARABENS!')
        print('O número de tentativas necessárias foram de {}'.format(tentativas))
    else:
        acerto = 'N'
        tentativas += 1
        print('Você errou, o número pensado pela máquina é {} e você digitou {}, tente novamente!'.format(escolhido, adivinha))


'''while'''#MENU QUE PEDE DOIS VALORES E PERGUNTA AO USUÁRIO OQUE ELE DESEJA FAZER COM ELES: SOMA, MULTIPLICAÇÃO, QUAL O MAIOR, DIGITAR NOVOS NÚMEROS OU SAIR DO PROGRAMA.
menu = 'S'
while menu == 'S':
    print('-=-'*15)
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print('-=-'*15)
    print("""MENU DE OPÇÕES:
    [1] - SOMA
    [2] - MULTIPLICAÇÃO
    [3] - SABER O MAIOR
    [4] - DIGITAR NOVOS NÚMEROS
    [5] - SAIR DO PROGRAMA 
    """)
    opcao = int(input('DIGITE UMA OPÇÃO: '))
    if opcao == 1:
        print('A soma de {} + {} resulta em: {}'.format(v1, v2, v1+v2))
        menu = str(input('Quer usar o programa novamente [S/N]?: ').upper())
        if menu == 'N':
            print('Obrigado por usar!')
    if opcao == 2:
        print('A multiplicação de {} x {} resulta em {}'.format(v1, v2, v1*v2))
        menu = str(input('Quer usar o programa novamente [S/N]?: ').upper())
        if menu == 'N':
            print('Obrigado por usar!')
    if opcao == 3:
        if v1 > v2:
            maior = v1
            print('O maior número entre {} e {} é {}'.format(v1, v2, maior))
            menu = str(input('Quer usar o programa novamente [S/N]?: ').upper())
            if menu == 'N':
                print('Obrigado por usar!')
        elif v2 > v1:
            maior = v2
            print('O maior número entre {} e {} é {}'.format(v1, v2, maior))
            menu = str(input('Quer usar o programa novamente [S/N]?: ').upper())
            if menu == 'N':
                print('Obrigado por usar!')
        else:
            print('Os números são iguais, ou seja, não possuimos um maior.')
            menu = str(input('Quer usar o programa novamente [S/N]?: ').upper())
            if menu == 'N':
                print('Obrigado por usar!')
    if opcao == 4:
        print("""
    Você escolheu digitar novos números!
        """)
        print('-=-'*15)
    if opcao == 5:
        menu = 'N'
        print('O jogo acabou!')
    if opcao >= 6:
        print("""
    Você digitou uma opção inválida!
    As opções devem ser entre 1 e 5""")
        print('-=-' * 15)

'''while'''#PROGRAMA QUE LÊ NÚMERO E MOSTRE SEU FATORIAL. CASO O NÚMERO SEJA 5, O FATORIAL FICA - 5*4*3*2*1 = 120 -
'''from math import factorial
n1 = int(input('Digite um número: '))
resultado1 = factorial(n1)
print('O fatorial de {} é {}'.format(n1, resultado1))'''

n1 = int(input('Digite um número: '))
inicio = n1*(n1-1)
contador = inicio
multiplo = n1-2
while multiplo >= 1:
    conta = contador*multiplo
    contador = conta
    multiplo -= 1
print('Resultado: {}'.format(contador))


'''while'''#LER O TERMO E A RAZÃO E MOSTRE OS 10 PRIMEIROS TERMOS DA PROGRESSÃO ARITMÉTICA
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A: '))
qtdtermos = int(input('Quantidade de termos: '))
contador = qtdtermos
while contador > 0:
    print('{}'.format(termo))
    termo += razao
    contador -= 1

'''while'''#MELHORAR O ÚLTIMO PROGRAMA PERMITINDO QUE O USUÁRIO ESCOLHA MAIS TERMOS DA RAZÃO ARITMÉTICA, E SÓ PARA QUANDO O USUÁRIO DIGITAR "0".
termo = int(input('Digite o termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
qtdtermos = int(input('Quantidade de termos iniciais: '))
contador = qtdtermos+1
while qtdtermos > 0:
    print('{}'.format(termo))
    termo += razao
    contador -= 1
    if contador == 1:
        pergunta = str(input('Você gostaria de adicionar mais um termo?[S/N]: ')).upper().strip()
        if pergunta == 'S':
            contador += 1
        if pergunta == 'N':
            print('Ok, obrigado')
            qtdtermos = 0

'''while'''#PROGRAMA LÊ UM NÚMERO E MOSTRA A QUANTIDADE DIGITADA EM UMA SEQUÊNCIA DE FIBONACCI.
'''falhei em realizar'''

'''while'''#PROGRAMA QUE LÊ VÁRIOS NÚMEROS INTEIROS E SÓ PARA QUANDO DIGITADO "999". NO FINAL, MOSTRA QUANTOS NÚMEROS FORAM DIGITADOS E QUAL A SOMA DELES. (DESCONSIDERANDO O "999").
base = 0
qtdnumeros = 0
somanumeros = 0
while base != 999:
    base = int(input('Digite um valor: '))
    qtdnumeros += 1
    somanumeros += base

print('A quantidade de números digitados foi de {} (contando com o 999) e {} sem contar com o último digitado '.format(qtdnumeros, qtdnumeros-1))
print('A soma dos números digitados é de {} (contando com o 999) e  {} sem contar com o último digitado'.format(somanumeros, somanumeros-999))

'''while'''#PROGRAMA QUE LÊ VARIOS NÚMEROS NO TECLADO E MOSTRA MÉDIA, QUAL O MAIOR E MENOR VALOR. A CONDIÇÃO DE PARA É "VOCÊ GOSTARIA DE CONTINUAR DIGITANDO?" E SÓ PARA CASO O USUÁRIO ESCOLHA QUE NÃO.
maior = 0
menor = 9999999999999999999999999999999999999
media = 0
qtdnumeros = 0
somanumeros = 0
menu = 1
while menu == 1:
    numero = int(input('Digite um número: '))
    qtdnumeros += 1
    somanumeros += numero
    media = somanumeros / qtdnumeros
    if numero >= maior:
        maior = numero
    if numero <= menor:
        menor = numero

    menu = int(input("""Gostaria de continuar?
    [1] - SIM
    [2] - NÃO

    DIGITE AQUI: """))
    if menu != 1 and 2:
        menu = 2
print('-=-' * 20)
print('Programa finalizado!')
print('Você digitou um total de {} N°s'.format(qtdnumeros))
print('O menor N° foi: {}'.format(menor))
print('O maior N° foi: {}'.format(maior))
print('A soma dos números foi: {}'.format(somanumeros))
print('A média dos números digitados é: {:.1f}'.format(media))


'''break'''#LÊ UM NÚMERO INFINITO DE N°s E SÓ PARA QUANDO O USUÁRIO DIGITAR "999". NO FINAL, MOSTRE QUANTOS
# FORAM DIGITADOS E QUAL A SOMA ENTRE ELES.
qtd = 0
soma = 0
n = 0
while True:
    n = int(input('Digite um número (999 FINALIZA A OPERAÇÃO): '))

    if n == 999:
        break
    qtd += 1
    soma += n
    print(f'Até agora foram digitados {qtd} N°s e a soma deles é de: {soma} ')
print(('-'*20))
print(f'Pronto! O programa acabou e você digitou um total de {qtd} N°s e uma soma de {soma}')


'''break''' #TABUADA COM QUALQUER NÚMERO ESCOLHIDO O PROGRAMA SÓ PARA QUANDO O VALOR DIGITADO FOR NEGATIVO.
mult = 1
cont = 10
validperg = True
n1 = int(input('Digite um número: '))
while mult <= 10:
    print(f'{n1} x {mult} = {n1*mult}')
    mult += 1
    cont -= 1
    if cont == 0:
        validperg = True
        while validperg == True:
            perg = str(input('Deseja continuar[S/N]: ')).upper().strip()
            if perg == 'S':
                n1 = int(input('Digite um número: '))
                if n1 < 0:
                    print(f"""Você digitou {n1} que é um número negativo.
Não podemos aceitar esse valor!""")
                    break
                mult = 1
                cont = 10
                validperg = False
            elif perg == 'N':
                break
            else:
                validperg = True

print('-'*40)
print('Obrigado por usar nosso programa!')


'''break'''#JOGUE PAR OU IMPAR COM O COMPUTADOR E SÓ É INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL
# DE VITÓRIAS QUE ELE E O COMPUTADOR CONQUISTARAM

print('Vamos jogar PAR OU IMPAR!')
from random import randint
from time import sleep
#variáveis
vicjog = 0
vicpc = 0
jogo = True
#jogo
while jogo == True:
    numeromaquina = randint(0, 5)
    validarnumero = True
    while validarnumero == True:
        numerojogador = int(input('Escolha um número (Entre 0 e 5): '))
        if numerojogador >= 0 and numerojogador <= 5:
            validarnumero = False
        else:
            print('Você digitou um número INVÁLIDO!')
            print('Lembrando que o número digitado deve estar entre 0 e 5.')
            print('='*20)
            sleep(1)

    validarescolha = True
    while validarescolha == True:
        escolhajogador = str(input('P = PAR ou I = ÍMPAR: ')).upper().strip()
        if escolhajogador == 'I' or escolhajogador == 'P':
            validarescolha = False
        else:
            print('Você digitou uma opção INVÁLIDA!')
            print('Lembrando que a opção deve ser P = PAR ou I = ÍMPAR')
            print('='*20)
            sleep(1)

    soma = (numeromaquina + numerojogador) % 2
    if soma == 0:
        resultado = 'P'
        resultado2 = 'PAR'
    else:
        resultado = 'I'
        resultado2 = 'ÍMPAR'

    if resultado == escolhajogador:
        print('Você ganhou!')
        print(f'A maquina digitou {numeromaquina} e você digitou {numerojogador} que somados resultam em um número {resultado2}')
        print('-'*20)
        vicjog += 1
        jogardnv = True
        while jogardnv == True:
            pergunta = str(input('Quer jogar novamente [S/N]?: ')).upper().strip()
            if pergunta == 'N':
                jogo = False
                break
            else:
                print('Ok, vamos de novo!')
                print('-')
                from time import sleep
                sleep(1.5)
                jogardnv = False


    else:
        print('Você perdeu!')
        print(f'A maquina digitou {numeromaquina} e você digitou {numerojogador} que somados resultam em um número {resultado2}')
        vicpc += 1
        break
print('='*20)
print("""O jogo acabou!
""")
print(f'Você ganhou um total de {vicjog} jogos')
print(f'E a maquina ganhou um total de {vicpc} jogos')


'''break'''#LER A IDADE E O SEXO DE VÁRIAS PESSOAS, A CADA CADASTRO PERGUNTAR SE QUER OU NÃO CONTINUAR E NO FINAL
# MOSTRAR: QUANTOS MAIORES DE 18 ANOS, QUANTOS HOMENS E MULHERES CADASTRADOS E QUANTAS MULHERES MENORES QUE 20 ANOS.
from time import sleep

#variáveis
contmaior18 = 0
qtdhomem = 0
qtdmulher = 0
mulhermenor20 = 0
idadetotal = 0
qtdtotal = 0

#cadastro
cadastro = True
while cadastro == True:
    nome = str(input('Digite seu nome: ')).strip().upper()

    validaidade = True
    while validaidade == True:
        idade = int(input('Digite sua idade: '))
        perguntaidade = str(input(f'Você confirma a idade de {idade}?[S/N]: ')).upper().strip()
        if perguntaidade == 'S':
            idadetotal += idade
            if idade > 18:
                contmaior18 += 1
            validaidade = False
        elif perguntaidade == 'N':
            print('Ok, faremos novamente!')
            sleep(1.5)
        if perguntaidade != 'S' and perguntaidade != 'N':
            print('Você digitou uma opção INVÁLIDA! Você deve digitar S= SIM e N= Não.')
            print('Vamos novamente!')
            sleep(1.5)


    validasexo = True
    while validasexo == True:
        sexo = str(input('Digite seu sexo[M/F]: ')).upper().strip()
        perguntasexo = str(input(f'Você confirma o sexo {sexo}? [S/N]: ')).strip().upper()
        if perguntasexo == 'S':
            if sexo == 'M':
                qtdhomem += 1
            elif sexo == 'F':
                qtdmulher += 1
            qtdtotal +=1
            if sexo == 'F' and idade < 20:
                mulhermenor20 += 1
            validasexo = False
        if perguntasexo == 'N':
            print('Ok, vamos novamente!')
            sleep(1.5)
        if perguntasexo != 'S' and perguntasexo != 'N':
            print('Você digitou uma opção INVÁLIDA! Você deve digitar S= SIM e N= Não.')
            print('Vamos novamente!')
            sleep(1.5)

    sleep(1)
    print('-'*20)
    print('Cadastro registrado com sucesso! ')

    novocadastro = True
    while novocadastro == True:
        pergunta = str(input('Gostaria de cadastrar uma outra pessoa? [S/N]: ')).upper().strip()
        if pergunta == 'S':
            novocadastro = False
        elif pergunta == 'N':
            cadastro = False
            break


print('='*30)
print(f"""- {qtdtotal} é o número de pessoas cadastradas
- {qtdmulher} Mulher(es) e {qtdhomem} Homen(s).

- Média de {idadetotal/qtdtotal} anos
- {contmaior18} Pessoa(s) maiores de 18 anos
- {mulhermenor20} Mulher(es) menor(es) que 20 anos""")


'''break'''#LER NOME E PREÇO DE VÁRIOS PRODUTOS, PERGUNTAR SE QUER CONTINUAR OU NÃO A CADA UM E NO FINAL MOSTRAR:
# QUAL É O TOTAL GASTO NA COMPRA, QUANTOS PRODUTOS CUSTAM MAIS DE R$1000,00 E O NOME DO PRODUTO MAIS BARATO.
from time import sleep

qtdproduto = 0
totalcompra = 0
produtomil = 0
nomemaisbarato = ''
maisbarato = 9999999999999

compra = True
while compra == True:
    validacompra = True
    while validacompra == True:
        produto = str(input('Digite o nome de seu produto: ')).upper().strip()
        valorproduto = float(input('Digite o valor do produto: '))
        pergunta = str(input(f"""Deseja confirmar a compra de:
    {produto} por R${valorproduto}?
    [S/N]: """)).upper().strip()
        if pergunta == 'S':
            qtdproduto += 1
            totalcompra += valorproduto
            if valorproduto > 1000:
                produtomil += 1
            if valorproduto < maisbarato:
                nomemaisbarato = produto
                maisbarato = valorproduto
            print('Ótimo, produto registrado!')
            print('-'*10)
            validacompra = False
        elif pergunta == 'N':
            print('Ok, vamos novamente!')
            print('='*40)
            sleep(1.5)
        else:
            print('Você digitou uma opção INVÁLIDA!')
            print('Você deve digitar S= SIM ou N= NÃO.')
            sleep(2)
            print('='*40)

    novoproduto = True
    while novoproduto == True:
        pergunta2 = str(input('Deseja comprar novo produto? [S/N]: ')).upper().strip()
        if pergunta2 == 'S':
            novoproduto = False
        elif pergunta2 == 'N':
            print('Tudo bem, muito obrigado pela preferência!')
            print('Volte sempre!')
            print('='*40)
            print('='*40)
            sleep(2)
            compra = False
            break
        else:
            print('Você digitou uma opção INVÁLIDA!')
            print('Digite S= Sim ou N= Não')
            sleep(1.5)

print(f"""REGISTRO DE COMPRA:
----------------------------------------------------------------------
{qtdproduto} PRODUTOS
R${totalcompra} A PAGAR
{produtomil} produtos acima de R$1000,00.
{nomemaisbarato} é o mais barato no valor de R${maisbarato}.""")
