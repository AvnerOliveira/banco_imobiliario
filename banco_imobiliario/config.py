from banco_imobiliario.entidades import (
    Aleatorio,
    Cauteloso,
    Dado,
    Exigente,
    Impulsivo,
    Propriedade,
    Tabuleiro,
)


class Configuracao:
    def __init__(self) -> None:
        self.__propriedades = Propriedade.gerar_lista_propriedades(20)
        self.__tabuleiro = Tabuleiro(self.__propriedades)
        self.__dado = Dado()
        self.__jogadores = [
            Impulsivo(self.__tabuleiro), Exigente(self.__tabuleiro),
            Cauteloso(self.__tabuleiro), Aleatorio(self.__tabuleiro)
        ]
        self.__tabuleiro.adicionar_jogadores(self.__jogadores)

    def montar_tabuleiro(self) -> Tabuleiro:
        return self.__tabuleiro

    def retorna_jogadores(self) -> list:
        return self.__jogadores

    def retorna_dado(self) -> Dado:
        return self.__dado
