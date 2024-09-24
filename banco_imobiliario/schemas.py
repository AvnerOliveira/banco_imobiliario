from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Response(BaseModel):
    vencedor: str
    jogadores: list[str]
