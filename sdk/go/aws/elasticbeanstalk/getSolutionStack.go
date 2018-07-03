// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticbeanstalk

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get the name of a elastic beanstalk solution stack.
func LookupSolutionStack(ctx *pulumi.Context, args *GetSolutionStackArgs) (*GetSolutionStackResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["mostRecent"] = args.MostRecent
		inputs["nameRegex"] = args.NameRegex
	}
	outputs, err := ctx.Invoke("aws:elasticbeanstalk/getSolutionStack:getSolutionStack", inputs)
	if err != nil {
		return nil, err
	}
	return &GetSolutionStackResult{
		Name: outputs["name"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getSolutionStack.
type GetSolutionStackArgs struct {
	// If more than one result is returned, use the most
	// recent solution stack.
	MostRecent interface{}
	// A regex string to apply to the solution stack list returned
	// by AWS. See [Elastic Beanstalk Supported Platforms][beanstalk-platforms] from
	// AWS documentation for reference solution stack names.
	NameRegex interface{}
}

// A collection of values returned by getSolutionStack.
type GetSolutionStackResult struct {
	// The name of the solution stack.
	Name interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
