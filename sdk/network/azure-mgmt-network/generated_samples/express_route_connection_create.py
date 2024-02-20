# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python express_route_connection_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.express_route_connections.begin_create_or_update(
        resource_group_name="resourceGroupName",
        express_route_gateway_name="gateway-2",
        connection_name="connectionName",
        put_express_route_connection_parameters={
            "id": "/subscriptions/subid/resourceGroups/resourceGroupName/providers/Microsoft.Network/expressRouteGateways/gateway-2/expressRouteConnections/connectionName",
            "name": "connectionName",
            "properties": {
                "authorizationKey": "authorizationKey",
                "expressRouteCircuitPeering": {
                    "id": "/subscriptions/subid/resourceGroups/resourceGroupName/providers/Microsoft.Network/expressRouteCircuits/circuitName/peerings/AzurePrivatePeering"
                },
                "routingConfiguration": {
                    "associatedRouteTable": {
                        "id": "/subscriptions/subid/resourceGroups/resourceGroupName/providers/Microsoft.Network/virtualHubs/hub1/hubRouteTables/hubRouteTable1"
                    },
                    "inboundRouteMap": {
                        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualHubs/virtualHub1/routeMaps/routeMap1"
                    },
                    "outboundRouteMap": {
                        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualHubs/virtualHub1/routeMaps/routeMap2"
                    },
                    "propagatedRouteTables": {
                        "ids": [
                            {
                                "id": "/subscriptions/subid/resourceGroups/resourceGroupName/providers/Microsoft.Network/virtualHubs/hub1/hubRouteTables/hubRouteTable1"
                            },
                            {
                                "id": "/subscriptions/subid/resourceGroups/resourceGroupName/providers/Microsoft.Network/virtualHubs/hub1/hubRouteTables/hubRouteTable2"
                            },
                            {
                                "id": "/subscriptions/subid/resourceGroups/resourceGroupName/providers/Microsoft.Network/virtualHubs/hub1/hubRouteTables/hubRouteTable3"
                            },
                        ],
                        "labels": ["label1", "label2"],
                    },
                },
                "routingWeight": 2,
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-06-01/examples/ExpressRouteConnectionCreate.json
if __name__ == "__main__":
    main()
