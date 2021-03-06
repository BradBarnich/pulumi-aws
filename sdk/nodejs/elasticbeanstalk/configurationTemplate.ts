// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides an Elastic Beanstalk Configuration Template, which are associated with
 * a specific application and are used to deploy different versions of the
 * application with the same configuration settings.
 */
export class ConfigurationTemplate extends pulumi.CustomResource {
    /**
     * Get an existing ConfigurationTemplate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConfigurationTemplateState, opts?: pulumi.CustomResourceOptions): ConfigurationTemplate {
        return new ConfigurationTemplate(name, <any>state, { ...opts, id: id });
    }

    /**
     * name of the application to associate with this configuration template
     */
    public readonly application: pulumi.Output<string>;
    /**
     * Short description of the Template
     */
    public readonly description: pulumi.Output<string | undefined>;
    /**
     * The ID of the environment used with this configuration template
     */
    public readonly environmentId: pulumi.Output<string | undefined>;
    /**
     * A unique name for this Template.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * Option settings to configure the new Environment. These
     * override specific values that are set as defaults. The format is detailed
     * below in Option Settings
     */
    public readonly settings: pulumi.Output<{ name: string, namespace: string, resource?: string, value: string }[]>;
    /**
     * A solution stack to base your Template
     * off of. Example stacks can be found in the [Amazon API documentation][1]
     */
    public readonly solutionStackName: pulumi.Output<string | undefined>;

    /**
     * Create a ConfigurationTemplate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConfigurationTemplateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ConfigurationTemplateArgs | ConfigurationTemplateState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ConfigurationTemplateState = argsOrState as ConfigurationTemplateState | undefined;
            inputs["application"] = state ? state.application : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["environmentId"] = state ? state.environmentId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["settings"] = state ? state.settings : undefined;
            inputs["solutionStackName"] = state ? state.solutionStackName : undefined;
        } else {
            const args = argsOrState as ConfigurationTemplateArgs | undefined;
            if (!args || args.application === undefined) {
                throw new Error("Missing required property 'application'");
            }
            inputs["application"] = args ? args.application : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["environmentId"] = args ? args.environmentId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["settings"] = args ? args.settings : undefined;
            inputs["solutionStackName"] = args ? args.solutionStackName : undefined;
        }
        super("aws:elasticbeanstalk/configurationTemplate:ConfigurationTemplate", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ConfigurationTemplate resources.
 */
export interface ConfigurationTemplateState {
    /**
     * name of the application to associate with this configuration template
     */
    readonly application?: pulumi.Input<string>;
    /**
     * Short description of the Template
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The ID of the environment used with this configuration template
     */
    readonly environmentId?: pulumi.Input<string>;
    /**
     * A unique name for this Template.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Option settings to configure the new Environment. These
     * override specific values that are set as defaults. The format is detailed
     * below in Option Settings
     */
    readonly settings?: pulumi.Input<pulumi.Input<{ name: pulumi.Input<string>, namespace: pulumi.Input<string>, resource?: pulumi.Input<string>, value: pulumi.Input<string> }>[]>;
    /**
     * A solution stack to base your Template
     * off of. Example stacks can be found in the [Amazon API documentation][1]
     */
    readonly solutionStackName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ConfigurationTemplate resource.
 */
export interface ConfigurationTemplateArgs {
    /**
     * name of the application to associate with this configuration template
     */
    readonly application: pulumi.Input<string>;
    /**
     * Short description of the Template
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The ID of the environment used with this configuration template
     */
    readonly environmentId?: pulumi.Input<string>;
    /**
     * A unique name for this Template.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Option settings to configure the new Environment. These
     * override specific values that are set as defaults. The format is detailed
     * below in Option Settings
     */
    readonly settings?: pulumi.Input<pulumi.Input<{ name: pulumi.Input<string>, namespace: pulumi.Input<string>, resource?: pulumi.Input<string>, value: pulumi.Input<string> }>[]>;
    /**
     * A solution stack to base your Template
     * off of. Example stacks can be found in the [Amazon API documentation][1]
     */
    readonly solutionStackName?: pulumi.Input<string>;
}
