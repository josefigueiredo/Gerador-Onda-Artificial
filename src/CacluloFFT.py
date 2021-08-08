'''
Created on 26 de mai de 2021

@author: jose
'''
from numpy import fft
from FormaOnda import FormaOnda


class CalculoFFT():
    '''
    classdocs
    '''
    def __init__(self, fo: FormaOnda):
        '''
        Constructor
        '''
        self.__fft = fft.fft(fo.getFO(),64,norm="forward")
        
        
    def obterFFT(self):
        return self.__fft
        
        