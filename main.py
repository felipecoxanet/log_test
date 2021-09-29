import db
import logs
from csv_process import gera_csv
from config_file import log_file
from config_file import sql_get_id
from config_file import sql_completo
from config_file import sql_select_completo
from config_file import service_header_completo
from config_file import service_file_name_completo
from config_file import sql_delete


def grava_log():
    connection = db.connect_to_db()
    log_id = db.return_log_id(connection, sql_get_id)
    log_data = logs.process_log(log_file, log_id)

    if len(sql_completo) != len(log_data):
        print('O numero de logs obtidos, {}, nao confere com o numero de inserts {}'.format(len(sql_completo),
                                                                                            len(log_data)))
        exit(1)

    indice = 0
    for x in log_data:
        db.grava_log(log_data[indice], connection, sql_completo[indice])
        indice += 1


def cria_csv():
    connection = db.connect_to_db()
    indice = 0
    for x in sql_select_completo:
        row = db.db_cursor(sql_select_completo[indice], connection)
        gera_csv(row, service_header_completo[indice], service_file_name_completo[indice])
        indice += 1


def limpa_tabelas():
    connection = db.connect_to_db()
    indice = 0
    for x in sql_delete:
        db.db_cursor_delete(sql_delete[indice], connection)
        indice += 1


def final_Call():
    if __name__ == '__main__':
        opcao_desejada = input('Selecione a opcao desejada: \n'
                               '1 - Somente inserir os dados de log no banco de dados.\n'
                               '2 - Somente gerar os relatorios (CSV).\n'
                               '3 - Inserir os dados no banco e gerar os relatorios (CSV).\n'
                               '4 - Apagar todos os dados de todas as tabela..\n'
                               '5 - Sair\n'
                               'Digite: ')
        opcao_desejada = int(opcao_desejada)

        if opcao_desejada == 1:
            grava_log()
        elif opcao_desejada == 2:
            cria_csv()
        elif opcao_desejada == 3:
            grava_log()
            cria_csv()
        elif opcao_desejada == 4:
            opcao_deletar = input('Tem certeza que deseja deletar o conteudo de todas as tabelas????\n'
                                  'Essa acao é irreversivel!!\n'
                                  '1 - DELETAR TUDO!\n'
                                  '2 - CANCELAR\n')
            opcao_deletar = int(opcao_deletar)
            print(opcao_deletar)
            if opcao_deletar == 1:
                limpa_tabelas()
            elif opcao_deletar == 2:
                print('Processo cancelado.')
                exit(1)
            else:
                print('Tente novamente e digite uma opcao valida. Opcao {} invalida'.format(opcao_deletar))
        elif opcao_desejada == 5:
            exit(1)
        else:
            print('Tente novamente e digite uma opcao valida. Opcao {} invalida'.format(opcao_desejada))


if __name__ == '__main__':
    final_Call()
