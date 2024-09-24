from banco_imobiliario.config import Configuracao
from banco_imobiliario.entidades import Jogador, Resultado


class Jogo():

    def jogar() -> list:
        resultado = Resultado()

        configuracao = Configuracao()
        tabuleiro = configuracao.montar_tabuleiro()
        dado = configuracao.retorna_dado()
        jogadores = configuracao.retorna_jogadores()

        for rodada in range(1, 1001):
            if tabuleiro.retorna_qtd_jogadores() <= 1:
                break

            for jogador in jogadores:
                if jogador.retorna_em_jogo():
                    casa = jogador.avancar_casas(dado.sortear())
                    propriedade = tabuleiro.retornar_propriedade(casa)
                    jogador.analisar(propriedade)

        resultado.adicionar_vencedor(
            Jogador(rodada, tabuleiro.retornar_vencedor())
        )
        resultado.adicionar_jogadores(tabuleiro.retorna_lista_jogadores())
        print(resultado)

        return resultado.retornar_resultado()
