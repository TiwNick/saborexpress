from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('Praca', 'Gourmet')
bebida_suco = Bebida('Suco de laranja', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_coxinha = Prato('Coxinha de frango', 4.0, 'a melhor coxinha da cidade')
prato_coxinha.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_coxinha)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()