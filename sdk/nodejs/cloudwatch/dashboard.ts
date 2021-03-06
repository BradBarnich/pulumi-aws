// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a CloudWatch Dashboard resource.
 */
export class Dashboard extends pulumi.CustomResource {
    /**
     * Get an existing Dashboard resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DashboardState, opts?: pulumi.CustomResourceOptions): Dashboard {
        return new Dashboard(name, <any>state, { ...opts, id: id });
    }

    /**
     * The Amazon Resource Name (ARN) of the dashboard.
     */
    public /*out*/ readonly dashboardArn: pulumi.Output<string>;
    /**
     * The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).
     */
    public readonly dashboardBody: pulumi.Output<string>;
    /**
     * The name of the dashboard.
     */
    public readonly dashboardName: pulumi.Output<string>;

    /**
     * Create a Dashboard resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DashboardArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DashboardArgs | DashboardState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: DashboardState = argsOrState as DashboardState | undefined;
            inputs["dashboardArn"] = state ? state.dashboardArn : undefined;
            inputs["dashboardBody"] = state ? state.dashboardBody : undefined;
            inputs["dashboardName"] = state ? state.dashboardName : undefined;
        } else {
            const args = argsOrState as DashboardArgs | undefined;
            if (!args || args.dashboardBody === undefined) {
                throw new Error("Missing required property 'dashboardBody'");
            }
            if (!args || args.dashboardName === undefined) {
                throw new Error("Missing required property 'dashboardName'");
            }
            inputs["dashboardBody"] = args ? args.dashboardBody : undefined;
            inputs["dashboardName"] = args ? args.dashboardName : undefined;
            inputs["dashboardArn"] = undefined /*out*/;
        }
        super("aws:cloudwatch/dashboard:Dashboard", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Dashboard resources.
 */
export interface DashboardState {
    /**
     * The Amazon Resource Name (ARN) of the dashboard.
     */
    readonly dashboardArn?: pulumi.Input<string>;
    /**
     * The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).
     */
    readonly dashboardBody?: pulumi.Input<string>;
    /**
     * The name of the dashboard.
     */
    readonly dashboardName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Dashboard resource.
 */
export interface DashboardArgs {
    /**
     * The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).
     */
    readonly dashboardBody: pulumi.Input<string>;
    /**
     * The name of the dashboard.
     */
    readonly dashboardName: pulumi.Input<string>;
}
