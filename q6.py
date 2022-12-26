def somaPares(list, soma = 0):
  if len(list) == 0:
    return 0
  
  if list[0] % 2 == 0:
    soma += list[0]
  
  return soma + somaPares(list[1:])

x = [1,2,3,4,5,6,7,8,9,10]
print(somaPares(x))