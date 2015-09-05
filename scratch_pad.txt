docker run \
--rm \
--name docker_audit \
-ti \
-v /home/moore/Devel/docker_audit/locallogs:/var/log/mysql \
-p 5601:5601 \
-p 9999:9200 \
mysqlboy/docker_audit \
/bin/bash


curl -XGET 'localhost:9999/logstash-*/_count?pretty'

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9999, 'url_prefix': 'es', 'use_ssl': False},
])
es.count('logstash-*')
