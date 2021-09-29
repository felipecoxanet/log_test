# log file
log_file = 'arquivos/logs.txt'

# DB dados
lib_dir = r"D:\app\felip\product\11.2.0\client_1\BIN"
user_db = "teste"
password_db = 'teste123'
dsn_db = "192.168.0.102:1521/xe"
encoding = "UTF-8"

# delete table data
sql_delete = ['DELETE  log_started', 'DELETE log_client', 'DELETE log_latencies', 'DELETE log_service',
              'DELETE log_route', 'DELETE log_authenticated', 'DELETE log_response', 'DELETE log_upstream',
              'DELETE log_request']

# CSV file names
service_file_name = 'arquivos/service_csv_file.csv'
service_avg__file_name = 'arquivos/service_avg__csv_file.csv'
service_file_name_completo = []
service_file_name_completo.append(service_file_name)
service_file_name_completo.append(service_avg__file_name)

# CSV Header
service_header = ['service_name', 'count']
service_avg_header = ['service_name', 'avg_latencies_request', 'latencies_kong', 'latencies_request']
service_header_completo = []
service_header_completo.append(service_header)
service_header_completo.append(service_avg_header)

# SQLs Select Reports
sql_service = ('SELECT service_name, count(*) '
               'FROM log_service ' 
               'GROUP BY service_name')
sql_avg_service = ('SELECT log_service.service_name, '
                   'Avg(latencies_request), '
                   'Avg(latencies_kong), '
                   'Avg(latencies_request) '
                   'FROM log_latencies '
                   'LEFT JOIN log_service ON log_service.log_id = log_latencies.log_id '
                   'GROUP BY log_service.service_name')
sql_select_completo = []
sql_select_completo.append(sql_service)
sql_select_completo.append(sql_avg_service)

# SQLs insert Logs
sql_get_id = 'select max(log_id) ' \
             'from log_request'
sql_insert_request = ('insert into log_request(log_id, '
                                              'request_method, '
                                              'request_uri, '
                                              'request_url, '
                                              'request_size, '
                                              'request_querystring, '
                                              'request_headers_accept, '
                                              'request_headers_host, '
                                              'request_headers_useragent) '
                      'values(:log_id, '
                              ':request_method, '
                              ':request_uri, '
                              ':request_url, '
                              ':request_size, '
                              ':request_querystring, '
                              ':request_headers_accept, '
                              ':request_headers_host, '
                              ':request_headers_useragent)')
sql_insert_upstream = ('insert into log_upstream(log_id, '
                                                 'upstream_uri) '
                       'values(:log_id, '
                               ':upstream_uri)')
sql_insert_response = ('insert into log_response(log_id, '
                                                 'response_status, '
                                                 'response_size, '
                                                 'response_headers_contentlength, '
                                                 'response_headers_via, '
                                                 'response_headers_connection, '
                                                 'response_headers_accesscontrolallowcredentials, '
                                                 'response_headers_contenttype, '
                                                 'response_headers_server, '
                                                 'response_headers_accesscontrolalloworigin) '
                       'values(:log_id, '
                               ':response_status, '
                               ':response_size, '
                               ':response_headers_contentlength, '
                               ':response_headers_via, '
                               ':response_headers_connection, '
                               ':response_headers_accesscontrolallowcredentials, '
                               ':response_headers_contenttype, '
                               ':response_headers_server, '
                               ':response_headers_accesscontrolalloworigin)')
sql_insert_authenticated = ('insert into log_authenticated(log_id, '
                                                           'authenticated_entity_consumer_id_uuid) '
                            'values(:log_id, '
                                    ':authenticated_entity_consumer_id_uuid)')
sql_insert_route = ('insert into log_route(log_id, '
                                           'route_created_at, '
                                           'route_hosts, '
                                           'route_id, '
                                           'route_methods, '
                                           'route_paths, '
                                           'route_preserve_host, '
                                           'route_protocols, '
                                           'route_regex_priority, '
                                           'route_service_id, '
                                           'route_strip_path, '
                                           'route_updated_at) '
                    'values(:log_id, '
                            ':route_created_at, '
                            ':route_hosts, '
                            ':route_id, '
                            ':route_methods, '
                            ':route_paths, '
                            ':route_preserve_host, '
                            ':route_protocols, '
                            ':route_regex_priority, '
                            ':route_service_id, '
                            ':route_strip_path, '
                            ':route_updated_at)')
sql_insert_service = ('insert into log_service(log_id, '
                                               'service_connect_timeout, '
                                               'service_created_at, '
                                               'service_host, '
                                               'service_id, '
                                               'service_name, '
                                               'service_path, '
                                               'service_port, '
                                               'service_protocol, '
                                               'service_read_timeout, '
                                               'service_retries, '
                                               'service_updated_at, '
                                               'service_write_timeout) '
                      'values(:log_id, '
                              ':service_connect_timeout, '
                              ':service_created_at, '
                              ':service_host, '
                              ':service_id, '
                              ':service_name, '
                              ':service_path, '
                              ':service_port, '
                              ':service_protocol, '
                              ':service_read_timeout, '
                              ':service_retries, '
                              ':service_updated_at, '
                              ':service_write_timeout)')
sql_insert_latencies = ('insert into log_latencies(log_id, '
                                                   'latencies_proxy, '
                                                   'latencies_kong, '
                                                   'latencies_request) '
                        'values(:log_id, '
                                ':latencies_proxy, '
                                ':latencies_kong, '
                                ':latencies_request)')
sql_insert_client = ('insert into log_client(log_id, '
                                             'client_ip) '
                     'values(:log_id, '
                             ':client_ip)')
sql_insert_started = ('insert into log_started(log_id, '
                                               'started_at) '
                      'values(:log_id, '
                              ':started_at)')

sql_completo = []
sql_completo.append(sql_insert_request)
sql_completo.append(sql_insert_upstream)
sql_completo.append(sql_insert_response)
sql_completo.append(sql_insert_authenticated)
sql_completo.append(sql_insert_route)
sql_completo.append(sql_insert_service)
sql_completo.append(sql_insert_latencies)
sql_completo.append(sql_insert_client)
sql_completo.append(sql_insert_started)
