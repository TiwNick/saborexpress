from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        '''Construtor para restaurante, categoria e status'''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
 
    def __str__(self):
        '''Funcao para exibir o nome e a categoria do restaurante'''
        return f'{self._nome} | {self._categoria}'
        
    @classmethod
    def listar_restaurantes(cls):
        '''Funcao para listar restaurantes, categoria e status'''
        print(f'{'NOME DO RESTAURANTE'.ljust(25)} | {'CATEGORIA'.ljust(25)} | {'AVALIAÇÃO'.ljust(25)} | {'STATUS'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        '''Funcao para exibir se o restaurante esta ativo ou nao'''
        return '✔️' if self._ativo else '❌'

    def alternar_estado(self):
        '''Funcao para alternar o estado dos restaurantes (mudar o status)'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''Funcao para receber e armazenar a nota do cliente'''
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        '''Funcao para medir a media das avaliacoes'''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media_das_notas = round(soma_das_notas / quantidade_de_notas, 1)
        return media_das_notas

    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)
        
    @property
    def exibir_cardapio(self):
        print(f'Aqui esta o cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1): 
            if hasattr(item, 'descricao'):
                '''Se tiver o atributo descricao, sera um prato, se nao, sera bebida'''
                mensagem_prato = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}\n'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}\n'
                print(mensagem_bebida)
               






