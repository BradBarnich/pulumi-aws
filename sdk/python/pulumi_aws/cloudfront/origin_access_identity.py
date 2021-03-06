# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class OriginAccessIdentity(pulumi.CustomResource):
    """
    Creates an Amazon CloudFront origin access identity.
    
    For information about CloudFront distributions, see the
    [Amazon CloudFront Developer Guide][1]. For more information on generating
    origin access identities, see
    [Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content][2].
    """
    def __init__(__self__, __name__, __opts__=None, comment=None):
        """Create a OriginAccessIdentity resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['comment'] = comment

        __props__['caller_reference'] = None
        __props__['cloudfront_access_identity_path'] = None
        __props__['etag'] = None
        __props__['iam_arn'] = None
        __props__['s3_canonical_user_id'] = None

        super(OriginAccessIdentity, __self__).__init__(
            'aws:cloudfront/originAccessIdentity:OriginAccessIdentity',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

