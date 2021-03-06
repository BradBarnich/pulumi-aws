# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class DomainName(pulumi.CustomResource):
    """
    Registers a custom domain name for use with AWS API Gateway.
    
    This resource just establishes ownership of and the TLS settings for
    a particular domain name. An API can be attached to a particular path
    under the registered domain name using
    the `aws_api_gateway_base_path_mapping` resource.
    
    API Gateway domains can be defined as either 'edge-optimized' or 'regional'.  In an edge-optimized configuration,
    API Gateway internally creates and manages a CloudFront distribution to route requests on the given hostname. In
    addition to this resource it's necessary to create a DNS record corresponding to the given domain name which is an alias
    (either Route53 alias or traditional CNAME) to the Cloudfront domain name exported in the `cloudfront_domain_name`
    attribute.
    
    In a regional configuration, API Gateway does not create a CloudFront distribution to route requests to the API, though
    a distribution can be created if needed. In either case, it is necessary to create a DNS record corresponding to the
    given domain name which is an alias (either Route53 alias or traditional CNAME) to the regional domain name exported in
    the `regional_domain_name` attribute.
    
    > **Note:** All arguments including the private key will be stored in the raw state as plain-text.
    [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
    """
    def __init__(__self__, __name__, __opts__=None, certificate_arn=None, certificate_body=None, certificate_chain=None, certificate_name=None, certificate_private_key=None, domain_name=None, endpoint_configuration=None, regional_certificate_arn=None, regional_certificate_name=None):
        """Create a DomainName resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['certificate_arn'] = certificate_arn

        __props__['certificate_body'] = certificate_body

        __props__['certificate_chain'] = certificate_chain

        __props__['certificate_name'] = certificate_name

        __props__['certificate_private_key'] = certificate_private_key

        if not domain_name:
            raise TypeError('Missing required property domain_name')
        __props__['domain_name'] = domain_name

        __props__['endpoint_configuration'] = endpoint_configuration

        __props__['regional_certificate_arn'] = regional_certificate_arn

        __props__['regional_certificate_name'] = regional_certificate_name

        __props__['certificate_upload_date'] = None
        __props__['cloudfront_domain_name'] = None
        __props__['cloudfront_zone_id'] = None
        __props__['regional_domain_name'] = None
        __props__['regional_zone_id'] = None

        super(DomainName, __self__).__init__(
            'aws:apigateway/domainName:DomainName',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

