from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        '''Acessa a classe item cardapio e usa os padroes de informacoes dela (nome e preco)'''
        super().__init__(nome, preco)
        self._descricao = descricao


    def __str__(self):
        return self._nome