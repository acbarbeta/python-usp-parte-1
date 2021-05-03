# Semana 7

## Exercícios obrigatórios

### Exercício 1
Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.
Por exemplo:

```
digite a largura: 10
digite a altura: 3
##########
##########
##########
```
```
digite a largura: 2
digite a altura: 2
##
##
```

### Exercício 2
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

Por exemplo:

```
digite a largura: 10
digite a altura: 3
##########
#        #
##########
```
```
digite a largura: 2
digite a altura: 2
##
##
```

## Exercícios adicionais (opcionais)

### Exercício 1 - Primos

Escreva a função __n_primos__ que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

Exemplo:
```
>>>n_primos(2)
1
>>>n_primos(4)
2
>>>n_primos(121)
30
```

### Exercício 2 - Soma das hipotenusas
Escreva uma função __soma_hipotenusas__ que receba como parâmetro um número inteiro positivo _n_ e devolva a soma de todos os inteiros entre 1 e _n_ que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.
__Dica1__: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de 1 até _n_ testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.
__Dica2__: primeiro faça uma função __é_hipotenusa__ que diz se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.

Exemplo: 

```
# Para n = 25, as hipotenusas são:
# 5, 10, 13, 15, 17, 20, 25
# note que cada número deve ser somado apenas uma vez. Assim:
soma_hipotenusas(25)
# deve devolver 105
```
