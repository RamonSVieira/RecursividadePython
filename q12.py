def primo_r(n,d):
  if d == 1: 
    return True
  if n%d==0: 
    return False
  else: 
    return primo_r(n, d-1)

def primo(n):
  if n==1: 
    return False
  return primo_r(n, n-1)

def lista_primos(lista):
  if len(lista) ==0: 
    return []
  primos = lista_primos(lista[:-1])
  if primo(lista[-1]): 
    primos.append(lista[-1])
  return primos

nums = [1,2,3,4,5]
print(lista_primos(nums))