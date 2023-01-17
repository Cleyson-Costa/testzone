import pymysql.cursors


# noinspection PyBroadException
class Connection:

    def __init__(self):
        self.__con = None
        self.__ftc = None
        self.__qry = []
        self.__field = []
        self.__table = []
        self.__where = []
        self.__group = []
        self.__having = []
        self.__order = []
        self.__limit = 0
        self.__host = '127.0.0.1'
        self.__user = 'cleyson'
        self.__db = 'testzone'
        self.__pass = 'Cl@976213'
        self.__port = 3306

    def reset(self):
        self.__ftc = None
        self.__qry = []
        self.__field = []
        self.__table = []
        self.__where = []
        self.__group = []
        self.__having = []
        self.__order = []
        self.__limit = 0
        return self

    def set_host(self, host: str):
        self.__host = host
        return self

    def set_user(self, user: str):
        self.__user = user
        return self

    def set_db(self, database: str):
        self.__db = database
        return self

    def set_pass(self, password: str):
        self.__pass = password
        return self

    def set_port(self, port: str):
        self.__port = port
        return self

    def connect(self):
        self.__con = pymysql.connect(
            host=self.__host,
            user=self.__user,
            database=self.__db,
            password=self.__pass,
            port=self.__port,
            cursorclass=pymysql.cursors.DictCursor
        )
        return self

    def add_field(self, field_name: str):
        self.__field.append(field_name)
        return self

    def add_table(self, table_name: str):
        self.__table.append(table_name)
        return self

    def add_where(self, assertion: str, expected, operator='='):
        if expected != '' and type(expected) is str:
            self.__where.append(assertion + operator + f'\'{expected}\'')
        return self

    def add_where_one(self, assertion: str):
        self.__where.append(assertion)
        return self

    def add_having(self, condition: str):
        self.__having.append(condition)
        return self

    def add_order(self, condition: str):
        self.__order.append(condition)
        return self

    def set_limit(self, value: int):
        self.__limit = value
        return self

    def get_field(self):
        return ',\n'.join(self.__field)

    def get_table(self):
        return '\n'.join(self.__table)

    def get_where(self):
        return '\nand '.join(self.__where)

    def get_group(self):
        return ',\n '.join(self.__group)

    def get_having(self):
        return '\nand '.join(self.__having)

    def get_order(self):
        return ',\n '.join(self.__order)

    def get_limit(self):
        return self.__limit

    def set_qry(self, sql: str):
        self.__qry = sql

    def get_qry(self):
        return self.__qry

    def get_select(self):
        qry = 'select\n' + self.get_field()
        qry += '\nfrom\n' + self.get_table()
        qry += '\nwhere\n' + self.get_where() \
            if self.__where != [] else ''
        qry += '\ngroup by\n' + self.get_group() \
            if self.__group != [] else ''
        qry += '\nhaving\n' + self.get_having() \
            if self.__having != [] else ''
        qry += '\norder by\n' + self.get_order() \
            if self.__order != [] else ''
        qry += '\nlimit ' + str(self.get_limit()) \
            if self.__limit != 0 else ''
        return qry

    def __exec(self):
        self.__con.begin()
        cur = self.__con.cursor()
        try:
            cur.execute(self.__qry)
            self.__ftc = cur.fetchall()
        except:
            self.__con.rollback()
        finally:
            cur.close()
            self.__con.close()

    def exec_select(self):
        if self.__qry != '':
            self.__qry = self.get_select()
        self.__exec()
        return self

    def fetch(self):
        return self.__ftc
