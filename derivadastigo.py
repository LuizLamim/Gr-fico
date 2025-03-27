import sympy as sp

def calcular_derivada_trigonometrica(funcao, variavel):
  """
  Calcula a derivada de uma função trigonométrica em relação a uma variável.

  Args:
    funcao: A função trigonométrica como uma string.
    variavel: A variável em relação à qual a derivada será calculada.

  Returns:
    A derivada da função como uma string.
  """

  x = sp.symbols(variavel)
  funcao_sympy = sp.sympify(funcao)
  derivada = sp.diff(funcao_sympy, x)
  return str(derivada)

# Exemplos de uso
funcao1 = "sin(x)"
variavel1 = "x"
derivada1 = calcular_derivada_trigonometrica(funcao1, variavel1)
print(f"A derivada de {funcao1} em relação a {variavel1} é: {derivada1}")

funcao2 = "cos(2*x)"
variavel2 = "x"
derivada2 = calcular_derivada_trigonometrica(funcao2, variavel2)
print(f"A derivada de {funcao2} em relação a {variavel2} é: {derivada2}")

funcao3 = "tan(x**2)"
variavel3 = "x"
derivada3 = calcular_derivada_trigonometrica(funcao3, variavel3)
print(f"A derivada de {funcao3} em relação a {variavel3} é: {derivada3}")

funcao4 = "sec(x) + csc(x)"
variavel4 = "x"
derivada4 = calcular_derivada_trigonometrica(funcao4, variavel4)
print(f"A derivada de {funcao4} em relação a {variavel4} é: {derivada4}")

funcao5 = "cot(x) * sin(x)"
variavel5 = "x"
derivada5 = calcular_derivada_trigonometrica(funcao5, variavel5)
print(f"A derivada de {funcao5} em relação a {variavel5} é: {derivada5}")