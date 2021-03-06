# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class AccountPublicAccessBlock(pulumi.CustomResource):
    """
    Manages S3 account-level Public Access Block configuration. For more information about these settings, see the [AWS S3 Block Public Access documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html).
    
    > **NOTE:** Each AWS account may only have one S3 Public Access Block configuration. Multiple configurations of the resource against the same AWS account will cause a perpetual difference.
    
    -> Advanced usage: To use a custom API endpoint for this Terraform resource, use the [`s3control` endpoint provider configuration](https://www.terraform.io/docs/providers/aws/index.html#s3control), not the `s3` endpoint provider configuration.
    """
    def __init__(__self__, __name__, __opts__=None, account_id=None, block_public_acls=None, block_public_policy=None, ignore_public_acls=None, restrict_public_buckets=None):
        """Create a AccountPublicAccessBlock resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['account_id'] = account_id

        __props__['block_public_acls'] = block_public_acls

        __props__['block_public_policy'] = block_public_policy

        __props__['ignore_public_acls'] = ignore_public_acls

        __props__['restrict_public_buckets'] = restrict_public_buckets

        super(AccountPublicAccessBlock, __self__).__init__(
            'aws:s3/accountPublicAccessBlock:AccountPublicAccessBlock',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

