# -*- coding: utf-8 -*-
"""calculadora.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v_hf9D9x2wvJ9qcvffAxUviUJAWctrz3

#Calculadora
"""

while True:
  start = print("Vamos Calcular!") #Iniciando a calculadora.

  primeiroNumero = int(input("Digite um número inteiro: ")) #Inserindo o primeiro valor numérico.

  operador = input("Digite uma operação: \n + somar\n - subtrair\n * multiplicar \n / dividir\n") #Inserindo a operação aritmética.

  segundoNumero = int(input("Digite outro número inteiro: ")) #Inserindo o segundo valor numérico.

  if operador == "+":
    print(primeiroNumero + segundoNumero) #Se o operador for igual a "+", a soma dos valores é retornada.
  elif operador == "-":
    print(primeiroNumero - segundoNumero) #Se o operador for igual a "-", a subtração dos valores é retornada.
  elif operador == "*":
    print(primeiroNumero * segundoNumero) #Se o operador for igual a "*", a multiplicação dos valores é retornada.
  elif operador == "/":
    print(primeiroNumero / segundoNumero) #Se o operador for igual a "/", a divisão dos valores é retornada.
  else :
    print("Operação incorreta!") #Se o operador for diferente das 4 opções acima, a calculadora retorna que a operação está incorreta e encerra o programa.
  break