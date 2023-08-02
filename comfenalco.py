cursos = [("PYTHON", 6), ("PHP", 6), ("JAVA", 6), ("BLOCKCHAIN", 8), ("INGLÉS", 4), ("HABILIDADES BLANDAS", 2)]

def inscribirAlumnos() :
    alumnos = list()
    print("BIENVENIDO AL SISTEMA DE INSCRIPCIÓN DE ALUMNOS")
    flag = True
    while flag :
        alumno = list()
        nombre = input("INGRESE EL NOMBRE COMPLETO DEL ESTUDIANTE, SI DESEA DEJAR DE INSCRIBIR DIGITE 0: ")
        if nombre == "" :
            print("DEBE INGRESAR VALORES, INTENTE DE NUEVO")
        elif nombre == "0" :
            flag = False
        else :
            alumno.append(nombre)
            alumnos.append(alumno)
    return alumnos

def mostrarCursos() :
    for i in cursos :
        print(f"{cursos.index(i)}. {i[0]} - {i[1]}")

def inscribirCursos(listaAlumnos=list()) :
    for i in listaAlumnos :
        for j in range(3) :
            mostrarCursos()
            print(f"ESTUDIANTE - {i[0]}")
            while True :
                x = int(input("DIGITE EL CÓDIGO DEL CURSO A MATRICULAR : "))
                try :
                    i.append(list(cursos[x]))
                    break
                except IndexError :
                    print("INGRESE UN CÓDIGO DE CURSO VÁLIDO!")
    return listaAlumnos
    

print(inscribirCursos(inscribirAlumnos()))








            
    