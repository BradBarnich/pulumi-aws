// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class Policy extends lumi.NamedResource implements PolicyArgs {
    public readonly adjustmentType: string;
    public /*out*/ readonly arn: string;
    public readonly autoscalingGroupName: string;
    public readonly cooldown?: number;
    public readonly estimatedInstanceWarmup?: number;
    public readonly metricAggregationType: string;
    public readonly minAdjustmentMagnitude?: number;
    public readonly minAdjustmentStep?: number;
    public readonly policyName?: string;
    public readonly policyType?: string;
    public readonly scalingAdjustment?: number;
    public readonly stepAdjustment?: { metricIntervalLowerBound?: string, metricIntervalUpperBound?: string, scalingAdjustment: number }[];

    constructor(name: string, args: PolicyArgs) {
        super(name);
        if (lumirt.defaultIfComputed(args.adjustmentType, "") === undefined) {
            throw new Error("Property argument 'adjustmentType' is required, but was missing");
        }
        this.adjustmentType = args.adjustmentType;
        if (lumirt.defaultIfComputed(args.autoscalingGroupName, "") === undefined) {
            throw new Error("Property argument 'autoscalingGroupName' is required, but was missing");
        }
        this.autoscalingGroupName = args.autoscalingGroupName;
        this.cooldown = args.cooldown;
        this.estimatedInstanceWarmup = args.estimatedInstanceWarmup;
        this.metricAggregationType = args.metricAggregationType;
        this.minAdjustmentMagnitude = args.minAdjustmentMagnitude;
        this.minAdjustmentStep = args.minAdjustmentStep;
        this.policyName = args.policyName;
        this.policyType = args.policyType;
        this.scalingAdjustment = args.scalingAdjustment;
        this.stepAdjustment = args.stepAdjustment;
    }
}

export interface PolicyArgs {
    readonly adjustmentType: string;
    readonly autoscalingGroupName: string;
    readonly cooldown?: number;
    readonly estimatedInstanceWarmup?: number;
    readonly metricAggregationType?: string;
    readonly minAdjustmentMagnitude?: number;
    readonly minAdjustmentStep?: number;
    readonly policyName?: string;
    readonly policyType?: string;
    readonly scalingAdjustment?: number;
    readonly stepAdjustment?: { metricIntervalLowerBound?: string, metricIntervalUpperBound?: string, scalingAdjustment: number }[];
}
