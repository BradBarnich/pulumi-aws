# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class ConnectionAssociation(pulumi.CustomResource):
    """
    Associates a Direct Connect Connection with a LAG.
    """
    def __init__(__self__, __name__, __opts__=None, connection_id=None, lag_id=None):
        """Create a ConnectionAssociation resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not connection_id:
            raise TypeError('Missing required property connection_id')
        __props__['connection_id'] = connection_id

        if not lag_id:
            raise TypeError('Missing required property lag_id')
        __props__['lag_id'] = lag_id

        super(ConnectionAssociation, __self__).__init__(
            'aws:directconnect/connectionAssociation:ConnectionAssociation',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

