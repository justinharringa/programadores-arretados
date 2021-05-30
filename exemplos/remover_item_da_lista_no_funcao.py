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

print("-----------outro exemplo-----------")
outra_lista_de_opcoes = [1, 2, 3, 'a', 'b', 'c']


def tirar_uma_coisa(lista, coisa_pra_remover):
    lista.remove(coisa_pra_remover)
    return lista


print(f'lista original: {outra_lista_de_opcoes}')
print(f'primeiro vamos ver o funcao retornar a mesma lista pra usar na hora')
print(f'remove a: {tirar_uma_coisa(outra_lista_de_opcoes, "a")}')
print(f'tb dar pra ver que removeu da lista original: {outra_lista_de_opcoes}')
print(f'remove 1: {tirar_uma_coisa(outra_lista_de_opcoes, 1)}')
print(f'remove c: {tirar_uma_coisa(outra_lista_de_opcoes, "c")}')
