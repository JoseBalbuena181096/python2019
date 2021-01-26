# -*- coding: utf-8 -*- 
#The imports are add in the start
import sys
from modulo_importable import saludar_modulo

def parsear_argumentos_basicos():
    argumentos = sys.argv[1:]
    return argumentos

def main(argumentos):
    """
    Inside we put our main funtionality of our scritp 
    """
    if argumentos[0]=="saludar":
        nombre = argumentos[1]
        saludar_modulo(nombre)

if __name__=="__main__":
    #this code is ejecuted if run this 
    argumentos = parsear_argumentos_basicos()
    print("argumentos pasados al script: ",argumentos)
    main(argumentos)
