from functools import reduce

resultados = list(filter(lambda x : x % 2 != 0 ,(range(100))))
resultadosreduce = reduce(lambda x , y : x+y , (range(100)))
print(resultados)
print(resultadosreduce)
