# sizani
A cloud status and reporting framework. You can avoid writing scripts and using generic command line tool to check stats or monitor your cloud resource instead use YAML to get a complete information about your infrastructure running on Cloud in a json format or beautify tabular format.
I have tested the framework on Mac, Ubuntu and Windows 10.

## Getting Started
These instructions will get you a copy of the project up and running on your machine for development, testing and production purposes. See deployment notes on how to deploy the project on a live system.

### Services Supported
1. EC2

I will add a lot more to this project. Many more AWS services, cloud monitoring tracking, selective information, alerting ..etc.

### Installation
The project is not yet on pypi. I will upload it to pypi soon.

1. Currently, download the [gitrepo](https://github.com/sizani/sizani/archive/master.zip) and extract it to your any system running Ubuntu, MacOS, Windows 10 or *nix OS.
```
wget https://github.com/sizani/sizani/archive/master.zip
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
5. Next, let`s pass the yaml file to sizani to connect to AWS and capture common stats information in the default beautify tabular format about your AWS resource.
```
sizani -f myec2.yaml
```
![table_format](https://github.com/sizani/sizani/blob/master/docs/img/table_output.png?raw=true)

6. Next, let`s pass the yaml file to sizani to connect to AWS and capture common stats information in JSON format about your AWS resource.
```
sizani -f myec2.yaml
{
    "i-035c7ae5efa22c67d": {
        "instance_state": "running",
        "instance_type": "t2.micro",
        "network_interfaces": {
            "Association": {
                "IpOwnerId": "amazon",
                "PublicDnsName": "ec2-54-186-68-70.us-west-2.compute.amazonaws.com",
                "PublicIp": "54.186.68.70"
            },
            "Primary": true,
            "PrivateDnsName": "ip-172-31-16-120.us-west-2.compute.internal",
            "PrivateIpAddress": "172.31.16.120"
        },
        "public_dns_name": "ec2-54-186-68-70.us-west-2.compute.amazonaws.com",
        "public_ip_address": "54.186.68.70"
    },
    "i-0af2ffa689e3a42bf": {
        "instance_state": "running",
        "instance_type": "t2.micro",
        "network_interfaces": {
            "Association": {
                "IpOwnerId": "amazon",
                "PublicDnsName": "ec2-54-191-175-224.us-west-2.compute.amazonaws.com",
                "PublicIp": "54.191.175.224"
            },
            "Primary": true,
            "PrivateDnsName": "ip-172-31-20-143.us-west-2.compute.internal",
            "PrivateIpAddress": "172.31.20.143"
        },
        "public_dns_name": "ec2-54-191-175-224.us-west-2.compute.amazonaws.com",
        "public_ip_address": "54.191.175.224"
    }
}
```
7. Now, let`s shutdown the one of the two servers and re-run the scripts to check the output. Let`s try with the default beautify tabular format. Here you can see a couple custom messages while the server is in shutdown state.
![table_format](https://github.com/sizani/sizani/blob/master/docs/img/table_output_with_shutdown.png?raw=true)

8. Let`s try steps 7 with json format.
```
sizani -f myec2.yaml
{
    "i-035c7ae5efa22c67d": {
        "instance_state": "running",
        "instance_type": "t2.micro",
        "network_interfaces": {
            "Association": {
                "IpOwnerId": "amazon",
                "PublicDnsName": "ec2-54-186-68-70.us-west-2.compute.amazonaws.com",
                "PublicIp": "54.186.68.70"
            },
            "Primary": true,
            "PrivateDnsName": "ip-172-31-16-120.us-west-2.compute.internal",
            "PrivateIpAddress": "172.31.16.120"
        },
        "public_dns_name": "ec2-54-186-68-70.us-west-2.compute.amazonaws.com",
        "public_ip_address": "54.186.68.70"
    },
    "i-0af2ffa689e3a42bf": {
        "instance_state": "stopped",
        "instance_type": "t2.micro",
        "network_interfaces": {
            "Primary": true,
            "PrivateDnsName": "ip-172-31-20-143.us-west-2.compute.internal",
            "PrivateIpAddress": "172.31.20.143"
        },
        "public_dns_name": "available_only_in_running_state",
        "public_ip_address": "available_only_in_running_state"
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
  # Currently prints a few attributes even with all as attributes value.
  attributes: common
  # output_format [table|Json] - Default: table (lower_case) | This option is not required.
  format: json
```
