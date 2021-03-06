// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {ARN} from "../index";
import {Group} from "./group";
import {Role} from "./role";
import {User} from "./user";

/**
 * Attaches a Managed IAM Policy to user(s), role(s), and/or group(s)
 * 
 * !> **WARNING:** The aws_iam_policy_attachment resource creates **exclusive** attachments of IAM policies. Across the entire AWS account, all of the users/roles/groups to which a single policy is attached must be declared by a single aws_iam_policy_attachment resource. This means that even any users/roles/groups that have the attached policy via any other mechanism (including other Terraform resources) will have that attached policy revoked by this resource. Consider `aws_iam_role_policy_attachment`, `aws_iam_user_policy_attachment`, or `aws_iam_group_policy_attachment` instead. These resources do not enforce exclusive attachment of an IAM policy.
 * 
 * > **NOTE:** The usage of this resource conflicts with the `aws_iam_group_policy_attachment`, `aws_iam_role_policy_attachment`, and `aws_iam_user_policy_attachment` resources and will permanently show a difference if both are defined.
 */
export class PolicyAttachment extends pulumi.CustomResource {
    /**
     * Get an existing PolicyAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyAttachmentState, opts?: pulumi.CustomResourceOptions): PolicyAttachment {
        return new PolicyAttachment(name, <any>state, { ...opts, id: id });
    }

    /**
     * The group(s) the policy should be applied to
     */
    public readonly groups: pulumi.Output<Group[] | undefined>;
    /**
     * The name of the attachment. This cannot be an empty string.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The ARN of the policy you want to apply
     */
    public readonly policyArn: pulumi.Output<ARN>;
    /**
     * The role(s) the policy should be applied to
     */
    public readonly roles: pulumi.Output<Role[] | undefined>;
    /**
     * The user(s) the policy should be applied to
     */
    public readonly users: pulumi.Output<User[] | undefined>;

    /**
     * Create a PolicyAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PolicyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PolicyAttachmentArgs | PolicyAttachmentState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: PolicyAttachmentState = argsOrState as PolicyAttachmentState | undefined;
            inputs["groups"] = state ? state.groups : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["policyArn"] = state ? state.policyArn : undefined;
            inputs["roles"] = state ? state.roles : undefined;
            inputs["users"] = state ? state.users : undefined;
        } else {
            const args = argsOrState as PolicyAttachmentArgs | undefined;
            if (!args || args.policyArn === undefined) {
                throw new Error("Missing required property 'policyArn'");
            }
            inputs["groups"] = args ? args.groups : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["policyArn"] = args ? args.policyArn : undefined;
            inputs["roles"] = args ? args.roles : undefined;
            inputs["users"] = args ? args.users : undefined;
        }
        super("aws:iam/policyAttachment:PolicyAttachment", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PolicyAttachment resources.
 */
export interface PolicyAttachmentState {
    /**
     * The group(s) the policy should be applied to
     */
    readonly groups?: pulumi.Input<pulumi.Input<Group>[]>;
    /**
     * The name of the attachment. This cannot be an empty string.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ARN of the policy you want to apply
     */
    readonly policyArn?: pulumi.Input<ARN>;
    /**
     * The role(s) the policy should be applied to
     */
    readonly roles?: pulumi.Input<pulumi.Input<Role>[]>;
    /**
     * The user(s) the policy should be applied to
     */
    readonly users?: pulumi.Input<pulumi.Input<User>[]>;
}

/**
 * The set of arguments for constructing a PolicyAttachment resource.
 */
export interface PolicyAttachmentArgs {
    /**
     * The group(s) the policy should be applied to
     */
    readonly groups?: pulumi.Input<pulumi.Input<Group>[]>;
    /**
     * The name of the attachment. This cannot be an empty string.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ARN of the policy you want to apply
     */
    readonly policyArn: pulumi.Input<ARN>;
    /**
     * The role(s) the policy should be applied to
     */
    readonly roles?: pulumi.Input<pulumi.Input<Role>[]>;
    /**
     * The user(s) the policy should be applied to
     */
    readonly users?: pulumi.Input<pulumi.Input<User>[]>;
}
