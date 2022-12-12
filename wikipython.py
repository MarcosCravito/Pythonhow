#### Tudo sobre estudo de python ###

# Teclas básicas de atalho

# CTRL + / = Comentarios 
# CTRL + B = fecha aba de arquivos do vs code 
# CTRL + Z = Volta texto
# CTRL + Y = Vai para "frente" com o texto alterado
# TAB = espaçamento automatico
# CTRL + A = Seleciona tudo do texto

## repl.it -> emulador de linguagens de programação online !


## Operadores Lógicos ##

# a = 10
# b = 5
# soma = a + b
# subtracao = a - b
# multiplicacao = a * b
# resto = a % b

#Abaixo podemos ver um exemplo por escrito sobre os valores
#.format é para indicarmos o que cada um significa ( indicação de valores ) 
# print('Soma {soma}. \nSubtração {subtracao}'.format(soma=soma,subtracao=subtracao))

## INTERAÇÃO COM USUARIO##

#Podemos verificar que para que o usuario interaja devemos utilizar
#o input(''), logo de antemão devemos declarar o tipo pois dependendo dos
#parametros o python entenderá como uma string, e se nós estivermos
#mexendo com valores devemos fazer como foi realizado a baixo

# int = c = input('Entre com o primeiro valor:')
# int = d = input('Entre com o segundo valor:')

# print('Valor c: {c} valor d: {d}'.format(c=c,d=d))

## OPERADORES LÓGICOS IF/ELSE/ETC... ##

#É MUITO IMPORTANTE RESSALTAR A IDENTAÇÃO 
#PARA INDICAR OS PARAMETROS CORRETAMENTE 
#POIS UMA IDENTAÇÃO INCORRETA LEVARÁ AO NÃO FUNCIONAMENTO ADEQUADO DO CÓDIGO

# e = input('Entre com primeiro valor ')
# f = input('Entre com o segundo valor: ')

# if e > f:
#  print('Valor {e} é maior que {f}'.format(e=e,f=f))

# elif f > e:

#  print('{f} é o maior que {e}'.format(e=e,f=f))

# if e == f:

#   print('Valores iguais')

# else:
#     print('Modo inválido')

## ESTRUTURA DE REPETIÇÃO ##

# FOR:

#IMPRIMIR 100 PRIMEIROS NUMEROS A PARTIR DO 0

# for x in range(100):
#     print(x)

#x é a variavel criada dentro do for
#in ( em )
#range ele irá pegar de 0 a 99 e imprimir os valores sendo
#cada numero colocado na variavel x

#pode ser colocar

# for x in range(1,100)

#neste caso será de 1  a 100

#EXIBIR SE O N° É PRIMO

# a = int (input('Entre com um numero'))
# div = 0
# for x in range(1,a+1):
#     resto = a % x
    
#     if resto == 0:

#         #aqui a baixo por ser reduzido por div +=1 

#         div = div + 1

# if div == 2:
#     print('Numero ({a}) é primo'.format(a))

# else:
#     print('Numero ({a}) não é primo'.format(a))


##WHILE ( ENQUANTO )

#POSSUI O MESMO PRINCIPIO POR EXEMPLO

# while (a <= 10):
#     print(a)
    # a += 1

    ###CRIAR LISTAS####

# listas podem ser inteira,string e etc...

#lista = [1, 3, 5, 7]

# print(lista)  // <- AQUI SERA EXIBIDO OS VALORES

#Como fazer para ele exibir um valor em especifico

# print(lista[1]) -> Dentro do [] podemos colocar a posição do elemento situado na lista

#forma de somar elementos da lista

#podemos usar o for ou

# print(sum(lista))

#podemos tambem identificar valores maiores ou menores

#print(min(lista))
#print(max(lista))

#Saber se já tem algum elemento incluso na lista

#if 'elemento' in lista:
  
    # print('Existe {elemento} na lista'.format{elemento})

# else:
  
    # print('Não existe {elemento} na lista'.format{elemento})

 ## Incluir elementos na lista ##

#  lista.append('elemento')

#  .append é para incluir elementos na lista !

##REMOVER ULTIMO ELEMENTO DA LISTA

#lista.pop()
# print(lista)

#neste caso acima irá exibir a lista sem o ultimo elemento

#TIRAR UM ELEMENTO ESPECÍFICO DA LISTA

#lista.pop(numero da localização do elemento,2,3,4)

#CASO JÁ CONHEÇA O ELEMENTO E QUEIRA REMOVER O MESMO DIRETAMENTE

#lista.remove(elemento)

## ORDENAR LISTA CRESCENTE

# lista.short()

##ORDERNAR LISTA DECRESCENTE

# lista.reverse()


## DIFERENÇA DE DUPLAS PARA LISTAS ##

# LISTAS:

#São possiveis de se alterar, manusear e alterar dados.

#TUPLA: Não conseguimos alterar seus dados, apena criar as mesmas !

#EXEMPLO DE TUPLA

#tupla = (1, 10, 12, 14)
# print(tupla)

##PARA EXIBIR ALGUM VALOR ESPECIFICO
# print(tupla[elemento])

#OBS -> A TUPLA NÃO PODE TER SEUS VALORES ALTERADOS ! 

##MOSTRAR QUANTOS ELEMENTOS TEM NA LISTA E NATUPLA

# print(ten(lista))

## INDICAR O TIPO DE ELEMENTO UTILIZADO ( LISTA, TUPLA ETC..)

# print(type(lista))

## ALTERNAR LISTA PARA TUPLA 
# O IDEAL É CRIAR TUPLA E NÃO ALTERAR PARA LISTA

# lista = list(tupla)

### CONJUNTOS ÁRITMETICOS ###

# {} - > PARA CONJUNTOS UTILIZAMOS CHAVES  !

# conjunto = {1,2,3,4,5}
# print(conjunto)

#No conjunto não pode se repetir um elemento !

## ACRESCENTAR ELEMENTOS NO CONJUNTO

# conjunto.add(elemento)

## REMOVER

# conjunto.discard(elemento)

## UNIÃO DE CONJUNTOS 

# conjuntoum = {1,2,3,4,5}

# conjuntodois = {6,7,8}

# conjuntouniao = conjunto.union(conjunto2)

# print(conjunto.uniao)

## INTERSECÇÃO DE CONJUNTOS ##

# conjuntointerseccao = conjunto.intersection(conjunto2)


## DIFERENÇA (ORDEM DE FATORES ##

# conjunto_diferenca = conjunto.difference(conjunto2)

## DIFERENÇA SIMÉTRICA, ELEMENTO QUE SÓ TEM EM UM CONJUNTO E NÃO EM AMBOS ##

# conjunto_diff_simetrica = conjunto.synmetric_differene(conjunto2)

## PERTINENCIA 

# Retorna se um conjunto é um subconjunto de outro conjunto

#exemplo

# conjunto_a = {1,2,3}
# conjunto_b = {1,2,3,4,5}
# conjunto_subset = conjunto_a.issubset(conjunto_a)
# print(conjunto_subset)

# conjunto_superset = conjunto_b.issuperset(conjunto_b)


## CONVERTER LISTA PARA CONJUNTO

# lista = [1,2,3]
# conjunto = set(lista)

## CONVERTER CONJUNTO PARA LISTA

# list = list(conjunto)