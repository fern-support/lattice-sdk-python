# This file was auto-generated from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...types.agent_task_request import AgentTaskRequest
from ...types.heartbeat_object import HeartbeatObject


class StreamAsAgentResponse_Heartbeat(UniversalBaseModel):
    event: typing.Literal["heartbeat"] = "heartbeat"
    data: HeartbeatObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamAsAgentResponse_AgentRequest(UniversalBaseModel):
    event: typing.Literal["agent_request"] = "agent_request"
    data: AgentTaskRequest

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


StreamAsAgentResponse = typing_extensions.Annotated[
    typing.Union[StreamAsAgentResponse_Heartbeat, StreamAsAgentResponse_AgentRequest],
    pydantic.Field(discriminator="event"),
]
update_forward_refs(StreamAsAgentResponse_AgentRequest)
