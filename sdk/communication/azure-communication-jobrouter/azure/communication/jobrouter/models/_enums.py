# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class DistributionModeKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Discriminators for supported distribution mode types."""

    BEST_WORKER = "bestWorker"
    """Discriminator value for BestWorkerMode."""
    LONGEST_IDLE = "longestIdle"
    """Discriminator value for LongestIdleMode."""
    ROUND_ROBIN = "roundRobin"
    """Discriminator value for RoundRobinMode."""


class ExceptionActionKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Discriminators for supported exception action types."""

    CANCEL = "cancel"
    """Discriminator value for CancelExceptionAction."""
    MANUAL_RECLASSIFY = "manualReclassify"
    """Discriminator value for ManualReclassifyExceptionAction."""
    RECLASSIFY = "reclassify"
    """Discriminator value for ReclassifyExceptionAction."""


class ExceptionTriggerKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Discriminators for supported exception trigger types."""

    QUEUE_LENGTH = "queueLength"
    """Discriminator value for QueueLengthExceptionTrigger."""
    WAIT_TIME = "waitTime"
    """Discriminator value for WaitTimeExceptionTrigger."""


class ExpressionRouterRuleLanguage(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Available expression languages that can be configured."""

    POWER_FX = "powerFx"
    """PowerFx"""


class JobMatchingModeKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Discriminators for supported matching mode types."""

    QUEUE_AND_MATCH = "queueAndMatch"
    """Discriminator value for QueueAndMatchMode."""
    SCHEDULE_AND_SUSPEND = "scheduleAndSuspend"
    """Discriminator value for ScheduleAndSuspendMode."""
    SUSPEND = "suspend"
    """Discriminator value for SuspendMode."""


class LabelOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes supported operations on label values."""

    EQUAL = "equal"
    """Equal."""
    NOT_EQUAL = "notEqual"
    """Not Equal."""
    LESS_THAN = "lessThan"
    """Less than."""
    LESS_THAN_OR_EQUAL = "lessThanOrEqual"
    """Less than or equal."""
    GREATER_THAN = "greaterThan"
    """Greater than."""
    GREATER_THAN_OR_EQUAL = "greaterThanOrEqual"
    """Greater than or equal."""


class QueueSelectorAttachmentKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Discriminators for supported queue selector attachment types."""

    CONDITIONAL = "conditional"
    """Discriminator value for ConditionalQueueSelectorAttachment."""
    PASS_THROUGH = "passThrough"
    """Discriminator value for PassThroughQueueSelectorAttachment."""
    RULE_ENGINE = "ruleEngine"
    """Discriminator value for RuleEngineQueueSelectorAttachment."""
    STATIC = "static"
    """Discriminator value for StaticQueueSelectorAttachment."""
    WEIGHTED_ALLOCATION = "weightedAllocation"
    """Discriminator value for WeightedAllocationQueueSelectorAttachment."""


class RouterJobStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the various status of a job."""

    PENDING_CLASSIFICATION = "pendingClassification"
    """Job is waiting to be classified."""
    QUEUED = "queued"
    """Job has been queued."""
    ASSIGNED = "assigned"
    """Job has been assigned to a worker."""
    COMPLETED = "completed"
    """Job has been completed by a worker."""
    CLOSED = "closed"
    """Job has been closed by a worker."""
    CANCELLED = "cancelled"
    """Job has been cancelled."""
    CLASSIFICATION_FAILED = "classificationFailed"
    """Classification process failed for the job."""
    CREATED = "created"
    """Job has been created."""
    PENDING_SCHEDULE = "pendingSchedule"
    """Job has been created but not been scheduled yet."""
    SCHEDULED = "scheduled"
    """Job has been scheduled successfully."""
    SCHEDULE_FAILED = "scheduleFailed"
    """Job scheduling failed."""
    WAITING_FOR_ACTIVATION = "waitingForActivation"
    """Job is in a suspended state and waiting for an update."""


class RouterJobStatusSelector(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enums used to filters jobs by status."""

    ALL = "all"
    """Default"""
    PENDING_CLASSIFICATION = "pendingClassification"
    """Job is waiting to be classified."""
    QUEUED = "queued"
    """Job has been queued."""
    ASSIGNED = "assigned"
    """Job has been assigned to a worker."""
    COMPLETED = "completed"
    """Job has been completed by a worker."""
    CLOSED = "closed"
    """Job has been closed by a worker."""
    CANCELLED = "cancelled"
    """Job has been cancelled."""
    CLASSIFICATION_FAILED = "classificationFailed"
    """Classification process failed for the job."""
    CREATED = "created"
    """Job has been created."""
    PENDING_SCHEDULE = "pendingSchedule"
    """Job has been created but not been scheduled yet."""
    SCHEDULED = "scheduled"
    """Job has been scheduled successfully."""
    SCHEDULE_FAILED = "scheduleFailed"
    """Job scheduling failed."""
    WAITING_FOR_ACTIVATION = "waitingForActivation"
    """Job is in a suspended state and waiting for an update."""
    ACTIVE = "active"
    """Job is in a state of PendingClassification or Queued or Assigned or ClassificationFailed or
    #: Completed or PendingSchedule or Scheduled or ScheduleFailed or WaitingForActivation."""


class RouterRuleKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Discriminators for supported router rule types."""

    DIRECT_MAP = "directMap"
    """Discriminator value for DirectMapRouterRule."""
    EXPRESSION = "expression"
    """Discriminator value for ExpressionRouterRule."""
    FUNCTION = "function"
    """Discriminator value for FunctionRouterRule."""
    STATIC = "static"
    """Discriminator value for StaticRouterRule."""
    WEBHOOK = "webhook"
    """Discriminator value for WebhookRouterRule."""


class RouterWorkerSelectorStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the status of a worker selector."""

    ACTIVE = "active"
    """Worker selector is valid."""
    EXPIRED = "expired"
    """Worker selector is not valid."""


class RouterWorkerState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enums for worker states."""

    ACTIVE = "active"
    """Worker is active and available to take offers."""
    DRAINING = "draining"
    """Worker is not active, if there are existing offers they are being revoked. No new offers are
    #: sent."""
    INACTIVE = "inactive"
    """Worker is not active. No new offers are sent."""


class RouterWorkerStateSelector(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enums used to filters workers by state."""

    ACTIVE = "active"
    """Worker is active and available to take offers."""
    DRAINING = "draining"
    """Worker is not active, if there are existing offers they are being revoked. No new offers are
    #: sent."""
    INACTIVE = "inactive"
    """Worker is not active. No new offers are sent."""
    ALL = "all"
    """Worker is active or draining or inactive."""


class ScoringRuleParameterSelector(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Supported parameters for scoring workers used with BestWorkerMode."""

    JOB_LABELS = "jobLabels"
    """Parameter to add job labels to scoring payload.  Property is sent as ``job``."""
    WORKER_SELECTORS = "workerSelectors"
    """Parameter to add worker selectors from a job to scoring payload.  Property is sent as
    #: ``selectors``."""


class WorkerSelectorAttachmentKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Discriminators for supported worker selector attachment types."""

    CONDITIONAL = "conditional"
    """Discriminator value for ConditionalWorkerSelectorAttachment."""
    PASS_THROUGH = "passThrough"
    """Discriminator value for PassThroughWorkerSelectorAttachment."""
    RULE_ENGINE = "ruleEngine"
    """Discriminator value for RuleEngineWorkerSelectorAttachment."""
    STATIC = "static"
    """Discriminator value for StaticWorkerSelectorAttachment."""
    WEIGHTED_ALLOCATION = "weightedAllocation"
    """Discriminator value for WeightedAllocationWorkerSelectorAttachment."""
