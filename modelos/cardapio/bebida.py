from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        '''Acessa a classe item cardapio e usa os padroes de informacoes dela (nome e preco)'''
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome