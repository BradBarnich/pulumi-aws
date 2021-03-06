# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Role(pulumi.CustomResource):
    """
    Provides an IAM role.
    """
    def __init__(__self__, __name__, __opts__=None, assume_role_policy=None, description=None, force_detach_policies=None, max_session_duration=None, name=None, name_prefix=None, path=None, permissions_boundary=None, tags=None):
        """Create a Role resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not assume_role_policy:
            raise TypeError('Missing required property assume_role_policy')
        __props__['assume_role_policy'] = assume_role_policy

        __props__['description'] = description

        __props__['force_detach_policies'] = force_detach_policies

        __props__['max_session_duration'] = max_session_duration

        __props__['name'] = name

        __props__['name_prefix'] = name_prefix

        __props__['path'] = path

        __props__['permissions_boundary'] = permissions_boundary

        __props__['tags'] = tags

        __props__['arn'] = None
        __props__['create_date'] = None
        __props__['unique_id'] = None

        super(Role, __self__).__init__(
            'aws:iam/role:Role',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

