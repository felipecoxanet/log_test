# Instruções

1 - Ter instalado um banco de dados Oracle e ajustar as credenciais de usuario, senha e tns em `arquivos/config_file.py`, variavel `DB dados`

2 - Criar as tabelas no banco de dados, script disponivel em `arquivos/create_tables.sql`

3 - Ter um client Oracle instalado na maquina onde o teste será executado e ajustar o caminho da instalacao do Cliente em `arquivos/config_file.py`, variavel `lib_dir`

Caso necessario, ajustar o arquivo do Client Oracle `sqlnet.ora`:
````
SQLNET.ALLOWED_LOGON_VERSION_CLIENT = 8
SQLNET.ALLOWED_LOGON_VERSION_SERVER = 8
SQLNET.AUTHENTICATION_SERVICES= (NONE)
````

4 - Instalar o modulo cx_Oracle:

https://www.foxinfotech.in/2018/09/how-to-import-cx_oracle-in-pycharm.html

https://www.foxinfotech.in/2018/09/how-to-install-cx_oracle-for-python-on-windows.html

https://www.oracletutorial.com/python-oracle

OBS: instalar o cx_Oracle pelo terminal do IDE

5 - Ajustar o caminho do arquivo de logs em `arquivos/config_file.py`, variavel `log_file`. Esse arquivo é o que será processado pelo programa. 
O `arquivos/logs_sample.txt` que pode ser usado como teste.

6 - Os arquivos de Reports (CSV) serao gerados no diretorio `arquivos` do projeto.
