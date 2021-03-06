# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class EfsLocation(pulumi.CustomResource):
    """
    Manages an AWS DataSync EFS Location.
    
    > **NOTE:** The EFS File System must have a mounted EFS Mount Target before creating this resource.
    """
    def __init__(__self__, __name__, __opts__=None, ec2_config=None, efs_file_system_arn=None, subdirectory=None, tags=None):
        """Create a EfsLocation resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not ec2_config:
            raise TypeError('Missing required property ec2_config')
        __props__['ec2_config'] = ec2_config

        if not efs_file_system_arn:
            raise TypeError('Missing required property efs_file_system_arn')
        __props__['efs_file_system_arn'] = efs_file_system_arn

        __props__['subdirectory'] = subdirectory

        __props__['tags'] = tags

        __props__['arn'] = None
        __props__['uri'] = None

        super(EfsLocation, __self__).__init__(
            'aws:datasync/efsLocation:EfsLocation',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

