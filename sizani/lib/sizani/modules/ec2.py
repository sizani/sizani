# # -*- coding: utf-8 -*-
import json
import re
import psutil
import paramiko
from collections import defaultdict
from sizani.lib.sizani.utils import logconf
from sizani.lib.sizani.utils.decor import Decor as ppprint
from tabulate import tabulate
import textwrap


class bcolors:
    HEADER = '\033[35m'
    NULLIFY = '\033[0m'
    RUNNING = '\033[32m'
    SHUTDOWN = '\033[31m'
    PENDING = '\033[33m'


class EC2:
    # Custom logger
    _log = logconf.SIZANILogger()

    def __init__(self, ec2resource, format, monitoring, ssh_session, key, ssh_username):
        """Default constructor"""
        try:
            self._log.traceEnter(self.__class__.__name__)
            self._ec2resource = ec2resource
            self._format = format
            self._monitoring = monitoring
            self._ssh_session = ssh_session
            self._key = key
            self._ssh_username = ssh_username
            self._monitor(ec2resource, format, monitoring, ssh_session, key, ssh_username)
        finally:
            self._log.traceExit(self.__class__.__name__)

    def __del__(self):
        """Default destructor"""
        try:
            self._log.traceEnter(self.__class__.__name__)
            pass
        finally:
            self._log.traceExit(self.__class__.__name__)

    def _monitor(self, ec2resource, format, monitoring, ssh_session, key, ssh_username):
        try:
            self._log.traceEnter(self.__class__.__name__)
            args = defaultdict()
            placement = defaultdict()
            productcodes = defaultdict()
            netinfo = defaultdict()
            sysmon = defaultdict()
            tabformat = []
            instances = self._ec2resource.instances.filter(Filters=[{
                'Name':
                'instance-state-name',
                'Values': [
                    'pending', 'running', 'shutting-down', 'stopped',
                    'stopping', 'terminated'
                ],
            }])
            for instance in instances:
                if instance.id:
                    try:
                        instance.ami_launch_index
                        ami_launch_index = instance.ami_launch_index
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.image_id
                        image_id = instance.image_id,
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.instance_type
                        instance_type = instance.instance_type
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.kernel_id
                        if(instance.kernel_id is None):
                            kernel_id = "not_applicable"
                        else:
                            kernel_id = instance.kernel_id
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.key_name
                        key_name = instance.key_name
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.launch_time
                        launch_time = instance.launch_time.strftime("%Y-%m-%d %H:%M:%S")
                    except NameError:
                        self._log.error('value not defined')
                    # try:
                    #     instance.monitoring
                    #     monitoring = instance.monitoring
                    # except NameError:
                    #     self._log.error('value not defined')
                    try:
                        instance.placement['AvailabilityZone']
                        availability_zone = instance.placement['AvailabilityZone']
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.placement['GroupName']
                        if(instance.placement['GroupName'] is None or instance.placement['GroupName'] == ''):
                            group_name = "not_applicable"
                        else:
                            group_name = instance.placement['GroupName']
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.placement['Tenancy']
                        tenancy = instance.placement['Tenancy']
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.platform
                        if(instance.platform is None):
                            platform = "*nix"
                        else:
                            platform = "windows"
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.private_dns_name
                        private_dns_name = instance.private_dns_name
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.private_ip_address
                        private_ip_address = instance.private_ip_address
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.public_dns_name
                        if(instance.public_dns_name is None or instance.public_dns_name == ""):
                            if(format == 'table'):
                                public_dns_name = bcolors.SHUTDOWN+'available_only_in_running_state'+bcolors.NULLIFY
                            else:
                                public_dns_name = 'available_only_in_running_state'
                        else:
                            public_dns_name = instance.public_dns_name
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.public_ip_address
                        if(instance.public_ip_address is None or instance.public_ip_address == ""):
                            if(format == 'table'):
                                public_ip_address = bcolors.SHUTDOWN+'available_only_in_running_state'+bcolors.NULLIFY
                            else:
                                public_ip_address = 'available_only_in_running_state'
                        else:
                            public_ip_address = instance.public_ip_address
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.ramdisk_id
                        if(instance.ramdisk_id is None or instance.ramdisk_id == ""):
                            ramdisk_id = "not_applicable"
                        else:
                            ramdisk_id = instance.ramdisk_id
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.state['Name']
                        instance_state = instance.state['Name']
                        if (instance_state == 'running'):
                            if(format == 'table'):
                                instance_state = bcolors.RUNNING+'RUNNING'+bcolors.NULLIFY
                            else:
                                instance_state = instance_state
                        elif(instance_state == 'stopped'):
                            if(format == 'table'):
                                instance_state = bcolors.SHUTDOWN+'SHUTDOWN'+bcolors.NULLIFY
                            else:
                                instance_state = instance_state
                        else:
                            instance_state = instance_state
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.state_transition_reason
                        state_transition_reason = instance.state_transition_reason
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.architecture
                        architecture = instance.architecture
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.block_device_mappings[0].get('DeviceName')
                        block_device_name = instance.block_device_mappings[0].get('DeviceName')
                    except (NameError, IndexError) as ni:
                        block_device_name = ""
                        self._log.error(block_device_name)
                    try:
                        instance.block_device_mappings[0]['Ebs'].get('AttachTime')
                        block_device_attachtime = instance.block_device_mappings[0].get(
                            'AttachTime')
                    except (NameError, IndexError) as ni:
                        block_device_attachtime = ""
                        self._log.error(block_device_attachtime)
                    try:
                        instance.block_device_mappings[0]['Ebs'].get('DeleteOnTermination')
                        block_device_delete_on_termination = instance.block_device_mappings[0]['Ebs'].get(
                            'DeleteOnTermination')
                    except (NameError, IndexError) as ni:
                        block_device_delete_on_termination = ""
                        self._log.error(block_device_delete_on_termination)
                    try:
                        instance.block_device_mappings[0]['Ebs'].get('Status')
                        block_device_status = instance.block_device_mappings[0]['Ebs'].get('Status')
                    except (NameError, IndexError) as ni:
                        block_device_status = ""
                        self._log.error(block_device_status)
                    try:
                        instance.block_device_mappings[0]['Ebs'].get('VolumeId')
                        block_device_volume_id = instance.block_device_mappings[0]['Ebs'].get(
                            'VolumeId')
                    except (NameError, IndexError) as ni:
                        block_device_volume_id = ""
                        self._log.error(block_device_volume_id)
                    try:
                        instance.client_token
                        if(instance.client_token is None or instance.client_token == ""):
                            client_token = "not_applicable"
                        else:
                            client_token = instance.client_token
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.ebs_optimized
                        ebs_optimized = instance.ebs_optimized
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.ena_support
                        ena_support = instance.ena_support
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.hypervisor
                        hypervisor = instance.hypervisor
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.root_device_name
                        root_device_name = instance.root_device_name
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.root_device_type
                        root_device_type = instance.root_device_type
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.security_groups[0]['GroupName']
                        security_group_name = instance.security_groups[0]['GroupName']
                    except (NameError, IndexError) as ni:
                        security_group_name = ""
                        self._log.error(security_group_name)
                    try:
                        instance.security_groups[0]['GroupId']
                        security_group_id = instance.security_groups[0]['GroupId']
                    except (NameError, IndexError) as ni:
                        security_group_id = ""
                        self._log.error(security_group_id)
                    try:
                        instance.state_reason
                        state_reason = instance.state_reason
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.tags
                        if(instance.tags is None):
                            tags = "tags_not_added_for_this_instance"
                        else:
                            tags = instance.tags
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.virtualization_type
                        virtualization_type = instance.virtualization_type
                    except NameError:
                        self._log.error('value not defined')
                    try:
                        instance.cpu_options
                        cpu_options = instance.cpu_options
                    except NameError:
                        self._log.error('value not defined')
                    block_device_mappings = {
                        'block_device_name': block_device_name,
                        'block_device_attachtime': block_device_attachtime,
                        'block_device_delete_on_termination': block_device_delete_on_termination,
                        'block_device_status': block_device_status,
                        'block_device_volume_id': block_device_volume_id,
                    }
                    for iface in instance.network_interfaces:
                        try:
                            iface.private_ip_addresses[0]
                            association = iface.private_ip_addresses[0]
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.attachment['AttachTime'].strftime("%Y-%m-%d %H:%M:%S")
                            attachment_time = iface.attachment['AttachTime'].strftime(
                                "%Y-%m-%d %H:%M:%S")
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.attachment['AttachmentId']
                            attachment_id = iface.attachment['AttachmentId']
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.attachment['DeleteOnTermination']
                            delete_on_termination = iface.attachment['DeleteOnTermination']
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.attachment['DeviceIndex']
                            device_index = iface.attachment['DeviceIndex']
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.attachment['Status']
                            status = iface.attachment['Status']
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.description
                            description = iface.description
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.groups[0]['GroupName']
                            group_name = iface.groups[0]['GroupName']
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.groups[0]['GroupId']
                            group_id = iface.groups[0]['GroupId']
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.mac_address
                            mac_address = iface.mac_address
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.network_interface_id
                            network_interface_id = iface.network_interface_id
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.owner_id
                            owner_id = iface.owner_id
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.source_dest_check
                            source_dest_check = iface.source_dest_check
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.subnet_id
                            subnet_id = iface.subnet_id
                        except NameError:
                            self._log.error('value not defined')
                        try:
                            iface.vpc_id
                            vpc_id = iface.vpc_id
                        except NameError:
                            self._log.error('value not defined')
                        attachment = {
                            'attachment_time': attachment_time,
                            'attachment_id': attachment_id,
                            'delete_on_termination': delete_on_termination,
                            'device_index': device_index,
                            'status': status,
                        }
                        groups = {
                            'group_name': group_name,
                            'group_id': group_id,
                        }
                        netinfo = {
                            'association': association,
                            'attachment': attachment,
                            'description': description,
                            'groups': groups,
                            'mac_address': mac_address,
                            'network_interface_id': network_interface_id,
                            'owner_id': owner_id,
                            'source_dest_check': source_dest_check,
                            'subnet_id': subnet_id,
                            'vpc_id': vpc_id,
                        }
                    security_groups = {
                        'group_name': security_group_name,
                        'group_id': security_group_id,
                    }
                    if(ssh_session == None):
                        pass
                    elif(key == None):
                        pass
                    elif(ssh_username == None):
                        pass
                    else:
                        ssh_session.connect(public_ip_address, port=22, username=ssh_username,
                                            password=None, pkey=key, key_filename=None,
                                            timeout=60, allow_agent=True, look_for_keys=True,
                                            compress=False, sock=None, gss_auth=False,
                                            gss_kex=False, gss_deleg_creds=True, gss_host=None,
                                            banner_timeout=None, auth_timeout=None, gss_trust_dns=True,
                                            passphrase=None)
                        sftp_session = ssh_session.open_sftp()
                        sftp_session.put('cmd/sys', '/tmp/sizanisys')
                        ssh_session.exec_command('chmod +x /tmp/sizanisys')
                        stdin, stdout, stderr = ssh_session.exec_command('/tmp/sizanisys')
                        sys_dict = stdout.readlines()[0]
                        sys_json = json.loads(sys_dict)
                        sysmon = {
                            'memory_usage_percent': sys_json['memory_usage_percent'],
                            'swap_usage_percent': sys_json['swap_usage_percent'],
                            'partition_usage_percent': sys_json['partition_usage_percent'],
                            'cpu_percent': sys_json['cpu_percent'],
                        }
                        ssh_session.close()
                    # try:
                    #     if(memory_usage_percent is None or memory_usage_percent == ''):
                    #         print(memory_usage_percent)
                    #         memory_usage_percent = 'only_available_if_monitoring_enabled'
                    #     else:
                    #         memory_usage_percent = memory_usage_percent
                    #         print(memory_usage_percent)
                    # except NameError:
                    #     self._log.error('value not defined')
                    args[instance.id] = {
                        'public_dns_name': public_dns_name,
                        'public_ip_address': public_ip_address,
                        'instance_state': instance_state,
                        'instance_type': instance_type,
                        'network_interfaces': netinfo["association"],
                        'platform': platform,
                        'memory_usage_percent': sysmon.get('memory_usage_percent'),
                        'swap_usage_percent': sysmon.get('swap_usage_percent'),
                        'partition_usage_percent': sysmon.get('partition_usage_percent'),
                        'cpu_percent': sysmon.get('cpu_percent'),
                        # 'ami_launch_index': ami_launch_index,
                        # 'image_id': image_id,
                        # 'kernel_id': kernel_id,
                        # 'key_name': key_name,
                        # 'launch_time': launch_time,
                        # 'monitoring': monitoring,
                        # 'availability_zone': availability_zone,
                        # 'group_name': group_name,
                        # 'tenancy': tenancy,
                        # 'platform': platform,
                        # 'ramdisk_id': ramdisk_id,
                        # 'state_transition_reason': state_transition_reason,
                        # 'architecture': architecture,
                        # 'block_device_mappings': block_device_mappings,
                        # 'client_token': client_token,
                        # 'ebs_optimized': ebs_optimized,
                        # 'ena_support': ena_support,
                        # 'hypervisor': hypervisor,
                        # 'root_device_name': root_device_name,
                        # 'root_device_type': root_device_type,
                        # 'security_groups': security_groups,
                        # 'state_reason': state_reason,
                        # 'tags': tags,
                        # 'virtualization_type': virtualization_type,
                        # 'cpu_options': cpu_options,
                    }

                    tabformat.append([instance.id,
                                      instance_state,
                                      instance_type,
                                      netinfo["association"]["PrivateIpAddress"],
                                      netinfo["association"]["PrivateDnsName"],
                                      public_ip_address,
                                      public_dns_name,
                                      platform,
                                      sysmon.get('memory_usage_percent'),
                                      sysmon.get('swap_usage_percent'),
                                      sysmon.get('partition_usage_percent'),
                                      sysmon.get('cpu_percent'),
                                      ])

            if (args == {}):
                args = {
                    'warning': 'No EC2 instance found in given region. Please try another region in murid yaml file or create a new EC2 instance.'
                }
                ppprint(json.dumps(args, sort_keys=True, indent=4))
            else:
                if(format == 'table'):
                    tabs = [bcolors.HEADER+"ID"+bcolors.NULLIFY,
                            bcolors.HEADER+"STATE"+bcolors.NULLIFY,
                            bcolors.HEADER+"TYPE"+bcolors.NULLIFY,
                            bcolors.HEADER+"PRIVATE_IP"+bcolors.NULLIFY,
                            bcolors.HEADER+"PRIVATE_DNS_NAME"+bcolors.NULLIFY,
                            bcolors.HEADER+"PUBLIC_IP"+bcolors.NULLIFY,
                            bcolors.HEADER+"PUBLIC_DNS_NAME"+bcolors.NULLIFY,
                            bcolors.HEADER+"PLATFORM"+bcolors.NULLIFY,
                            bcolors.HEADER+"MEM_USAGE (%)"+bcolors.NULLIFY,
                            bcolors.HEADER+"SWAP_USAGE (%)"+bcolors.NULLIFY,
                            bcolors.HEADER+"PARTITION_USAGE (%)"+bcolors.NULLIFY,
                            bcolors.HEADER+"CPU_USAGE (%)"+bcolors.NULLIFY]
                    print(tabulate(tabformat, tabs, "fancy_grid"))
                else:
                    ppprint(json.dumps(args, sort_keys=True, indent=4))
        finally:
            self._log.traceExit(self.__class__.__name__)
