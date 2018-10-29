# sizani-aws
An AWS cloud information and reporting framework. You can avoid writing scripts and use YAML to get a complete information about your infrastructure running on AWS.
I have tested the framework on Mac, Ubuntu and Windows 10.

## Getting Started
These instructions will get you a copy of the project up and running on your machine for development, testing and production purposes. See deployment notes on how to deploy the project on a live system.

### Services Supported
1. EC2

I will add a lot more to this project. Many more AWS services, cloud monitoring tracking, selective information, alerting ..etc.

### Installation
The project is not yet on pypi. I will upload it to pypi soon. 

1. Currently, download the [gitrepo](https://github.com/sizani/sizani-aws/archive/master.zip) and extract it to your any system running Ubuntu, MacOS, Windows 10 or *nix OS.
```
wget https://github.com/sizani/sizani-aws/archive/master.zip
```
2. Extract/Unzip the master.zip
```
unzip master.zip
```
3. Next change directory and enter sizani-aws-master & execute pip command to install all dependencies
```
cd sizani-aws-master
pip install .
```
4. Next, execute sizani from command prompt to look for help instructions
```
sizani

usage: sizani [-h] [-V] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -f FILE, --file FILE  specify a murid file to run
 ```
5. Next, let`s pass the yaml file to sizani to connect to AWS and capture all kind of information in JSON format about your AWS resource.
```
sizani -f myec2.yaml
{
    "i-xxxxxxxxx": {
        "ami_launch_index": 0,
        "architecture": "x86_64",
        "availability_zone": "us-west-2b",
        "block_device_mappings": {
            "block_device_attachtime": null,
            "block_device_delete_on_termination": true,
            "block_device_name": "/dev/xvda",
            "block_device_status": "attached",
            "block_device_volume_id": "vol-0xxxxxxxxx"
        },
        "client_token": "not_applicable",
        "cpu_options": {
            "CoreCount": 1,
            "ThreadsPerCore": 1
        },
        "ebs_optimized": false,
        "ena_support": true,
        "group_name": "launch-wizard-1",
        "hypervisor": "xen",
        "image_id": [
            "ami-axxxxxxx"
        ],
        "instance_state": "running",
        "instance_type": "t2.micro",
        "kernel_id": "not_applicable",
        "key_name": "alxxxxx",
        "launch_time": "2018-10-28 18:25:21",
        "monitoring": {
            "State": "disabled"
        },
        "network_interfaces": {
            "association": {
                "Association": {
                    "IpOwnerId": "amazon",
                    "PublicDnsName": "ec2-xx-xxx-xxx-xxx.us-west-2.compute.amazonaws.com",
                    "PublicIp": "xx.xxx.xxx.xxx"
                },
                "Primary": true,
                "PrivateDnsName": "ip-1xx-xx-xx-xx.us-west-2.compute.internal",
                "PrivateIpAddress": "xxx.xx.xx.xx"
            },
            "attachment": {
                "attachment_id": "eni-attach-09xxxxxxxxx",
                "attachment_time": "2018-10-28 18:25:21",
                "delete_on_termination": true,
                "device_index": 0,
                "status": "attached"
            },
            "description": "",
            "groups": {
                "group_id": "sg-0xxxxxxxxx",
                "group_name": "launch-wizard-1"
            },
            "mac_address": "02:xx:xx:xx:xx:xx",
            "network_interface_id": "eni-04xxxxxxxxxx",
            "owner_id": "7xxxxxxxxxxxxx",
            "source_dest_check": true,
            "subnet_id": "subnet-axxxxxxx",
            "vpc_id": "vpc-f4xxxxxxxxx"
        },
        "platform": "not_applicable",
        "PublicDnsName": "ec2-xx-xxx-xxx-xxx.us-west-2.compute.amazonaws.com",
        "PublicIp": "xx.xxx.xxx.xxx",
        "ramdisk_id": "not_applicable",
        "root_device_name": "/dev/xvda",
        "root_device_type": "ebs",
        "security_groups": {
            "group_id": "sg-xxxxxxxxxxxx",
            "group_name": "launch-wizard-1"
        },
        "state_reason": null,
        "state_transition_reason": "",
        "tags": [
            {
                "Key": "name",
                "Value": "test"
            }
        ],
        "tenancy": "default",
        "virtualization_type": "hvm"
    }
}

```
#### YAML Coding guidelines:
YAML is a very simple human-readable data serialization language. Please make sure to pass yaml in following format for sizani to work.
```
---
# Mandatory provider name: aws [Enterprise version will support all cloud providers and many more functionalities]
aws:
  # Mandatory access key to connect to AWS cloud provider
  aws_access_key_id: MYACCESSKEYID
  # Mandatory secret access key to connect to AWS cloud provider
  aws_secret_access_key: MYSECRETACCESSKRY
  region: us-west-2
  # Resource is what you want the information about, Currently supports single resource will add support
  # for multiple values soon
  resources: ec2
  # Currently prints very detailed information via all attributes .
  attributes: all
```
