def listOrdenada(list):
  if len(list) == 0:
    return []
  if len(list) == 1:
    return True
  if list[-1] > list[-2]:
    return listOrdenada(list[:-1])
  else:
    return False


x = [1,2,3,4,11,6,7,8,9]
print(listOrdenada(x))