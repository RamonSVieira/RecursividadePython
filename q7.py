def quantBits(x):
  if x==0:
    return 0
  
  if x==1:
    return 1
  
  return 1+quantBits(x//2)

print(quantBits(32))