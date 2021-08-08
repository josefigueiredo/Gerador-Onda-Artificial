'''
Created on 22 de mai de 2021

@author: jose
'''
from Harmonica import Harmonica
from typing import List
import numpy

class FormaOnda():
    '''
    classdocs
    '''


    def __init__(self, nAmostras, listaH: List[Harmonica]):
        '''
        Constructor
        '''
        self.__list = listaH
        self.__intervAmostra = 1/60/nAmostras
        self.__fo = numpy.zeros(nAmostras,dtype="float")
        self.__quantHarm = len(listaH)
        self.fazOnda()

    def fazOndaOld(self):
        for i in range(self.__quantHarm):
            for j in range(self.__quantHarm-1, i-1, -1):
                self.__fo += self.__list[j].getValores()

    def fazOndaV2(self):
        for i in range(self.__quantHarm-1,-1,-1):
            self.__fo += self.__list[i].getValores()
            for j in range(i):
                self.__fo += self.__list[j].getValoresSemVDC()

    def fazOnda(self):
        for i in range(self.__quantHarm):
            self.__fo += self.__list[i].getValores()

    def getFO(self):
        return self.__fo

    def getFO2Arduino(self):
        return self.__fo.tolist()

        """
           def __init__(self, nAmostras, listaH: List[Harmonica]):
        self._list = listaH
        self._intervaloAmostra = 1/60/nAmostras
        self._fo = np.zeros(nAmostras, dtype=float)
        self._quantHarm = len(listaH)
    def fazOnda(self):
        for i in range(self._quantHarm):
            for j in range(self._quantHarm-1,i-1,-1):
                self._fo += self._list[j]._valores
    def getFO(self):
        return self._fo

"""
