import numpy as np

print(" -----------llenar matriz de ceros--------------")
matriz=np.zeros([2,3]) # 3 filas X 5 columnas
print(matriz)
print(" -----------llenar matriz de unos--------------")
matriz=np.ones([3,5])
print(matriz)
print(" -----------llenar lista vacios--------------")
matriz=np.empty([3,5])
print(matriz)
print(" -----------llenar lista con rango--------------")
# el primer parametro es el valor inicial 
# el segundo parametro es el valor final 
# el tercer parametro es el incremento
lista=np.arange(0,10,2)
print(lista)
print(" -----------llenar lista con rango 2--------------")
lista=np.arange(0,10,1)
print(lista)
