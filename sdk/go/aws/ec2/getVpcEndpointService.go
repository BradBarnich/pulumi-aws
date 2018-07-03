// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The VPC Endpoint Service data source details about a specific service that
// can be specified when creating a VPC endpoint within the region configured in the provider.
func LookupVpcEndpointService(ctx *pulumi.Context, args *GetVpcEndpointServiceArgs) (*GetVpcEndpointServiceResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["service"] = args.Service
		inputs["serviceName"] = args.ServiceName
	}
	outputs, err := ctx.Invoke("aws:ec2/getVpcEndpointService:getVpcEndpointService", inputs)
	if err != nil {
		return nil, err
	}
	return &GetVpcEndpointServiceResult{
		AcceptanceRequired: outputs["acceptanceRequired"],
		AvailabilityZones: outputs["availabilityZones"],
		BaseEndpointDnsNames: outputs["baseEndpointDnsNames"],
		Owner: outputs["owner"],
		PrivateDnsName: outputs["privateDnsName"],
		ServiceName: outputs["serviceName"],
		ServiceType: outputs["serviceType"],
		VpcEndpointPolicySupported: outputs["vpcEndpointPolicySupported"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getVpcEndpointService.
type GetVpcEndpointServiceArgs struct {
	// The common name of an AWS service (e.g. `s3`).
	Service interface{}
	// The service name that can be specified when creating a VPC endpoint.
	ServiceName interface{}
}

// A collection of values returned by getVpcEndpointService.
type GetVpcEndpointServiceResult struct {
	// Whether or not VPC endpoint connection requests to the service must be accepted by the service owner - `true` or `false`.
	AcceptanceRequired interface{}
	// The Availability Zones in which the service is available.
	AvailabilityZones interface{}
	// The DNS names for the service.
	BaseEndpointDnsNames interface{}
	// The AWS account ID of the service owner or `amazon`.
	Owner interface{}
	// The private DNS name for the service.
	PrivateDnsName interface{}
	ServiceName interface{}
	// The service type, `Gateway` or `Interface`.
	ServiceType interface{}
	// Whether or not the service supports endpoint policies - `true` or `false`.
	VpcEndpointPolicySupported interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
