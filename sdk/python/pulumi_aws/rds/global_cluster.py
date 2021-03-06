# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class GlobalCluster(pulumi.CustomResource):
    """
    Manages a RDS Global Cluster, which is an Aurora global database spread across multiple regions. The global database contains a single primary cluster with read-write capability, and a read-only secondary cluster that receives data from the primary cluster through high-speed replication performed by the Aurora storage subsystem.
    
    More information about Aurora global databases can be found in the [Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html#aurora-global-database-creating).
    
    > **NOTE:** RDS only supports the `aurora` engine (MySQL 5.6 compatible) for Global Clusters at this time.
    """
    def __init__(__self__, __name__, __opts__=None, database_name=None, deletion_protection=None, engine=None, engine_version=None, global_cluster_identifier=None, storage_encrypted=None):
        """Create a GlobalCluster resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['database_name'] = database_name

        __props__['deletion_protection'] = deletion_protection

        __props__['engine'] = engine

        __props__['engine_version'] = engine_version

        if not global_cluster_identifier:
            raise TypeError('Missing required property global_cluster_identifier')
        __props__['global_cluster_identifier'] = global_cluster_identifier

        __props__['storage_encrypted'] = storage_encrypted

        __props__['arn'] = None
        __props__['global_cluster_resource_id'] = None

        super(GlobalCluster, __self__).__init__(
            'aws:rds/globalCluster:GlobalCluster',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

