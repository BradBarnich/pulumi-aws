// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class DefaultRouteTable extends lumi.NamedResource implements DefaultRouteTableArgs {
    public readonly defaultRouteTableId: string;
    public readonly propagatingVgws?: string[];
    public readonly route: { cidrBlock?: string, egressOnlyGatewayId?: string, gatewayId?: string, instanceId?: string, ipv6CidrBlock?: string, natGatewayId?: string, networkInterfaceId?: string, vpcPeeringConnectionId?: string }[];
    public readonly tags?: {[key: string]: any};
    public /*out*/ readonly vpcId: string;

    constructor(name: string, args: DefaultRouteTableArgs) {
        super(name);
        if (lumirt.defaultIfComputed(args.defaultRouteTableId, "") === undefined) {
            throw new Error("Property argument 'defaultRouteTableId' is required, but was missing");
        }
        this.defaultRouteTableId = args.defaultRouteTableId;
        this.propagatingVgws = args.propagatingVgws;
        this.route = args.route;
        this.tags = args.tags;
    }
}

export interface DefaultRouteTableArgs {
    readonly defaultRouteTableId: string;
    readonly propagatingVgws?: string[];
    readonly route?: { cidrBlock?: string, egressOnlyGatewayId?: string, gatewayId?: string, instanceId?: string, ipv6CidrBlock?: string, natGatewayId?: string, networkInterfaceId?: string, vpcPeeringConnectionId?: string }[];
    readonly tags?: {[key: string]: any};
}
