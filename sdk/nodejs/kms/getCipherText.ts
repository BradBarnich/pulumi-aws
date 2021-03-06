// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The KMS ciphertext data source allows you to encrypt plaintext into ciphertext
 * by using an AWS KMS customer master key.
 * 
 * > **Note:** All arguments including the plaintext be stored in the raw state as plain-text.
 * [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
 */
export function getCipherText(args: GetCipherTextArgs, opts?: pulumi.InvokeOptions): Promise<GetCipherTextResult> {
    return pulumi.runtime.invoke("aws:kms/getCipherText:getCipherText", {
        "context": args.context,
        "keyId": args.keyId,
        "plaintext": args.plaintext,
    }, opts);
}

/**
 * A collection of arguments for invoking getCipherText.
 */
export interface GetCipherTextArgs {
    /**
     * An optional mapping that makes up the encryption context.
     */
    readonly context?: {[key: string]: string};
    /**
     * Globally unique key ID for the customer master key.
     */
    readonly keyId: string;
    /**
     * Data to be encrypted. Note that this may show up in logs, and it will be stored in the state file.
     */
    readonly plaintext: string;
}

/**
 * A collection of values returned by getCipherText.
 */
export interface GetCipherTextResult {
    /**
     * Base64 encoded ciphertext
     */
    readonly ciphertextBlob: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
