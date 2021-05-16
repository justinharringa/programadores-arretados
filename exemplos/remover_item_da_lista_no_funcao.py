# exemplo mostrando como remover uma coisa no função

lista_de_opcoes = ['a', 'b', 'c']


def tirar_da_lista(opcoes):
    opcoes.remove('c')
    print(f"removei 'c'... agora tem: {opcoes}")
    return opcoes


print(f"antes: {lista_de_opcoes}")
# Passei lista_de_opcoes pra tirar_da_lista(opcoes) usar...
# Ele retorna a mesma lista
outra_lista_retornado = tirar_da_lista(lista_de_opcoes)
print(f"depois (original): {lista_de_opcoes}")
print(f"depois (retornado): {outra_lista_retornado}")
