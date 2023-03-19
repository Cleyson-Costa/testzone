class Pessoas:

    def __init__(self):
        self.__nome = ''
        self.__fantasia = ''
        self.__tipo = 0
        self.__id_nacionalidade = 0
        self.__nascimento = ''

    def getNome(self):
        return self.__nome

    def setNome(self, value: str):
        self.__nome = value
        return self

    def getFantasia(self):
        return self.__fantasia

    def setFantasia(self, value: str):
        self.__fantasia = value
        return self

    def getTipo(self):
        return self.__tipo

    def setTipo(self, value: int):
        self.__tipo = value
        return self

    def getIdNacionalidade(self):
        return self.__id_nacionalidade

    def setIdNascionalidade(self, value: int):
        self.__id_nacionalidade = value
        return self

    def getNascimento(self):
        return self.__nascimento

    def setNascimento(self, value: str):
        self.__nascimento = value
        return self
