numeros = [2,4,6,100,200,400,220,340]
for i in range(len(numeros)):
   if numeros[i] > 100:
      print(numeros[i],"Es mayor que 100")
   elif numeros[i] < 100:
      print(numeros[i],"Es menor que 100")
   else:
      print(numeros[i],"Es igual a 100")