'''
Created on 21 de mai de 2021

@author: José de Figueiredo
@email: deb.gnulinux@gmail.com
'''
from Harmonica import Harmonica
from FormaOnda import FormaOnda
import matplotlib.pyplot as plt
from datetime import datetime
from CacluloFFT import CalculoFFT

Amostras = 64
Freq = 60

h60 = Harmonica(5,0,60,0,Amostras)
h120 = Harmonica(2,0,120,0,Amostras)
h180 = Harmonica(1.5,0,180,0,Amostras)
h240 = Harmonica(0.5,0,240,0,Amostras)

listaParaF1 = [h60]
FO_1 = FormaOnda(Amostras,listaParaF1)

listaParaF2 = [h120,h60]
FO_2 = FormaOnda(Amostras,listaParaF2)

listaParaF3 = [h180,h120,h60]
FO_3 = FormaOnda(Amostras,listaParaF3)

listaParaF4 = [h240,h120,h60]
FO_4 = FormaOnda(Amostras,listaParaF4)


f = open("formasGeradas.txt","w")

if __name__ == '__main__':
    f.write(datetime.now().strftime('%d/%m/%Y')+ "\n")

    print("60Hz (5V)")
    print(FO_1.getFO2Arduino())

    f.write("60Hz (5V) \n")
    f.write(str(FO_1.getFO2Arduino())+ "\n")

    print("60 Hz(5v), 120Hz (2v)")
    print(FO_2.getFO2Arduino())

    f.write("60Hz(5V), 120Hz(2v) \n")
    f.write(str(FO_2.getFO2Arduino())+ "\n")

    print("60(5v), 120(2v),180(1.5v)")
    print(FO_3.getFO2Arduino())

    print("60 HZ(5v), 120Hz(2v) 180Hz(1.5v)")
    print(FO_3.getFO2Arduino())

    f.write("60Hz(5V), 120Hz(2v), 180Hz(1.5v)")
    f.write(str(FO_3.getFO2Arduino())+ "\n")

    print("60 HZ(5v), 120Hz (2v), 240Hz (0.5v)")
    print(FO_4.getFO2Arduino())

    f.write("60Hz(5V), 120Hz(2v), 240Hz(0.5v)")
    f.write(str(FO_4.getFO2Arduino())+ "\n")

    f.close()
