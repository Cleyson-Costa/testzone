from fastapi import FastAPI
from model.pessoa import Pessoa_Fisica
from caste.cidade import Cidade
from caste.nacionalidade import Nacionalidade
from caste.pessoaFisica import PessoaFisica

app = FastAPI()


@app.get("/")
def home():
    return "API ON"


@app.get("/cidades")
def get_city(uf: str = ''):
    return Cidade().set_uf(uf).get_cidades()


@app.get("/nacionalidades")
def get_nationality():
    return Nacionalidade().get_nacionalidades()


@app.post("/pfisica/")
def set_people(pessoa: Pessoa_Fisica):
    return PessoaFisica() \
        .setNome(pessoa.nome) \
        .setFantasia(pessoa.fantasia) \
        .setIdNascionalidade(pessoa.id_nacionalidade) \
        .setNascimento(pessoa.nascimento) \
        .setIdSexo(pessoa.id_sexo) \
        .setIdEtinias(pessoa.id_etnias) \
        .setIdTipoSangue(pessoa.id_tipo_sangue) \
        .setIdEstadoCivil(pessoa.id_estado_civil)

@app.get("/pfisica/")
def get_people(pessoa: Pessoa_Fisica):
    return PessoaFisica() \
        .setNome(pessoa.nome) \
        .setFantasia(pessoa.fantasia) \
        .setNascimento(pessoa.nascimento) \
        .get_pessoas()