import jsonlines


def process_log(log_file, log_id):
    contador = 0
    request_details = []
    upstream_uri_details = []
    response_details = []
    authenticated_entity_details = []
    route_details = []
    service_details = []
    latencies_details = []
    client_ip_details = []
    started_at_details = []

    with jsonlines.open(log_file) as arquivo:
        for obj in arquivo:
            log_id += 1
            contador += 1

            # request
            request_method = obj['request']['method']
            request_uri = obj['request']['uri']
            request_url = obj['request']['url']
            request_size = obj['request']['size']
            request_querystring = obj['request']['querystring']
            request_querystring_str = ';'.join(str(e) for e in request_querystring)
            request_headers_accept = obj['request']['headers']['accept']
            request_headers_host = obj['request']['headers']['host']
            request_headers_useragent = obj['request']['headers']['user-agent']
            request_details.append((log_id, request_method, request_uri, request_url, request_size,
                                    request_querystring_str, request_headers_accept, request_headers_host,
                                    request_headers_useragent))

            # upstream_uri
            upstream_uri = obj['upstream_uri']
            upstream_uri_details.append((log_id, upstream_uri))

            # response
            response_status = obj['response']['status']
            response_size = obj['response']['size']
            response_headers_contentlength = obj['response']['headers']['Content-Length']
            response_headers_via = obj['response']['headers']['via']
            response_headers_connection = obj['response']['headers']['Connection']
            response_headers_accesscontrolallowcredentials = obj['response']['headers']['access-control-allow' \
                                                                                        '-credentials']
            response_headers_contenttype = obj['response']['headers']['Content-Type']
            response_headers_server = obj['response']['headers']['server']
            response_headers_accesscontrolalloworigin = obj['response']['headers']['access-control-allow-origin']
            response_details.append((log_id, response_status, response_size, response_headers_contentlength,
                                     response_headers_via, response_headers_connection,
                                     response_headers_accesscontrolallowcredentials, response_headers_contenttype,
                                     response_headers_server, response_headers_accesscontrolalloworigin))

            # authenticated_entity
            authenticated_entity_consumer_id_uuid = obj['authenticated_entity']['consumer_id']['uuid']
            authenticated_entity_details.append((log_id, authenticated_entity_consumer_id_uuid))

            # route
            route_created_at = obj['route']['created_at']
            route_hosts = obj['route']['hosts']
            route_id = obj['route']['id']
            route_methods = obj['route']['methods']
            route_methods_str = ';'.join(str(e) for e in route_methods)
            route_paths = obj['route']['paths']
            route_paths_str = ';'.join(str(e) for e in route_paths)
            route_preserve_host = obj['route']['preserve_host']
            route_protocols = obj['route']['protocols']
            route_protocols_str = ';'.join(str(e) for e in route_protocols)
            route_regex_priority = obj['route']['regex_priority']
            route_service_id = obj['route']['service']['id']
            route_strip_path = obj['route']['strip_path']
            route_updated_at = obj['route']['updated_at']
            route_details.append((log_id, route_created_at, route_hosts, route_id, route_methods_str, route_paths_str,
                                  route_preserve_host, route_protocols_str, route_regex_priority, route_service_id,
                                  route_strip_path, route_updated_at))

            # service
            service_connect_timeout = obj['service']['connect_timeout']
            service_created_at = obj['service']['created_at']
            service_host = obj['service']['host']
            service_id = obj['service']['id']
            service_name = obj['service']['name']
            service_path = obj['service']['path']
            service_port = obj['service']['port']
            service_protocol = obj['service']['protocol']
            service_read_timeout = obj['service']['read_timeout']
            service_retries = obj['service']['retries']
            service_updated_at = obj['service']['updated_at']
            service_write_timeout = obj['service']['write_timeout']
            service_details.append((log_id, service_connect_timeout, service_created_at, service_host, service_id,
                                    service_name, service_path, service_port, service_protocol, service_read_timeout,
                                    service_retries, service_updated_at, service_write_timeout))

            # latencies
            latencies_proxy = obj['latencies']['proxy']
            latencies_kong = obj['latencies']['kong']
            latencies_request = obj['latencies']['request']
            latencies_details.append((log_id, latencies_proxy, latencies_kong, latencies_request))

            # client_ip
            client_ip = obj['client_ip']
            client_ip_details.append((log_id, client_ip))

            # started_at
            started_at = obj['started_at']
            started_at_details.append((log_id, started_at))

        return [request_details, upstream_uri_details, response_details, authenticated_entity_details, route_details,
                service_details, latencies_details, client_ip_details, started_at_details]
