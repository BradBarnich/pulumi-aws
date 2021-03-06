# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Policy(pulumi.CustomResource):
    """
    Provides an Application AutoScaling Policy resource.
    """
    def __init__(__self__, __name__, __opts__=None, adjustment_type=None, alarms=None, cooldown=None, metric_aggregation_type=None, min_adjustment_magnitude=None, name=None, policy_type=None, resource_id=None, scalable_dimension=None, service_namespace=None, step_adjustments=None, step_scaling_policy_configurations=None, target_tracking_scaling_policy_configuration=None):
        """Create a Policy resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['adjustment_type'] = adjustment_type

        __props__['alarms'] = alarms

        __props__['cooldown'] = cooldown

        __props__['metric_aggregation_type'] = metric_aggregation_type

        __props__['min_adjustment_magnitude'] = min_adjustment_magnitude

        __props__['name'] = name

        __props__['policy_type'] = policy_type

        if not resource_id:
            raise TypeError('Missing required property resource_id')
        __props__['resource_id'] = resource_id

        if not scalable_dimension:
            raise TypeError('Missing required property scalable_dimension')
        __props__['scalable_dimension'] = scalable_dimension

        if not service_namespace:
            raise TypeError('Missing required property service_namespace')
        __props__['service_namespace'] = service_namespace

        __props__['step_adjustments'] = step_adjustments

        __props__['step_scaling_policy_configurations'] = step_scaling_policy_configurations

        __props__['target_tracking_scaling_policy_configuration'] = target_tracking_scaling_policy_configuration

        __props__['arn'] = None

        super(Policy, __self__).__init__(
            'aws:appautoscaling/policy:Policy',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

