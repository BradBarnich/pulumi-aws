# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Directory(pulumi.CustomResource):
    """
    Provides a Simple or Managed Microsoft directory in AWS Directory Service.
    
    > **Note:** All arguments including the password and customer username will be stored in the raw state as plain-text.
    [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
    """
    def __init__(__self__, __name__, __opts__=None, alias=None, connect_settings=None, description=None, edition=None, enable_sso=None, name=None, password=None, short_name=None, size=None, tags=None, type=None, vpc_settings=None):
        """Create a Directory resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['alias'] = alias

        __props__['connect_settings'] = connect_settings

        __props__['description'] = description

        __props__['edition'] = edition

        __props__['enable_sso'] = enable_sso

        __props__['name'] = name

        if not password:
            raise TypeError('Missing required property password')
        __props__['password'] = password

        __props__['short_name'] = short_name

        __props__['size'] = size

        __props__['tags'] = tags

        __props__['type'] = type

        __props__['vpc_settings'] = vpc_settings

        __props__['access_url'] = None
        __props__['dns_ip_addresses'] = None
        __props__['security_group_id'] = None

        super(Directory, __self__).__init__(
            'aws:directoryservice/directory:Directory',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

