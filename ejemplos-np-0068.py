import numpy as np

# lista 
califas = np.array([60, 70, 90])
print(" ----------- ej 1 imprimir califas ----------")
print(califas) # imprime la lista de xcalifa 
print(type(califas)) # muestra el tipo de arreglo 
print(" ----------- ej 0 dimensiones de un array ----------")
califas = np.array(60)
print(califas)
print("dimension : ", califas.ndim)
print(" ----------- ej 1 dimension de un array ----------")
califas = np.array([60, 70, 90])
print(califas)
print("dimension : ", califas.ndim)
print(" ----------- ej 2 dimensiones de un array ----------")
califas = np.array(
    [
        [60, 70, 90],
        [50, 80, 98]
        ]) # un areglo de 2 dimensiones es como una tabla de excel
print(califas)
print("dimension : ", califas.ndim)
print(" ----------- ej 3 dimensiones de un array ----------")
califas = np.array([
    [
        [60, 70, 90],
        [50, 80, 98]
    ],
    [
        [60, 70, 90],
        [50, 80, 98]
    ],
    ]) # un areglo de 3 dimensiones es como una tabla de excel
print(califas)
print("dimension : ", califas.ndim)