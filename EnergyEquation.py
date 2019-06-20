#coding: utf-8
import subprocess
import sys
import math

arquivoEquation = open('resultsEquation.txt', 'w')
arquivoEquation.write('# Coluna 1 > Time' + "\n")
arquivoEquation.write('# Coluna 2 > Energy consumption' + "\n")

n = 0        # numero de nós (saltos)
p = 0.2818   # potencia
t = 0.020    # tempo em miliseconds
pack = 3     # numero de pacotes transmitidos no intervalo de tempo de analise nas simulações NS
gr = 0.00001 # constante de energia no recebimento de pacotes
gp = 0.95    # constante de energia no processamento de pacotes

n = 1
while (n <= 10):
    eq = ((((math.log10(n) * p) * t) + ((gr * t) * n)) * pack) * gp
    print ("Resp for n=" + str(n) + ": " + str(eq)) 
    arquivoEquation.write(str(n) + ' ' + str(eq) + "\n")

    n=n+1

arquivoEquation.close()