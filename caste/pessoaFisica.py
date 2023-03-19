from crud.connection import Connection
from caste.pessoa import Pessoas


class PessoaFisica(Pessoas):

    def __init__(self):
        super().__init__()
        self.setTipo(1)
        self.__id_sexo = 0
        self.__id_etnias = 0
        self.__id_tipo_sangue = 0
        self.__id_estado_civil = 0

    def getIdSexo(self):
        return self.__id_sexo

    def setIdSexo(self, value: int):
        self.__id_sexo = value
        return self

    def getIdEtnias(self):
        return self.__id_etnias

    def setIdEtinias(self, value: int):
        self.__id_etnias = value
        return self

    def getIdTipoSangue(self):
        return self.__id_tipo_sangue

    def setIdTipoSangue(self, value: int):
        self.__id_tipo_sangue = value
        return self

    def getIdEstadoCivil(self):
        return self.__id_estado_civil

    def setIdEstadoCivil(self, value: int):
        self.__id_estado_civil = value
        return self

    def get_pessoas(self):
        limit = 0
        if self.getNome() == '' \
                and self.getFantasia() == '' \
                and self.getNascimento() == '':
            limit = 10

        """ # TODO
            Where:
                nome
                fantasia
                nascimento
                nascionalidade
                cidade
                email
                telefone
                endereco
                documento
                afiliado
                sexo
                etnia
                tp sangue
                est civil
        """
        return Connection() \
            .connect() \
            .add_field('id') \
            .add_field('nome') \
            .add_table('cidade') \
            .add_where('nome', self.getNome()) \
            .set_limit(limit) \
            .exec_select() \
            .fetch()
