CREATE TABLE log_request (
  log_id NUMBER,
  request_method VARCHAR2(50),
  request_uri VARCHAR2(500),
  request_url VARCHAR2(500),
  request_size NUMBER,
  request_querystring VARCHAR2(50),
  request_headers_accept VARCHAR2(50),
  request_headers_host VARCHAR2(500),
  request_headers_useragent VARCHAR2(500),
  CONSTRAINT log_id_pk PRIMARY KEY (log_id)
);
CREATE TABLE log_upstream (
  upstream_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
  log_id NUMBER,
  upstream_uri VARCHAR2(500),
  CONSTRAINT fk_upstream_log_id
    FOREIGN KEY (log_id)
    REFERENCES log_request(log_id),
  PRIMARY KEY(upstream_id)
);
CREATE TABLE log_response (
  response_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
  log_id NUMBER,
  response_status NUMBER,
  response_size NUMBER,
  response_headers_contentlength NUMBER,
  response_headers_via VARCHAR2(500),
  response_headers_connection VARCHAR2(500),
  response_headers_accesscontrolallowcredentials VARCHAR2(50),
  response_headers_contenttype VARCHAR2(500),
  response_headers_server VARCHAR2(500),
  response_headers_accesscontrolalloworigin VARCHAR2(500),
  CONSTRAINT fk_response_log_id
    FOREIGN KEY (log_id)
    REFERENCES log_request(log_id),
  PRIMARY KEY(response_id)
);
CREATE TABLE log_authenticated (
  authenticated_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
  log_id NUMBER,
  authenticated_entity_consumer_id_uuid VARCHAR2(500),
  CONSTRAINT fk_authenticated_log_id
    FOREIGN KEY (log_id)
    REFERENCES log_request(log_id),
  PRIMARY KEY(authenticated_id)
);
CREATE TABLE log_route (
  route_table_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
  log_id NUMBER,
  route_created_at VARCHAR2(500),
  route_hosts VARCHAR2(500),
  route_id VARCHAR2(500),
  route_methods VARCHAR2(500),
  route_paths VARCHAR2(500),
  route_preserve_host VARCHAR2(500),
  route_protocols VARCHAR2(500),
  route_regex_priority NUMBER,
  route_service_id VARCHAR2(500),
  route_strip_path VARCHAR2(500),
  route_updated_at VARCHAR2(500),
  CONSTRAINT fk_route_log_id
    FOREIGN KEY (log_id)
    REFERENCES log_request(log_id),
  PRIMARY KEY(route_table_id)
);
CREATE TABLE log_service (
  service_table_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
  log_id NUMBER,
  service_connect_timeout NUMBER,
  service_created_at VARCHAR2(500),
  service_host VARCHAR2(500),
  service_id VARCHAR2(500),
  service_name VARCHAR2(500),
  service_path VARCHAR2(500),
  service_port NUMBER,
  service_protocol VARCHAR2(500),
  service_read_timeout NUMBER,
  service_retries NUMBER,
  service_updated_at VARCHAR2(500),
  service_write_timeout NUMBER,
  CONSTRAINT fk_service_log_id
    FOREIGN KEY (log_id)
    REFERENCES log_request(log_id),
  PRIMARY KEY(service_table_id)
);
CREATE TABLE log_latencies (
  latencies_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
  log_id NUMBER,
  latencies_proxy NUMBER,
  latencies_kong NUMBER,
  latencies_request NUMBER,
  CONSTRAINT fk_latencies_log_id
    FOREIGN KEY (log_id)
    REFERENCES log_request(log_id),
  PRIMARY KEY(latencies_id)
);
CREATE TABLE log_client (
  client_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
  log_id NUMBER,
  client_ip VARCHAR2(500),
  CONSTRAINT fk_client_log_id
    FOREIGN KEY (log_id)
    REFERENCES log_request(log_id),
  PRIMARY KEY(client_id)
);
CREATE TABLE log_started (
  started_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
  log_id NUMBER,
  started_at VARCHAR2(500),
  CONSTRAINT fk_started_log_id
    FOREIGN KEY (log_id)
    REFERENCES log_request(log_id),
  PRIMARY KEY(started_id)
);
