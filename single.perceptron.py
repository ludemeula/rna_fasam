import numpy as np
import matplotlib.pyplot as plt
import random as rand


def plotar(w1,w2,bias,title):
    xvals = np.arange(-1, 3, 0.01)
    newyvals = (((xvals * w2) * - 1) - bias) / w1
    plt.plot(xvals, newyvals, 'r-')
    plt.title(title)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.axis([-1,2,-1,2])
    plt.plot([0,1,0],[0,0,1], 'b^')
    plt.plot([1],[1], 'go')
    plt.xticks([0,1])
    plt.yticks([0,1])
    plt.show()


def ativacao(u):
  return 1 if u > 0 else -1

def saida(entradas, pesos, bias):

  u = 0

  for i in range(len(entradas)):
    u = u + entradas[i] * pesos[i]

  return u + bias

def peso(x, w, alpha):
  for i in range(len(w)):
    w[i] = w[i] + e[i] * alpha * x[i]

def erro(saida_desejada, saida):
   return saida_desejada - saida

def soma(erros):
  soma = 0
  for erro in erros:
    if erro != 0:
      soma = soma + 1
  return soma

#max_it -> número de iteraçoes
#E -> vetor de erros
#alpha -> taxa de aprendizado
#X-> matriz de entradas
#d-> vetor de saida desejada
def perceptron(max_it, E, alpha, X, d):
  w = [rand.random() for i in range(2)] #vetor de pesos
  b = rand.random() #bias
  t = 1 # número de épocas
  N = len(X)

  while t < max_it and E > 0:
    e = []
    for i in range(0, N):
      y = ativacao(saida(X[i], w, b))
      e.append(d[i] - y)
      for index in range(len(w)):
        w[index] = w[index] + e[i] * alpha * X[i][index]
      b = b + alpha * e[i]

    E = soma(e)
    t = t + 1
  return (w, b)


def main():
  X = [[1,1],[1,0],[0,1],[0,0]]
  d = [1,-1,-1,-1]

  w, bias = perceptron(max_it=100, E=1, alpha=.1, X=X, d=d)
  plotar(w[0],w[1],bias,"Porta lógica AND com Perceptron")


if __name__ == '__main__':
  main()
