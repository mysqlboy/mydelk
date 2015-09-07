FROM elasticsearch
MAINTAINER eroomydna@gmail.com

WORKDIR ~
ADD logstash.list /etc/apt/sources.list.d/logstash.list
RUN apt-get -qq update
RUN apt-get -y -qq install wget tar gzip logstash

# Installing Kibana
RUN mkdir /usr/kibana
RUN wget -q https://download.elastic.co/kibana/kibana/kibana-4.1.1-linux-x64.tar.gz
RUN tar -xzf kibana-4.1.1-linux-x64.tar.gz -C /opt
RUN ln -s /opt/kibana-4.1.1-linux-x64 /opt/kibana

# Logstash config
ADD config/logstash.conf /etc/logstash/conf.d/logstash.conf
# Add patterns
RUN mkdir -p /etc/logstash/patterns
ADD config/mysql.pattern /etc/logstash/patterns/mysql
ADD setup.sh /tmp/setup.sh
RUN chmod +x /tmp/setup.sh

CMD '/tmp/setup.sh'
