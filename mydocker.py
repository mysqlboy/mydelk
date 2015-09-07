#!/usr/bin/python

#   Library to start docker container
#
#
#
import sys
from docker.errors import APIError
import docker
from io import BytesIO

class Container:

    def __init__(self,name,image,docker_host):
        self.cli = docker.Client(base_url=docker_host,version='auto')
        self.containerName = name
        self.containerImage = image

    def writeDockerfile(self,dockerfile, path):
        p = open(path, 'w')
        p.write(docker)
        p.close()

        return True

    def buildContainer(self):
        pass

    def createContainer(self):
        try:
            self.created_cnt = self.cli.create_container(image=self.containerImage,
                                                    host_config=docker.utils.create_host_config(binds=['/home/moore/Devel/docker_audit/locallogs:/var/log/mysql']),
                                                    name=self.containerName,
                                                    detach=True,

                                                    )
            return (self.created_cnt['Id'])
        except ValueError,e:
            print e

    def destroyContainer(self):
        self.cli.remove_container(container=self.containerName, v=True, force=True)

    def startContainer(self,id):
        try:
            self.cli.start(container=self.created_cnt['Id'])
        except ValueError,e:
            print e

    def stopContainer(self):
        self.cli.stop(self.containerName)

    def findContainer(self):
        #print "your container is caller %s" % (self.containerName)
        for i in self.cli.containers(all=True):
            if str(i['Names'][0]) == '/%s' % self.containerName:
                return True

    def statContainer(self):

        try:
            container_info = {}
            self.container_meta = self.cli.inspect_container(self.containerName)
            self.containerId = self.container_meta['Id']

            #print self.containerId
            return self.container_meta['NetworkSettings']['IPAddress']

        except ValueError, e:
            print e
