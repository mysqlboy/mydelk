#!/bin/bash

## setup.sh
## Shell script to initiate the various components of the stack.

service elasticsearch start
sleep 3
/opt/kibana/bin/kibana &
/opt/logstash/bin/logstash -f /etc/logstash/conf.d/logstash.conf $LSDEBUG
