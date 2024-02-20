# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-compute
# USAGE
    python virtual_machine_scale_set_vm_run_command_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.virtual_machine_scale_set_vm_run_commands.begin_create_or_update(
        resource_group_name="myResourceGroup",
        vm_scale_set_name="myvmScaleSet",
        instance_id="0",
        run_command_name="myRunCommand",
        run_command={
            "location": "West US",
            "properties": {
                "asyncExecution": False,
                "errorBlobManagedIdentity": {},
                "errorBlobUri": "https://mystorageaccount.blob.core.windows.net/mycontainer/MyScriptError.txt",
                "outputBlobManagedIdentity": {"clientId": "22d35efb-0c99-4041-8c5b-6d24db33a69a"},
                "outputBlobUri": "https://mystorageaccount.blob.core.windows.net/myscriptoutputcontainer/MyScriptoutput.txt",
                "parameters": [{"name": "param1", "value": "value1"}, {"name": "param2", "value": "value2"}],
                "runAsPassword": "<runAsPassword>",
                "runAsUser": "user1",
                "source": {
                    "scriptUri": "https://mystorageaccount.blob.core.windows.net/scriptcontainer/MyScript.ps1",
                    "scriptUriManagedIdentity": {"objectId": "4231e4d2-33e4-4e23-96b2-17888afa6072"},
                },
                "timeoutInSeconds": 3600,
                "treatFailureAsDeploymentFailure": True,
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2023-09-01/examples/runCommandExamples/VirtualMachineScaleSetVMRunCommand_CreateOrUpdate.json
if __name__ == "__main__":
    main()
