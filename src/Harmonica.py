'''
Created on 21 de mai de 2021

@author: jose
'''
from math import sin, pi
import numpy

class Harmonica():
    '''
    classdocs
    Classe usada para definição e uma harmonica isolada.

    @param vAmplite: amplitude da harmônica
    @param vDC: tensão DC da harmônica
    @param freq: frequencia dessa harmonica
    @param fi: angulo de desasagem dessa harmonica
    @parm nAmostras: quantidade de amostras desse sample (sempre multiplo de 2) 

    '''
    def __init__(self, vAmplitude, vDC, freq, fi, nAmostras):
        '''
        Constructor
        '''
        __intervAmostras = 1/60/nAmostras
        __arr1 = []
        __arr2 = []

        for i in range(nAmostras):
            tAmostras = i*__intervAmostras
            __arr1.append(round(vDC + vAmplitude*sin(2*pi*freq*tAmostras+fi),3))
            __arr2.append(round(vAmplitude*sin(2*pi*freq*tAmostras+fi),3))
        self.__valores = numpy.array(__arr1)
        self.__valoresSemVDC = numpy.array(__arr2)

    def getValores(self):
        return self.__valores

    def getValoresSemVDC(self):
        return self.__valoresSemVDC

