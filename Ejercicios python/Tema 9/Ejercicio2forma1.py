from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

def numerosimpares(x):
    if x % 2 != 0:
        return True

    return False

def numerospares(x):
    if x % 2 == 0 :
        return True
    return False

def suma (a,b):
    print(f"a {a}, b {b}")
    return a+b 

numeros1 = filter(numerosimpares, numeros)
numeros2 = filter(numerospares, numeros)
numeroreducido = reduce(suma, numeros)


print(list(numeros1), "Estas en los numeros impares")
print(list(numeros2), "Estas en los numeros pares")
print(numeroreducido)



