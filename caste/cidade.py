from crud.connection import Connection


class Cidade:

    def __init__(self):
        self.__uf = ''

    def set_uf(self, uf: str):
        self.__uf = uf
        return self

    def get_uf(self):
        return self.__uf

    def get_cidades(self):
        limit = 10 if self.__uf == '' else 0
        return Connection() \
            .connect() \
            .add_field('uf') \
            .add_field('nome') \
            .add_field('ibge') \
            .add_table('cidade') \
            .add_where('uf', self.__uf) \
            .set_limit(limit) \
            .exec_select() \
            .fetch()
