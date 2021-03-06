# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetSecretResult(object):
    """
    A collection of values returned by getSecret.
    """
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_secret(__has_dynamic_attributes=None, secrets=None):
    """
    !> **WARNING:** This data source is deprecated and will be removed in the next major version. You can migrate existing configurations to the [`aws_kms_secrets` data source](https://www.terraform.io/docs/providers/aws/d/kms_secrets.html) following instructions available in the [Version 2 Upgrade Guide](https://www.terraform.io/docs/providers/aws/guides/version-2-upgrade.html#data-source-aws_kms_secret).
    
    The KMS secret data source allows you to use data encrypted with the AWS KMS
    service within your resource definitions.
    
    > **NOTE**: Using this data provider will allow you to conceal secret data within your
    resource definitions but does not take care of protecting that data in the
    logging output, plan output or state output.
    
    Please take care to secure your secret data outside of resource definitions.
    """
    __args__ = dict()

    __args__['__hasDynamicAttributes'] = __has_dynamic_attributes
    __args__['secrets'] = secrets
    __ret__ = await pulumi.runtime.invoke('aws:kms/getSecret:getSecret', __args__)

    return GetSecretResult(
        id=__ret__.get('id'))
