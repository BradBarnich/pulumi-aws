// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudformation

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The CloudFormation Stack data source allows access to stack
// outputs and other useful data including the template body.
func LookupStack(ctx *pulumi.Context, args *GetStackArgs) (*GetStackResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
	}
	outputs, err := ctx.Invoke("aws:cloudformation/getStack:getStack", inputs)
	if err != nil {
		return nil, err
	}
	return &GetStackResult{
		Capabilities: outputs["capabilities"],
		Description: outputs["description"],
		DisableRollback: outputs["disableRollback"],
		IamRoleArn: outputs["iamRoleArn"],
		NotificationArns: outputs["notificationArns"],
		Outputs: outputs["outputs"],
		Parameters: outputs["parameters"],
		Tags: outputs["tags"],
		TemplateBody: outputs["templateBody"],
		TimeoutInMinutes: outputs["timeoutInMinutes"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getStack.
type GetStackArgs struct {
	// The name of the stack
	Name interface{}
}

// A collection of values returned by getStack.
type GetStackResult struct {
	// A list of capabilities
	Capabilities interface{}
	// Description of the stack
	Description interface{}
	// Whether the rollback of the stack is disabled when stack creation fails
	DisableRollback interface{}
	// The ARN of the IAM role used to create the stack.
	IamRoleArn interface{}
	// A list of SNS topic ARNs to publish stack related events
	NotificationArns interface{}
	// A map of outputs from the stack.
	Outputs interface{}
	// A map of parameters that specify input parameters for the stack.
	Parameters interface{}
	// A map of tags associated with this stack.
	Tags interface{}
	// Structure containing the template body.
	TemplateBody interface{}
	// The amount of time that can pass before the stack status becomes `CREATE_FAILED`
	TimeoutInMinutes interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
