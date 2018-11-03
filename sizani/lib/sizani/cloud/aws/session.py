# # -*- coding: utf-8 -*-
import botocore
import boto3
import json
import paramiko
import sys
from sizani.lib.sizani.core import exceptions
from sizani.lib.sizani.core import interfaces
from sizani.lib.sizani.utils import logconf
from sizani.lib.sizani.modules import ec2


class AWSSessionImpl(interfaces.SessionInterface):
    log = logconf.SIZANILogger()

    def __init__(self, YamlManager):
        try:
            self.log.traceEnter(self.__class__.__name__)
            self._yamlmgr = YamlManager
            self._defaultregions = [
                "us-east-1",
                "us-east-2",
                "us-west-1",
                "us-west-2",
                "ca-central-1",
                "eu-central-1",
                "eu-west-1",
                "eu-west-2",
                "eu-west-3",
                "ap-northeast-1",
                "ap-northeast-2",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-south-1",
                "sa-east-1"
            ]
        finally:
            self.log.traceExit(self.__class__.__name__)

    def __del__(self):
        try:
            self.log.traceEnter(self.__class__.__name__)
            # self.disconnect(1)
        finally:
            self.log.traceExit(self.__class__.__name__)

    def monitor(self):
        try:
            self.log.traceEnter(self.__class__.__name__)
            awscreds = self._yamlmgr.readYAML()
            try:
                session = boto3.session.Session(
                    aws_access_key_id=awscreds['aws_access_key_id'],
                    aws_secret_access_key=awscreds['aws_secret_access_key'],
                )
                if (awscreds['resources'] == 'ec2'):
                    ec2resource = session.resource(
                        awscreds['resources'], region_name=awscreds['region'])
                    format = awscreds['format']
                    monitoring = awscreds['monitoring']
                    # ssh_password = awscreds['password']
                    if(monitoring == 'sizani'):
                        ssh = awscreds['ssh']
                        if(ssh is None or ssh == 'disabled'):
                            self.log.error(
                                'ssh is required when monitoring is set to sizani in yaml file.')
                        else:
                            ssh_auth_type = awscreds['auth_type']
                            ssh_username = awscreds['username']
                            ssh_access_key = awscreds['access_key']
                            if (ssh_auth_type is None or ssh_auth_type == ''):
                                self.log.error(
                                    'ssh is defined but no auth_type is defined in yaml file.')
                            elif (ssh_username is None or ssh_username == ''):
                                self.log.error(
                                    'ssh is defined but no username is defined in yaml file.')
                            elif (ssh_access_key is None or ssh_access_key == ''):
                                self.log.error(
                                    'ssh is defined but no access_key is defined in yaml file.')
                            else:
                                ssh_session = paramiko.SSHClient()
                                ssh_session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                                key = paramiko.RSAKey.from_private_key_file(ssh_access_key)
                                ec2.EC2(ec2resource, format, monitoring,
                                        ssh_session, key, ssh_username)
                    elif(monitoring == 'cloudwatch'):
                        self.log.error('cloudwatch Method not implemented yet.')
                    elif(monitoring == 'disabled'):
                        ec2.EC2(ec2resource, format, monitoring,
                                ssh_session=None, key=None, ssh_username=None)
                    else:
                        ec2.EC2(ec2resource, format, monitoring,
                                ssh_session=None, key=None, ssh_username=None)
            except (KeyError, TypeError) as kt:
                pass
            except ValueError as ve:
                self.log.error("Invalid region name specified in murid yaml file. Region needs to be one for the following %s." % (
                    self._defaultregions))
            except botocore.exceptions.ClientError as bc:
                self.log.error("AWS was not able to validate the provided access credentials")
            except:
                type, value, tb = sys.exc_info()
                self.log.exception("", type, value, tb)
                raise
        finally:
            self.log.traceExit(self.__class__.__name__)
