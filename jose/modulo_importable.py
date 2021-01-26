# -*- coding: utf-8 -*- 

def saludar_modulo(nombre):
    print("Hola {}, esta funcion se ha importado del modulo {},{}".format(nombre,__file__,__name__))

def felicitar_modulo(nombre):
    print("Felicidades {}".format(nombre))

def main():
    saludar_modulo("Tu")
if __name__=="__main__":
    main()
