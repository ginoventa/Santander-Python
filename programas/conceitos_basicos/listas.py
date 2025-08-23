nomes = list("python")
frutas = ["uva","banana","pera"]
for indice, fruta in enumerate(frutas): 
    print(f"{indice}: {fruta}")
print()

numeros = [1,2,3,4]
numerosss = numeros.copy()
quadrado = [numero**2 for numero in numeros]
print(quadrado, numerosss,1)
print(nomes, frutas) 
carros = ("gol",) 
print(isinstance(frutas, tuple))