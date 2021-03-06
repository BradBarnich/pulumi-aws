# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class LoadBalancer(pulumi.CustomResource):
    """
    Provides an Elastic Load Balancer resource, also known as a "Classic
    Load Balancer" after the release of
    [Application/Network Load Balancers](https://www.terraform.io/docs/providers/aws/r/lb.html).
    
    > **NOTE on ELB Instances and ELB Attachments:** Terraform currently
    provides both a standalone ELB Attachment resource
    (describing an instance attached to an ELB), and an ELB resource with
    `instances` defined in-line. At this time you cannot use an ELB with in-line
    instances in conjunction with a ELB Attachment resources. Doing so will cause a
    conflict and will overwrite attachments.
    """
    def __init__(__self__, __name__, __opts__=None, access_logs=None, availability_zones=None, connection_draining=None, connection_draining_timeout=None, cross_zone_load_balancing=None, health_check=None, idle_timeout=None, instances=None, internal=None, listeners=None, name=None, name_prefix=None, security_groups=None, source_security_group=None, subnets=None, tags=None):
        """Create a LoadBalancer resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['access_logs'] = access_logs

        __props__['availability_zones'] = availability_zones

        __props__['connection_draining'] = connection_draining

        __props__['connection_draining_timeout'] = connection_draining_timeout

        __props__['cross_zone_load_balancing'] = cross_zone_load_balancing

        __props__['health_check'] = health_check

        __props__['idle_timeout'] = idle_timeout

        __props__['instances'] = instances

        __props__['internal'] = internal

        if not listeners:
            raise TypeError('Missing required property listeners')
        __props__['listeners'] = listeners

        __props__['name'] = name

        __props__['name_prefix'] = name_prefix

        __props__['security_groups'] = security_groups

        __props__['source_security_group'] = source_security_group

        __props__['subnets'] = subnets

        __props__['tags'] = tags

        __props__['arn'] = None
        __props__['dns_name'] = None
        __props__['source_security_group_id'] = None
        __props__['zone_id'] = None

        super(LoadBalancer, __self__).__init__(
            'aws:elasticloadbalancing/loadBalancer:LoadBalancer',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

