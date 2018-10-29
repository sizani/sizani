# # -*- coding: utf-8 -*-
import botocore
import boto3
import json
import sys
from sizani.lib.sizani.core import exceptions
from sizani.lib.sizani.core import interfaces
from sizani.lib.sizani.utils import logconf
from sizani.lib.sizani.modules import ec2


class AWSSessionImpl(interfaces.SessionInterface):
    log = logconf.SIZANILogger()
    # ppprint = p.Decor.prompt_print_success()

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
                session = boto3.Session(
                    aws_access_key_id=awscreds['aws_access_key_id'],
                    aws_secret_access_key=awscreds['aws_secret_access_key'],
                )
                if (awscreds['resources'] == 'ec2'):
                    ec2resource = session.resource(
                        awscreds['resources'], region_name=awscreds['region'])
                    ec2.EC2(ec2resource)
                    # import datetime
                    # endTime = datetime.datetime.utcnow()
                    # startTime = endTime - datetime.timedelta(minutes=10)
                    # ec2resourc = session.client('cloudwatch', region_name=awscreds['region'])
                    # stats = ec2resourc.get_metric_statistics(
                    #     Period=300,
                    #     StartTime=datetime.datetime.utcnow() - datetime.timedelta(seconds=600),
                    #     EndTime=datetime.datetime.utcnow(),
                    #     MetricName='CPUUtilization',
                    #     Namespace='AWS/EC2',
                    #     Statistics=['Average'],
                    #     Dimensions=[{'Name': 'InstanceId', 'Value': 'i-0113d9d2484a01e8e'}]
                    # )
                    # print(stats)
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
