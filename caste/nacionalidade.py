from crud.connection import Connection


class Nacionalidade:

    def get_nacionalidades(self):
        return Connection() \
            .connect() \
            .add_field('id') \
            .add_field('nome') \
            .add_table('nacionalidade') \
            .exec_select() \
            .fetch()
