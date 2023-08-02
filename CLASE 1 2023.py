"""# OBJETOS, CLASE
'''VARIABLES
   FUNCIONES - print()'''
# INPUT - PROCESO - OUTPUT
# función(parámetro 1, parámetro 2, ...)
print("Q'HUBO PUES, MOR, POR QUÉ TAN PERDIDITO PUES?") # CONCATENAR
name = 'ANDRÉS'
age = 21
height = 1.68
single = False
print("Hola, mi nombre es "+name,"tengo", age, "años y mido", height, "metros.")"""

# CONDICIONALES - IF
# EDAD - 18+ entra, 18- no entra
# sí - if, sino (en otro caso) - else
# ANIDAR - elif
# BUENAS PRÁCTICAS - MINUSCULAS 
aforo = 0

while aforo<5 :
    print("BIENVENIDOS A VLADIMIR'S")
    print(f"Hay {aforo} personas")
    name = input("Cuál es tu nombre?\n") 
    print("QUE GUSTO TENERTE CON NOSOTROS", name)
    age = int(input("CUÁNTOS AÑOS TIENES? "))
    if age >= 18 :
        while True :
            gender = int(input ("¿CUÁL ES TU GÉNERO? 1. PARCERO 2. PARCERA - "))
            if gender == 1 :
                print("DEBES PAGAR UN COVER DE $30.000, BIENVENIDO PANA!")
                aforo += 1
                break
            elif gender == 2 :
                print("BIENVENIDA, GUAPA, DISFRUTA LA FIESTA!")
                aforo += 1
                break
            else :
                print("ESTAS UN POCO ENFIESTADO, INTENTA DE NUEVO.")
    else :
        print("OOPS! ESTÁS MUY PELA'O PARA ENTRAR, VUELVE CUANDO SEAS MAYOR")


# TEORÍA
"""
1. PROGRAMAR ES SOLUCIONAR PROBLEMAS TECNOLÓGICOS CON INFORMACIÓN - TICS
2. ALGORITMOS SON COMO UN RECETARÍO DE COCINA - SON UNA SERIE DE PASOS ESCRITAS EN UN LP PARA SOLUCIONAR PROBLEMA
3. VARIABLES QUE SON MUTABLES (QUE NO TIENEN UNA NATURALEZA DEFINIDA) - 4 TIPOS DE DATOS (int, str, float, bool)
4. FUNCIONES - PROCESOS EMPAQUETADOS (input, output)
5. IF, ELIF, ELSE
6. WHILE - MIENTRAS
while condición :
    algoritmo
while True :
    break
"""