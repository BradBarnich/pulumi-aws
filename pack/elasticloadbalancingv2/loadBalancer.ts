// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class LoadBalancer extends lumi.NamedResource implements LoadBalancerArgs {
    public readonly accessLogs?: { bucket: string, enabled?: boolean, prefix?: string }[];
    public /*out*/ readonly arn: string;
    public /*out*/ readonly arnSuffix: string;
    public /*out*/ readonly dnsName: string;
    public readonly enableDeletionProtection?: boolean;
    public readonly idleTimeout?: number;
    public readonly internal: boolean;
    public readonly ipAddressType: string;
    public readonly loadBalancerName: string;
    public readonly namePrefix?: string;
    public readonly securityGroups: string[];
    public readonly subnets: string[];
    public readonly tags?: {[key: string]: any};
    public /*out*/ readonly vpcId: string;
    public /*out*/ readonly zoneId: string;

    constructor(name: string, args: LoadBalancerArgs) {
        super(name);
        this.accessLogs = args.accessLogs;
        this.enableDeletionProtection = args.enableDeletionProtection;
        this.idleTimeout = args.idleTimeout;
        this.internal = args.internal;
        this.ipAddressType = args.ipAddressType;
        this.loadBalancerName = args.loadBalancerName;
        this.namePrefix = args.namePrefix;
        this.securityGroups = args.securityGroups;
        if (lumirt.defaultIfComputed(args.subnets, "") === undefined) {
            throw new Error("Property argument 'subnets' is required, but was missing");
        }
        this.subnets = args.subnets;
        this.tags = args.tags;
    }
}

export interface LoadBalancerArgs {
    readonly accessLogs?: { bucket: string, enabled?: boolean, prefix?: string }[];
    readonly enableDeletionProtection?: boolean;
    readonly idleTimeout?: number;
    readonly internal?: boolean;
    readonly ipAddressType?: string;
    readonly loadBalancerName?: string;
    readonly namePrefix?: string;
    readonly securityGroups?: string[];
    readonly subnets: string[];
    readonly tags?: {[key: string]: any};
}
