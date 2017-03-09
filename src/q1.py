'''
Created on 9 de mar de 2017

@author: Pablo (pabloipu@gmail.com)
'''
from math import log

number = int(input("tamanho da mesnsagem"))

bits = int(log(number,2) + 1)

print("Quntidade de bits = {0}". format(bits))