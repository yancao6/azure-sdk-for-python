# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ApplicationDeltaHealthPolicy
from ._models_py3 import ApplicationHealthPolicy
from ._models_py3 import ApplicationMetricDescription
from ._models_py3 import ApplicationResource
from ._models_py3 import ApplicationResourceList
from ._models_py3 import ApplicationResourceProperties
from ._models_py3 import ApplicationResourceUpdate
from ._models_py3 import ApplicationResourceUpdateProperties
from ._models_py3 import ApplicationTypeResource
from ._models_py3 import ApplicationTypeResourceList
from ._models_py3 import ApplicationTypeVersionResource
from ._models_py3 import ApplicationTypeVersionResourceList
from ._models_py3 import ApplicationTypeVersionsCleanupPolicy
from ._models_py3 import ApplicationUpgradePolicy
from ._models_py3 import ApplicationUserAssignedIdentity
from ._models_py3 import ArmApplicationHealthPolicy
from ._models_py3 import ArmRollingUpgradeMonitoringPolicy
from ._models_py3 import ArmServiceTypeHealthPolicy
from ._models_py3 import AvailableOperationDisplay
from ._models_py3 import AzureActiveDirectory
from ._models_py3 import CertificateDescription
from ._models_py3 import ClientCertificateCommonName
from ._models_py3 import ClientCertificateThumbprint
from ._models_py3 import Cluster
from ._models_py3 import ClusterCodeVersionsListResult
from ._models_py3 import ClusterCodeVersionsResult
from ._models_py3 import ClusterHealthPolicy
from ._models_py3 import ClusterListResult
from ._models_py3 import ClusterUpdateParameters
from ._models_py3 import ClusterUpgradeDeltaHealthPolicy
from ._models_py3 import ClusterUpgradePolicy
from ._models_py3 import ClusterVersionDetails
from ._models_py3 import DiagnosticsStorageAccountConfig
from ._models_py3 import EndpointRangeDescription
from ._models_py3 import ErrorModel
from ._models_py3 import ErrorModelError
from ._models_py3 import ManagedIdentity
from ._models_py3 import NamedPartitionSchemeDescription
from ._models_py3 import NodeTypeDescription
from ._models_py3 import Notification
from ._models_py3 import NotificationTarget
from ._models_py3 import OperationListResult
from ._models_py3 import OperationResult
from ._models_py3 import PartitionSchemeDescription
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import ServerCertificateCommonName
from ._models_py3 import ServerCertificateCommonNames
from ._models_py3 import ServiceCorrelationDescription
from ._models_py3 import ServiceLoadMetricDescription
from ._models_py3 import ServicePlacementPolicyDescription
from ._models_py3 import ServiceResource
from ._models_py3 import ServiceResourceList
from ._models_py3 import ServiceResourceProperties
from ._models_py3 import ServiceResourcePropertiesBase
from ._models_py3 import ServiceResourceUpdate
from ._models_py3 import ServiceResourceUpdateProperties
from ._models_py3 import ServiceTypeDeltaHealthPolicy
from ._models_py3 import ServiceTypeHealthPolicy
from ._models_py3 import SettingsParameterDescription
from ._models_py3 import SettingsSectionDescription
from ._models_py3 import SingletonPartitionSchemeDescription
from ._models_py3 import StatefulServiceProperties
from ._models_py3 import StatefulServiceUpdateProperties
from ._models_py3 import StatelessServiceProperties
from ._models_py3 import StatelessServiceUpdateProperties
from ._models_py3 import SystemData
from ._models_py3 import UniformInt64RangePartitionSchemeDescription
from ._models_py3 import UpgradableVersionPathResult
from ._models_py3 import UpgradableVersionsDescription
from ._models_py3 import UserAssignedIdentity

from ._service_fabric_management_client_enums import AddOnFeatures
from ._service_fabric_management_client_enums import ArmServicePackageActivationMode
from ._service_fabric_management_client_enums import ArmUpgradeFailureAction
from ._service_fabric_management_client_enums import ClusterEnvironment
from ._service_fabric_management_client_enums import ClusterState
from ._service_fabric_management_client_enums import ClusterUpgradeCadence
from ._service_fabric_management_client_enums import ClusterVersionsEnvironment
from ._service_fabric_management_client_enums import DurabilityLevel
from ._service_fabric_management_client_enums import ManagedIdentityType
from ._service_fabric_management_client_enums import MoveCost
from ._service_fabric_management_client_enums import NotificationCategory
from ._service_fabric_management_client_enums import NotificationChannel
from ._service_fabric_management_client_enums import NotificationLevel
from ._service_fabric_management_client_enums import PartitionScheme
from ._service_fabric_management_client_enums import ProvisioningState
from ._service_fabric_management_client_enums import ReliabilityLevel
from ._service_fabric_management_client_enums import RollingUpgradeMode
from ._service_fabric_management_client_enums import ServiceCorrelationScheme
from ._service_fabric_management_client_enums import ServiceKind
from ._service_fabric_management_client_enums import ServiceLoadMetricWeight
from ._service_fabric_management_client_enums import ServicePlacementPolicyType
from ._service_fabric_management_client_enums import SfZonalUpgradeMode
from ._service_fabric_management_client_enums import StoreName
from ._service_fabric_management_client_enums import UpgradeMode
from ._service_fabric_management_client_enums import VmssZonalUpgradeMode
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ApplicationDeltaHealthPolicy",
    "ApplicationHealthPolicy",
    "ApplicationMetricDescription",
    "ApplicationResource",
    "ApplicationResourceList",
    "ApplicationResourceProperties",
    "ApplicationResourceUpdate",
    "ApplicationResourceUpdateProperties",
    "ApplicationTypeResource",
    "ApplicationTypeResourceList",
    "ApplicationTypeVersionResource",
    "ApplicationTypeVersionResourceList",
    "ApplicationTypeVersionsCleanupPolicy",
    "ApplicationUpgradePolicy",
    "ApplicationUserAssignedIdentity",
    "ArmApplicationHealthPolicy",
    "ArmRollingUpgradeMonitoringPolicy",
    "ArmServiceTypeHealthPolicy",
    "AvailableOperationDisplay",
    "AzureActiveDirectory",
    "CertificateDescription",
    "ClientCertificateCommonName",
    "ClientCertificateThumbprint",
    "Cluster",
    "ClusterCodeVersionsListResult",
    "ClusterCodeVersionsResult",
    "ClusterHealthPolicy",
    "ClusterListResult",
    "ClusterUpdateParameters",
    "ClusterUpgradeDeltaHealthPolicy",
    "ClusterUpgradePolicy",
    "ClusterVersionDetails",
    "DiagnosticsStorageAccountConfig",
    "EndpointRangeDescription",
    "ErrorModel",
    "ErrorModelError",
    "ManagedIdentity",
    "NamedPartitionSchemeDescription",
    "NodeTypeDescription",
    "Notification",
    "NotificationTarget",
    "OperationListResult",
    "OperationResult",
    "PartitionSchemeDescription",
    "ProxyResource",
    "Resource",
    "ServerCertificateCommonName",
    "ServerCertificateCommonNames",
    "ServiceCorrelationDescription",
    "ServiceLoadMetricDescription",
    "ServicePlacementPolicyDescription",
    "ServiceResource",
    "ServiceResourceList",
    "ServiceResourceProperties",
    "ServiceResourcePropertiesBase",
    "ServiceResourceUpdate",
    "ServiceResourceUpdateProperties",
    "ServiceTypeDeltaHealthPolicy",
    "ServiceTypeHealthPolicy",
    "SettingsParameterDescription",
    "SettingsSectionDescription",
    "SingletonPartitionSchemeDescription",
    "StatefulServiceProperties",
    "StatefulServiceUpdateProperties",
    "StatelessServiceProperties",
    "StatelessServiceUpdateProperties",
    "SystemData",
    "UniformInt64RangePartitionSchemeDescription",
    "UpgradableVersionPathResult",
    "UpgradableVersionsDescription",
    "UserAssignedIdentity",
    "AddOnFeatures",
    "ArmServicePackageActivationMode",
    "ArmUpgradeFailureAction",
    "ClusterEnvironment",
    "ClusterState",
    "ClusterUpgradeCadence",
    "ClusterVersionsEnvironment",
    "DurabilityLevel",
    "ManagedIdentityType",
    "MoveCost",
    "NotificationCategory",
    "NotificationChannel",
    "NotificationLevel",
    "PartitionScheme",
    "ProvisioningState",
    "ReliabilityLevel",
    "RollingUpgradeMode",
    "ServiceCorrelationScheme",
    "ServiceKind",
    "ServiceLoadMetricWeight",
    "ServicePlacementPolicyType",
    "SfZonalUpgradeMode",
    "StoreName",
    "UpgradeMode",
    "VmssZonalUpgradeMode",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
