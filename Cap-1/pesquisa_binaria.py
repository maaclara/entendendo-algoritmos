def pesquisa_binaria(lista, item):
    posicaoMaisBaixa = 0  # ❶
    posicaoMaisAlta = len(lista) - 1  # ❶

    while posicaoMaisBaixa <= posicaoMaisAlta:  # ❷
        meio = (posicaoMaisBaixa + posicaoMaisAlta) // 2  # ❸
        chute = lista[meio]

        if chute == item:  # ❹
            return meio
        if chute > item:  # ❺
            posicaoMaisAlta = meio - 1
        else:  # ❻
            posicaoMaisBaixa = meio + 1

    return None  # ❼


def main():
    minha_lista = [1, 3, 5, 7, 9]  # ❽
    print(pesquisa_binaria(minha_lista, 3))  # => 1 ❾
    print(pesquisa_binaria(minha_lista, -1))  # => None ❿


if __name__ == "__main__":
    main()