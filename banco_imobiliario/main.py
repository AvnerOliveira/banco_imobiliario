from http import HTTPStatus

from fastapi import FastAPI

from banco_imobiliario.jogo import Jogo
from banco_imobiliario.schemas import Response

app = FastAPI()


@app.get('/jogo/simular', status_code=HTTPStatus.OK, response_model=Response)
def executar():
    resultado = Jogo.jogar()
    return resultado
