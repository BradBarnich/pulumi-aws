# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GetCanonicalUserIdResult(object):
    """
    A collection of values returned by getCanonicalUserId.
    """
    def __init__(__self__, display_name=None, id=None):
        if display_name and not isinstance(display_name, basestring):
            raise TypeError('Expected argument display_name to be a basestring')
        __self__.display_name = display_name
        """
        The human-friendly name linked to the canonical user ID.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_canonical_user_id():
    """
    The Canonical User ID data source allows access to the [canonical user ID](http://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html)
    for the effective account in which Terraform is working.
    """
    __args__ = dict()

    __ret__ = pulumi.runtime.invoke('aws:index/getCanonicalUserId:getCanonicalUserId', __args__)

    return GetCanonicalUserIdResult(
        display_name=__ret__.get('displayName'),
        id=__ret__.get('id'))
