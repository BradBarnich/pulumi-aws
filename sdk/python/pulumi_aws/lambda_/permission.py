# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Permission(pulumi.CustomResource):
    """
    Creates a Lambda permission to allow external sources invoking the Lambda function
    (e.g. CloudWatch Event Rule, SNS or S3).
    """
    def __init__(__self__, __name__, __opts__=None, action=None, event_source_token=None, function=None, principal=None, qualifier=None, source_account=None, source_arn=None, statement_id=None, statement_id_prefix=None):
        """Create a Permission resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not action:
            raise TypeError('Missing required property action')
        __props__['action'] = action

        __props__['event_source_token'] = event_source_token

        if not function:
            raise TypeError('Missing required property function')
        __props__['function'] = function

        if not principal:
            raise TypeError('Missing required property principal')
        __props__['principal'] = principal

        __props__['qualifier'] = qualifier

        __props__['source_account'] = source_account

        __props__['source_arn'] = source_arn

        __props__['statement_id'] = statement_id

        __props__['statement_id_prefix'] = statement_id_prefix

        super(Permission, __self__).__init__(
            'aws:lambda/permission:Permission',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

