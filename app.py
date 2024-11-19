from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
#restaurante_japa = Restaurante('Sushi' , 'Japonesa')
#restaurante_sorvete = Restaurante('sorvemix' , 'sorvete')
#restaurante_praca.receber_avaliacao('Guilerme', 10)
#restaurante_praca.receber_avaliacao('Julia', 7)

#restaurante_japa.alternar_estados()

bebida_suco = Bebida('Suco de Melancia', 5.0 , 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00 , 'O melhor pãozinho')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

    #Restaurante.lsitar_restaurantes()
    
if __name__ == '__main__':
    main()