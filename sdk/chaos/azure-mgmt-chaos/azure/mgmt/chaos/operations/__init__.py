# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._capabilities_operations import CapabilitiesOperations
from ._capability_types_operations import CapabilityTypesOperations
from ._experiments_operations import ExperimentsOperations
from ._operation_statuses_operations import OperationStatusesOperations
from ._operations import Operations
from ._target_types_operations import TargetTypesOperations
from ._targets_operations import TargetsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CapabilitiesOperations",
    "CapabilityTypesOperations",
    "ExperimentsOperations",
    "OperationStatusesOperations",
    "Operations",
    "TargetTypesOperations",
    "TargetsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
