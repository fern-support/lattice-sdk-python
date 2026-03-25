# This file was auto-generated from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...types.entity_event import EntityEvent
from ...types.heartbeat_object import HeartbeatObject


class StreamEntitiesResponse_Heartbeat(UniversalBaseModel):
    event: typing.Literal["heartbeat"] = "heartbeat"
    data: HeartbeatObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamEntitiesResponse_Entity(UniversalBaseModel):
    event: typing.Literal["entity"] = "entity"
    data: EntityEvent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


StreamEntitiesResponse = typing_extensions.Annotated[
    typing.Union[StreamEntitiesResponse_Heartbeat, StreamEntitiesResponse_Entity], pydantic.Field(discriminator="event")
]
update_forward_refs(StreamEntitiesResponse_Entity)
