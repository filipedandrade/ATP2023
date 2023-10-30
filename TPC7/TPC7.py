polinomio1 = [(1,7),(-3.7,4),(5,3),(-88,0)]

polinomio2 = [(2,2),(17,0)]

polinomio3 = [(7,4),(6,3),(-1,2),(43,0)]

polinomio4= [(1,4)]

polinomio5=[(1,2)]

polinomio6=[(1,3)]

def guardarPolinomio(lista, ficheiro):
    file=open(ficheiro,"w")
    for p in lista:
        coeficiente, grau = termo
        file.write(str(coeficiente)+";"+str(grau)+"|")
    file.write("\n")
    file.close()

guardarPolinomio(polinomio, "TPC7POLINOMIO.txt")

def derivadaPolinomio(lista):
    res=[]
    for p in lista:
        pol=[]
        for coeficiente, grau in p:
            coeficiente=coeficiente*grau
            grau=grau-1
            if (coeficiente!=0):
                pol.append(coeficiente,grau)
            res.append(pol)
        return res 
    
    derivadaPolinomio(polinomio)

import matplotlib.pyplot as plt

def graficoPolinomio(p):
    coef=[]
    g=[]
    for termo in p:
        coeficiente, grau =termo
        coef.append(coeficiente)
        g.append(grau)

    x=coef
    y=g
    plt.plot(x,y, market="o")
    plt.xlabel("Coeficientes")
    plt.ylabel("Graus")
    plt.title("Grafico Polinomio")
    plt.show()

    return
graficoPolinomio(polinomio1)

def criarPolinomios():
    polinomio=[]
    i=1
    grau=int(input("INSIRA O MAIOR GRAU DO POLINOMIO"))
    while grau >=0:
        coeficiente=float(input("INTRODUZA O COEFICIENTE DE GRAU"+ str(i)+":"))
        if (coeficiente!=0):
            termo=(coeficiente,grau)
            polinomio.append(termo)
        grau=grau-1
        i=i+1
    return polinomio

def LerPolinomio(ficheiro):
    lista=[]
    file=open(ficheiro,"r")
    for line in file:
        termos=line.split("|")
        polinomio=[]
        for termo in termos:
            if len(t)>1:
                coeficiente =t[0]
                grau=t[1]
                polinomio.append((coeficiente,grau))
        lista.append(polinomio)
    return lista



