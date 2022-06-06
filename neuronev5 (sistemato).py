import math
import random
from typing import Set
#dataset
dataset = [
    [1.5,0.5,1],
    [1.8,0.6,0],
    [1.7,1,0],
    [1.75,0.7,1],
    [1.8,0.9,1],
    [1.6,0.65,1],
    [1.87,0.6,0],
    [1.7,0.95,0]
]

#random
random.seed(1)
w1=0.1
w2=0.1
bias=0.1
TA = 0.1

#defs
def rn(x1,x2,w1,w2,bias):
    t = x1*w1+x2*w2+bias
    return 1/(1+math.exp(-t))

def der_sigmoide(t): #derivata delle sigmoide
    return 1/(1+math.exp(-t)) * (1-1/(1+math.exp(-t)))


#main code
def weight_update(w1,w2,bias): #esegue un aggiornamento dei pesi passando tutti i dati del vettore

    for _set in dataset: 
        a = _set[0]
        b = _set[1]
        va = _set[2]
        previsione = rn(_set[0],_set[1],w1,w2,bias)

        t = a * w1 + b * w2 + bias

        dfcd = 2 * (previsione - va) * der_sigmoide(t)
            
        dfcdw1 = dfcd * a
        w1 = w1 + TA * dfcd*w1

        dfcdw2 = dfcd * b
        w2 = w2 + TA * dfcd*w2

        dfcdb = dfcd
        bias = bias + TA * dfcd*b
    
    print(f"w1: {w1}")
    print(f"w2: {w2}")
    print(f"bias: {b}")

weight_update(random.random(),random.random(),random.random())
a = float(input("Inserisci peso: "))
b = float(input("Inserisci peso forma: "))
previsione = rn(a,b,w1,w2,bias)
print(f"Tentativo: {previsione}")
if previsione >= 0.999:
    print(f"\n\nTrovato: {previsione}")

#for i in range(len(dataset)):
