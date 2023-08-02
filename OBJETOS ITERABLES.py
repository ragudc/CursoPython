# OBJETOS ITERABLES
# arrays, arreglos, listas, tuplas, diccionarios, sets, objetos iterables
# MÉTODO - 

# TUPLAS
#              0        1           2       3           4
motomami = ("SAOKO", "MOTOMAMI", "CANDY", "DIABLO", "HENTAI")
print(motomami.index("CANDY"))
print(motomami[4])

# FOR - for i in object

for i in motomami :
    print(f"{motomami.index(i)+1}. {i}") # f"VOY A IMPRIMIR LA VARIABLE {X}"

for i in range(6) :
    print(i)


"""LISTAS - []
TUPLAS - ()
DICCIONARIOS - {}"""

# LISTAS
k = ("KIM", "KHLOÉ", "KYLIE", "KENDALL", "KOURTNEY", "KRIS")
kardashians = list() # crear una lista en blanco
kardashians.extend(["KIM", "KHLOÉ", "KYLIE", "KENDALL", "KOURTNEY", "KRIS"])
print(kardashians)

kardashians.remove("KOURTNEY") # elimina la primera ocurrencia de un valor
print(kardashians)

kardashians.pop(3)
print(kardashians)

kardashians.append("BRUCE") # inserta un elemento al final de la lista

kardashians.insert(1, "ROBERT") # agrega elementos en una posición específica
print(kardashians)

kardashians[1] = 1998 # editar un elemento
print(kardashians)
print(len(kardashians))

kardashians.append(k)
print(kardashians)

kardashians.pop()
print(kardashians)

kardashians[kardashians.index(1998)] = "ROB"
print(kardashians)

for i in k :
    kardashians.append(i) # insertar objetos al final de la lista
print(kardashians)

# DICCIONARIOS
emq = {"MALAMENTE":("Augurio", 3.14),
       "QUE NO SALGA LA LUNA":("Boda", 4.15),
       "PIENSO EN TU MIRÁ":("Celos", 2.59),
       1234:("Extásis", 3.02)}
print(emq)

print(emq.get("MALAMENTE"))

# ITEMS - KEYS - VALUES

for k in emq.values() :
    print(k)

