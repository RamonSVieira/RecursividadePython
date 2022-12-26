def quantDivisores(n, d):
  if n==0:
    return 0
  if d==1:
    return [1]
  elif n%d!=0:
    return quantDivisores(n, d-1)
  else:
    return [d] + quantDivisores(n, d-1)


x = int(input())
print(quantDivisores(x, x))