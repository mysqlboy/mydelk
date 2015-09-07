#!/usr/bin/python

from elasticsearch import Elasticsearch
import sys

import mydocker

# start the container
# provide output for
#   - documents imported
#   - kibana connection

# name,image,docker_host
def main():
    container_name = 'mydelk'
    docker_image = 'mysqlboy/docker_audit'
    docker_host = 'tcp://127.0.0.1:2375'
    cnt = mydocker.Container(container_name,docker_image,docker_host)
    cexists = cnt.findContainer()
    if cexists:
        # if yes get stats
        try:
            cnt.destroyContainer()
            container = cnt.createContainer()
            info = cnt.statContainer()
            cnt.startContainer(container)
        except ValueError, e:
            print "oops, we fucked up %s" % e
    else:
        container = cnt.createContainer()
        info = cnt.statContainer()
        cnt.startContainer(container)

    print info

if __name__ == "__main__":
    main()
