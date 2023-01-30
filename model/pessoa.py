from pydantic import BaseModel


class Pessoa(BaseModel):
    nome: str
    fantasia: str | None = None
    tipo: int
    id_nacionalidade: int
    nascimento: str


class Pessoa_Fisica(Pessoa):
    id_sexo: int
    id_etnias: int
    id_tipo_sangue: int
    id_estado_civil: int
