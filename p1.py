def indice_maior(lst, ind_maior=0, indice=0):
    # Se o vetor estiver vazio, retornar o índice armazenado em ind_maior
    if not lst:
        return ind_maior
    # Se o vetor tiver um elemento, retornar o índice atual
    if len(lst) == 1:
        return indice
    # Verificar se o primeiro elemento é maior do que o elemento armazenado em ind_maior
    if lst[0] > lst[ind_maior]:
        # Atualizar o índice do maior elemento
        ind_maior = indice
    # Verificar se o índice atual é o último índice do vetor
    if indice == len(lst) - 1:
        # Retornar o índice armazenado em ind_maior
        return ind_maior
    # Chamar a função recursivamente passando o vetor sem o primeiro elemento
    # o índice atualizado de ind_maior e o próximo índice
    return indice_maior(lst[1:], ind_maior, indice+1)

print(indice_maior([15, 1, 2, 3, 4, 5]))