from fastapi import FastAPI
from model.pessoa import Pessoa_Fisica
from caste.cidade import Cidade

app = FastAPI()


@app.get("/")
def home():
    return "API ON"


@app.get("/cidades")
def get_city(uf: str = ''):
    return Cidade().set_uf(uf).get_cidades()


@app.post("/pessoa/")
def set_people(pessoa: Pessoa_Fisica):
    return {
        "nome": pessoa.nome,
        "idade": pessoa.idade
    }
