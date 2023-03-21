# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(scope: str, assessment_name: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-01-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-01-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/{scope}/providers/Microsoft.Security/assessments/{assessmentName}/governanceAssignments"
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str"),
        "assessmentName": _SERIALIZER.url("assessment_name", assessment_name, "str", pattern=r"^[-\w\._\(\)]+$"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(scope: str, assessment_name: str, assignment_key: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-01-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-01-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/{scope}/providers/Microsoft.Security/assessments/{assessmentName}/governanceAssignments/{assignmentKey}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str"),
        "assessmentName": _SERIALIZER.url("assessment_name", assessment_name, "str", pattern=r"^[-\w\._\(\)]+$"),
        "assignmentKey": _SERIALIZER.url("assignment_key", assignment_key, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_request(scope: str, assessment_name: str, assignment_key: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-01-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-01-01-preview")
    )
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/{scope}/providers/Microsoft.Security/assessments/{assessmentName}/governanceAssignments/{assignmentKey}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str"),
        "assessmentName": _SERIALIZER.url("assessment_name", assessment_name, "str", pattern=r"^[-\w\._\(\)]+$"),
        "assignmentKey": _SERIALIZER.url("assignment_key", assignment_key, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(scope: str, assessment_name: str, assignment_key: str, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-01-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-01-01-preview")
    )
    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/{scope}/providers/Microsoft.Security/assessments/{assessmentName}/governanceAssignments/{assignmentKey}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str"),
        "assessmentName": _SERIALIZER.url("assessment_name", assessment_name, "str", pattern=r"^[-\w\._\(\)]+$"),
        "assignmentKey": _SERIALIZER.url("assignment_key", assignment_key, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


class GovernanceAssignmentsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2022_01_01_preview.SecurityCenter`'s
        :attr:`governance_assignments` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(self, scope: str, assessment_name: str, **kwargs: Any) -> Iterable["_models.GovernanceAssignment"]:
        """Get governance assignments on all of your resources inside a scope.

        :param scope: The scope of the Governance assignments. Valid scopes are: subscription (format:
         'subscriptions/{subscriptionId}'), or security connector (format:
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName})'.
         Required.
        :type scope: str
        :param assessment_name: The Assessment Key - A unique key for the assessment type. Required.
        :type assessment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either GovernanceAssignment or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.security.v2022_01_01_preview.models.GovernanceAssignment]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-01-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2022-01-01-preview")
        )
        cls: ClsType[_models.GovernanceAssignmentsList] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    scope=scope,
                    assessment_name=assessment_name,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("GovernanceAssignmentsList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {"url": "/{scope}/providers/Microsoft.Security/assessments/{assessmentName}/governanceAssignments"}

    @distributed_trace
    def get(self, scope: str, assessment_name: str, assignment_key: str, **kwargs: Any) -> _models.GovernanceAssignment:
        """Get a specific governanceAssignment for the requested scope by AssignmentKey.

        :param scope: The scope of the Governance assignments. Valid scopes are: subscription (format:
         'subscriptions/{subscriptionId}'), or security connector (format:
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName})'.
         Required.
        :type scope: str
        :param assessment_name: The Assessment Key - A unique key for the assessment type. Required.
        :type assessment_name: str
        :param assignment_key: The governance assignment key - the assessment key of the required
         governance assignment. Required.
        :type assignment_key: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GovernanceAssignment or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2022_01_01_preview.models.GovernanceAssignment
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-01-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2022-01-01-preview")
        )
        cls: ClsType[_models.GovernanceAssignment] = kwargs.pop("cls", None)

        request = build_get_request(
            scope=scope,
            assessment_name=assessment_name,
            assignment_key=assignment_key,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("GovernanceAssignment", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/{scope}/providers/Microsoft.Security/assessments/{assessmentName}/governanceAssignments/{assignmentKey}"
    }

    @overload
    def create_or_update(
        self,
        scope: str,
        assessment_name: str,
        assignment_key: str,
        governance_assignment: _models.GovernanceAssignment,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.GovernanceAssignment:
        """Creates or updates a governance assignment on the given subscription.

        :param scope: The scope of the Governance assignments. Valid scopes are: subscription (format:
         'subscriptions/{subscriptionId}'), or security connector (format:
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName})'.
         Required.
        :type scope: str
        :param assessment_name: The Assessment Key - A unique key for the assessment type. Required.
        :type assessment_name: str
        :param assignment_key: The governance assignment key - the assessment key of the required
         governance assignment. Required.
        :type assignment_key: str
        :param governance_assignment: Governance assignment over a subscription scope. Required.
        :type governance_assignment:
         ~azure.mgmt.security.v2022_01_01_preview.models.GovernanceAssignment
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GovernanceAssignment or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2022_01_01_preview.models.GovernanceAssignment
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        scope: str,
        assessment_name: str,
        assignment_key: str,
        governance_assignment: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.GovernanceAssignment:
        """Creates or updates a governance assignment on the given subscription.

        :param scope: The scope of the Governance assignments. Valid scopes are: subscription (format:
         'subscriptions/{subscriptionId}'), or security connector (format:
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName})'.
         Required.
        :type scope: str
        :param assessment_name: The Assessment Key - A unique key for the assessment type. Required.
        :type assessment_name: str
        :param assignment_key: The governance assignment key - the assessment key of the required
         governance assignment. Required.
        :type assignment_key: str
        :param governance_assignment: Governance assignment over a subscription scope. Required.
        :type governance_assignment: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GovernanceAssignment or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2022_01_01_preview.models.GovernanceAssignment
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        scope: str,
        assessment_name: str,
        assignment_key: str,
        governance_assignment: Union[_models.GovernanceAssignment, IO],
        **kwargs: Any
    ) -> _models.GovernanceAssignment:
        """Creates or updates a governance assignment on the given subscription.

        :param scope: The scope of the Governance assignments. Valid scopes are: subscription (format:
         'subscriptions/{subscriptionId}'), or security connector (format:
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName})'.
         Required.
        :type scope: str
        :param assessment_name: The Assessment Key - A unique key for the assessment type. Required.
        :type assessment_name: str
        :param assignment_key: The governance assignment key - the assessment key of the required
         governance assignment. Required.
        :type assignment_key: str
        :param governance_assignment: Governance assignment over a subscription scope. Is either a
         GovernanceAssignment type or a IO type. Required.
        :type governance_assignment:
         ~azure.mgmt.security.v2022_01_01_preview.models.GovernanceAssignment or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GovernanceAssignment or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2022_01_01_preview.models.GovernanceAssignment
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-01-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2022-01-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.GovernanceAssignment] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(governance_assignment, (IO, bytes)):
            _content = governance_assignment
        else:
            _json = self._serialize.body(governance_assignment, "GovernanceAssignment")

        request = build_create_or_update_request(
            scope=scope,
            assessment_name=assessment_name,
            assignment_key=assignment_key,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("GovernanceAssignment", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("GovernanceAssignment", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    create_or_update.metadata = {
        "url": "/{scope}/providers/Microsoft.Security/assessments/{assessmentName}/governanceAssignments/{assignmentKey}"
    }

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, scope: str, assessment_name: str, assignment_key: str, **kwargs: Any
    ) -> None:
        """Delete a GovernanceAssignment over a given scope.

        :param scope: The scope of the Governance assignments. Valid scopes are: subscription (format:
         'subscriptions/{subscriptionId}'), or security connector (format:
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName})'.
         Required.
        :type scope: str
        :param assessment_name: The Assessment Key - A unique key for the assessment type. Required.
        :type assessment_name: str
        :param assignment_key: The governance assignment key - the assessment key of the required
         governance assignment. Required.
        :type assignment_key: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-01-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2022-01-01-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            scope=scope,
            assessment_name=assessment_name,
            assignment_key=assignment_key,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/{scope}/providers/Microsoft.Security/assessments/{assessmentName}/governanceAssignments/{assignmentKey}"
    }
