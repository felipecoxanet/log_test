import cx_Oracle
from config_file import lib_dir
from config_file import user_db
from config_file import password_db
from config_file import dsn_db
from config_file import encoding


def connect_to_db():
    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    connection_db = cx_Oracle.connect(user=user_db, password=password_db,
                                      dsn=dsn_db,
                                      encoding=encoding)
    return connection_db


def return_log_id(connection_db, sql):
    try:
        with connection_db.cursor() as cursor:
            cursor.execute(sql)
            row = cursor.fetchone()
            row = row[0]
            if row is None:
                max_id = 0
            else:
                max_id = row
            connection_db.commit()
    except cx_Oracle.Error as error:
        print('Ocorreu um erro no return_log_id: {}'.format(error))
    return max_id


def grava_log(log_data, connection_db, sql):
    try:
        with connection_db.cursor() as cursor:
            # executa o insert de multiplas linhas
            cursor.executemany(sql, log_data)
            connection_db.commit()

    except cx_Oracle.Error as error:
        print(sql)
        print('Ocorreu um erro no grava_log: {}'.format(error))


def db_cursor(sql, connection_db):
    try:
        with connection_db.cursor() as cursor:
            cursor.execute(sql)
            while True:
                dados = cursor.fetchmany()
                connection_db.commit()
                if dados is None:
                    break
                return dados
    except cx_Oracle.Error as error:
        print(sql)
        print('Ocorreu um erro ao executar db_cursor: {}'.format(error))


def db_cursor_delete(sql, connection_db):
    try:
        with connection_db.cursor() as cursor:
            cursor.execute(sql)
            connection_db.commit()
    except cx_Oracle.Error as error:
        print(sql)
        print('Ocorreu um erro ao executar db_cursor_delete: {}'.format(error))
