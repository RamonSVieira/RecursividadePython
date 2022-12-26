def quantDivisores(n, d):
  if n==0:
    return 0
  if d==1:
    return 1
  elif n%d!=0:
    return quantDivisores(n, d-1)
  else:
    return 1+quantDivisores(n, d-1)

def verificaPrimo(y):
  if y == 0 or y==1:
    return "Não Primo"
  if quantDivisores(y, y)>2:
    return "Não Primo"
  else:
    return "Primo"

x = int(input())
print(verificaPrimo(x))