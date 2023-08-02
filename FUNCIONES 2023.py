# FUNCIONES
# print, insert, len

k = ("KIM", "KHLOE", "KOURTNEY", "KRIS")
motomami = ["SAOKO", "CANDY", "BULERÍAS"]

def longitud(x) : # palabra reservada "def" nombre_funcion(parámetros)
    contador = 0
    for i in x :
        contador += 1
    print(contador)
    return contador

print(f"EL ELENCO DE LAS KARDASHIANS ESTÁ COMPUESTO POR {longitud(k)} PERSONAJES")
print(f"EL DISCO MOTOMAMI TIENE {longitud(motomami)} SENCILLOS")

# EXCEPECIONES
# TRATAMIENTO DE EXCEPCIONES
# CLAÚSULAS try - except

def calculadora() :
    try :
        a = int(input("INGRESE UN NÚMERO - "))
    except ValueError : # CAPTURA UN TIPO DE ERROR
        print("INGRESO LETRAS EN LUGAR DE NÚMEROS")
    except NameError :
        print("LA VARIABLE NO ESTÁ DEFINIDA")
    try :    
        b = int(input("INGRESE OTRO NÚMERO - "))
    except : # CAPTURA CUALQUIER ERROR QUE SE PUEDA PRESENTAR
        print("INGRESO LETRAS EN LUGAR DE NÚMEROS")
    try :
        operación = int(input("INGRESE LA OPERACIÓN A EJECUTAR\n1. SUMA\n1. RESTA\n1. MULTIPLICACIÓN\n1. DIVISIÓN"))
    except :
        print("DEBE INGRESAR EL INDICE DE LA OPERACIÓN QUE DESEA REALIZAR")
    finally :
        print("M DE MOTOMAMI")
    if operación == 1 :
        print(a+b)
    elif operación == 2 :
        print(a-b)
    elif operación == 3 :
        print(a*b)
    elif operación == 4 :
        print(a/b)
    else :
        print("ERROR")

calculadora()