import random as r
import math as math
import scipy.integrate as integrate
from matplotlib import pyplot as plot
import numpy as np
#Uniquement quand positive 
def maxFonction(f, a, b):
    ma = 0
    while(a < (b)):
        ma = max(ma, f(a))
        a = x+0.01    
    return ma

def monte(f, a, b, p, d=False):
    iP = []
    sP = []
    iPy = []
    sPy = []
    ma = 0
    if(not d):
        print("Pas strictement croissant")
        ma = maxFonction(f, a, b)
    else:
        print("Strictement croissant")
        ma = f(b)
    print(ma)
    for i in range(p):
        x = r.random()*(b-a)+a
        y = r.random()*ma
        if(x<=b and y<=f(x) and x>=a):
            iP.append(x)
            iPy.append(y)
        else:
            sP.append(x)
            sPy.append(y)
    return [iP, sP,len(iP)/p, (len(iP)/p)*(b-a)*(ma), iPy, sPy]


a = int(input("Borne min : "))
b = int(input("Borne max : "))
cf = input("Fonction ? : ")
t = eval(input("Strictement croissante ? : "))
p = int(input("Nombre de point : "))

f = lambda x: eval(cf)
result = monte(f,a,b,p,t)
i = integrate.quad(f, a, b)[0]
print("Point dans la courbe : " + str(len(result[0])))
print("Point en dehors de la courbe : " + str(len(result[1])))
print("Rapport " + str(result[2]))
print("Aire " + str(result[3]))
print("Erreur relative : " + str(((abs(i-result[3]))/i)))

iPx = result[0]
sPx = result[1]
iPy = result[4]
sPy = result[5]

plot.scatter(iPx, iPy, s=1, color='green')
plot.scatter(sPx, sPy, s=1, color='red')

X = np.linspace(a-1,b+1,256,endpoint=True)
plot.plot(X, f(X))

plot.show()
