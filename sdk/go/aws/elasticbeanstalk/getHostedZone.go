// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticbeanstalk

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get the ID of an [elastic beanstalk hosted zone](http://docs.aws.amazon.com/general/latest/gr/rande.html#elasticbeanstalk_region).
func LookupHostedZone(ctx *pulumi.Context, args *GetHostedZoneArgs) (*GetHostedZoneResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["region"] = args.Region
	}
	outputs, err := ctx.Invoke("aws:elasticbeanstalk/getHostedZone:getHostedZone", inputs)
	if err != nil {
		return nil, err
	}
	return &GetHostedZoneResult{
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getHostedZone.
type GetHostedZoneArgs struct {
	// The region you'd like the zone for. By default, fetches the current region.
	Region interface{}
}

// A collection of values returned by getHostedZone.
type GetHostedZoneResult struct {
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
