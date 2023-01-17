from pydantic import BaseModel

class Pessoa(BaseModel):
    nome: str
    sobrenome: str | None = None

class Pessoa_Fisica(Pessoa):
    idade: int