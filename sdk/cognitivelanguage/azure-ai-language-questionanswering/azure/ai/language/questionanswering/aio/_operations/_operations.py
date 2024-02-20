# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._operations._operations import (
    build_question_answering_get_answers_from_text_request,
    build_question_answering_get_answers_request,
)
from .._vendor import QuestionAnsweringClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class QuestionAnsweringClientOperationsMixin(QuestionAnsweringClientMixinABC):
    @overload
    async def get_answers(
        self,
        options: _models.AnswersOptions,
        *,
        project_name: str,
        deployment_name: str,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AnswersResult:
        """Answers the specified question using your knowledge base.

        Answers the specified question using your knowledge base.

        :param options: Post body of the request. Required.
        :type options: ~azure.ai.language.questionanswering.models.AnswersOptions
        :keyword project_name: The name of the project to use. Required.
        :paramtype project_name: str
        :keyword deployment_name: The name of the specific deployment of the project to use. Required.
        :paramtype deployment_name: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: AnswersResult
        :rtype: ~azure.ai.language.questionanswering.models.AnswersResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def get_answers(
        self,
        options: IO[bytes],
        *,
        project_name: str,
        deployment_name: str,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AnswersResult:
        """Answers the specified question using your knowledge base.

        Answers the specified question using your knowledge base.

        :param options: Post body of the request. Required.
        :type options: IO[bytes]
        :keyword project_name: The name of the project to use. Required.
        :paramtype project_name: str
        :keyword deployment_name: The name of the specific deployment of the project to use. Required.
        :paramtype deployment_name: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: AnswersResult
        :rtype: ~azure.ai.language.questionanswering.models.AnswersResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def get_answers(
        self,
        options: Union[_models.AnswersOptions, IO[bytes]],
        *,
        project_name: str,
        deployment_name: str,
        **kwargs: Any
    ) -> _models.AnswersResult:
        """Answers the specified question using your knowledge base.

        Answers the specified question using your knowledge base.

        :param options: Post body of the request. Is either a AnswersOptions type or a IO[bytes] type.
         Required.
        :type options: ~azure.ai.language.questionanswering.models.AnswersOptions or IO[bytes]
        :keyword project_name: The name of the project to use. Required.
        :paramtype project_name: str
        :keyword deployment_name: The name of the specific deployment of the project to use. Required.
        :paramtype deployment_name: str
        :return: AnswersResult
        :rtype: ~azure.ai.language.questionanswering.models.AnswersResult
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
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AnswersResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(options, (IOBase, bytes)):
            _content = options
        else:
            _json = self._serialize.body(options, "AnswersOptions")

        _request = build_question_answering_get_answers_request(
            project_name=project_name,
            deployment_name=deployment_name,
            content_type=content_type,
            api_version=self._config.api_version,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("AnswersResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def get_answers_from_text(
        self, options: _models.AnswersFromTextOptions, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.AnswersFromTextResult:
        """Answers the specified question using the provided text in the body.

        Answers the specified question using the provided text in the body.

        :param options: Post body of the request. Required.
        :type options: ~azure.ai.language.questionanswering.models.AnswersFromTextOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: AnswersFromTextResult
        :rtype: ~azure.ai.language.questionanswering.models.AnswersFromTextResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def get_answers_from_text(
        self, options: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.AnswersFromTextResult:
        """Answers the specified question using the provided text in the body.

        Answers the specified question using the provided text in the body.

        :param options: Post body of the request. Required.
        :type options: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: AnswersFromTextResult
        :rtype: ~azure.ai.language.questionanswering.models.AnswersFromTextResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def get_answers_from_text(
        self, options: Union[_models.AnswersFromTextOptions, IO[bytes]], **kwargs: Any
    ) -> _models.AnswersFromTextResult:
        """Answers the specified question using the provided text in the body.

        Answers the specified question using the provided text in the body.

        :param options: Post body of the request. Is either a AnswersFromTextOptions type or a
         IO[bytes] type. Required.
        :type options: ~azure.ai.language.questionanswering.models.AnswersFromTextOptions or IO[bytes]
        :return: AnswersFromTextResult
        :rtype: ~azure.ai.language.questionanswering.models.AnswersFromTextResult
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
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AnswersFromTextResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(options, (IOBase, bytes)):
            _content = options
        else:
            _json = self._serialize.body(options, "AnswersFromTextOptions")

        _request = build_question_answering_get_answers_from_text_request(
            content_type=content_type,
            api_version=self._config.api_version,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("AnswersFromTextResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
