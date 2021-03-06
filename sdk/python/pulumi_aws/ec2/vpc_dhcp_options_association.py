# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class VpcDhcpOptionsAssociation(pulumi.CustomResource):
    """
    Provides a VPC DHCP Options Association resource.
    * Removing the DHCP Options Association automatically sets AWS's `default` DHCP Options Set to the VPC.
    """
    def __init__(__self__, __name__, __opts__=None, dhcp_options_id=None, vpc_id=None):
        """Create a VpcDhcpOptionsAssociation resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not dhcp_options_id:
            raise TypeError('Missing required property dhcp_options_id')
        __props__['dhcp_options_id'] = dhcp_options_id

        if not vpc_id:
            raise TypeError('Missing required property vpc_id')
        __props__['vpc_id'] = vpc_id

        super(VpcDhcpOptionsAssociation, __self__).__init__(
            'aws:ec2/vpcDhcpOptionsAssociation:VpcDhcpOptionsAssociation',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

