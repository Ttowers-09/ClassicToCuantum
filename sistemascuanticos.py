"""
ESCUELA COLOMBIANA DE INGENIERIA JULIO GARAVITO
Estudiante: Ivan Santiago F. Torres
Docente: Luis Daniel Benavides
Asignatura: CNYT
"""
import numpy as np
import math

def sistema_determinista(v,m,clicks):
    cont = 0
    while cont < clicks:
        result = np.dot(m,v)
        v = np.transpose(result)
        cont += 1
    return v

def sistema_probabilistico(v2, m2, clicks):
    cont = 0
    while cont < clicks:
        result = np.dot(m2, v2)
        v2 = np.transpose(result)
        cont += 1
    return v2

def sistema_cuantico(v3, m3, clicks):
    cont = 0
    while cont < clicks:
        result = np.dot(m3, v3)
        v3 = np.transpose(result)
        cont += 1
    return v3

if __name__ == '__main__':
   v = np.array ([1,0,0,0,0,0])
   m = np.matrix ([[0,0,0,0,0,0],[1,0,0,0,1,0],[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,0,0,0,1],[0,0,1,0,0,0]])
   clicks = 2
   print (sistema_determinista(v,m,clicks))

   #Punto #2 sistema probabilistico
   v2 = np.array ([1,0,0,0,0,0,0,0,0,0,0])
   m2 = np.matrix ([[0,0,0,0,0,0,0,0,0,0,0],[1/3,0,0,0,0,0,0,0,0,0,0],[1/3,0,0,0,0,0,0,0,0,0,0],[1/3,0,0,0,0,0,0,0,0,0,0],[0,1/3,0,0,1,0,0,0,0,0,0],[0,1/3,0,0,0,1,0,0,0,0,0], [0,1/3,1/3,0,0,0,1,0,0,0,0],[0,0,1/3,0,0,0,0,1,0,0,0],[0,0,1/3,1/3,0,0,0,0,1,0,0],[0,0,0,1/3,0,0,0,0,0,1,0],[0,0,0,1/3,0,0,0,0,0,0,1]])
   print (sistema_probabilistico(v2, m2, clicks))

   #Punto #3 sistema de multiples rendijas cuánticas
   v3 = np.array([1,0,0])
   m3 = np.matrix([[1/math.sqrt(2),1/math.sqrt(2),0], [complex(0,-1/math.sqrt(2)),complex(0,1/math.sqrt(2)),0], [0,0,complex(0,1)]])
   print (sistema_cuantico(v3, m3, clicks))
