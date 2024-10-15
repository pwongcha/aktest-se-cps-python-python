"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from aktest_se_cps_python.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from aktest_se_cps_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetEnrollmentChangeRequestTypedDict(TypedDict):
    change_id: int
    r"""The change for this enrollment on which to perform the desired operation."""
    enrollment_id: int
    r"""Enrollment on which to perform the desired operation."""
    account_switch_key: NotRequired[str]
    r"""For customers who manage more than one account, this [runs the operation from another account](https://techdocs.akamai.com/developer/docs/manage-many-accounts-with-one-api-client). The Identity and Access Management API provides a [list of available account switch keys](https://techdocs.akamai.com/iam-api/reference/get-client-account-switch-keys)."""


class GetEnrollmentChangeRequest(BaseModel):
    change_id: Annotated[
        int,
        pydantic.Field(alias="changeId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The change for this enrollment on which to perform the desired operation."""

    enrollment_id: Annotated[
        int,
        pydantic.Field(alias="enrollmentId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Enrollment on which to perform the desired operation."""

    account_switch_key: Annotated[
        Optional[str],
        pydantic.Field(alias="accountSwitchKey"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""For customers who manage more than one account, this [runs the operation from another account](https://techdocs.akamai.com/developer/docs/manage-many-accounts-with-one-api-client). The Identity and Access Management API provides a [list of available account switch keys](https://techdocs.akamai.com/iam-api/reference/get-client-account-switch-keys)."""


class AllowedInputTypedDict(TypedDict):
    info: str
    r"""The resource location for the allowed input's description."""
    required_to_proceed: bool
    r"""If `true`, this input is required for the change to proceed."""
    type: str
    r"""The type input. For more information, see the [Change input content type mapping](ref:change-input-content-type-mapping)."""
    update: str
    r"""The resource path location that you can use to make a call for this input."""


class AllowedInput(BaseModel):
    info: str
    r"""The resource location for the allowed input's description."""

    required_to_proceed: Annotated[bool, pydantic.Field(alias="requiredToProceed")]
    r"""If `true`, this input is required for the change to proceed."""

    type: str
    r"""The type input. For more information, see the [Change input content type mapping](ref:change-input-content-type-mapping)."""

    update: str
    r"""The resource path location that you can use to make a call for this input."""


class DeploymentScheduleTypedDict(TypedDict):
    r"""The schedule for when you want this change to deploy."""

    not_after: Nullable[str]
    r"""Don't deploy the certificate after this date."""
    not_before: Nullable[str]
    r"""Don't deploy the certificate before this date."""


class DeploymentSchedule(BaseModel):
    r"""The schedule for when you want this change to deploy."""

    not_after: Annotated[Nullable[str], pydantic.Field(alias="notAfter")]
    r"""Don't deploy the certificate after this date."""

    not_before: Annotated[Nullable[str], pydantic.Field(alias="notBefore")]
    r"""Don't deploy the certificate before this date."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["notAfter", "notBefore"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class ErrorTypedDict(TypedDict):
    r"""Error information for this change."""

    code: str
    r"""The unique identifier code for this error."""
    description: str
    r"""The detailed description for this error."""
    timestamp: str
    r"""Indicates when this error occurred."""


class Error(BaseModel):
    r"""Error information for this change."""

    code: str
    r"""The unique identifier code for this error."""

    description: str
    r"""The detailed description for this error."""

    timestamp: str
    r"""Indicates when this error occurred."""


class State(str, Enum):
    r"""The change request's state. A value of `new` means the certificate is processed but the renewal process is not started. A `running` value means CPS is preparing to send your certificate to Let's Encrypt. An `awaiting-input` value means the process is waiting on a user input, for example the approval or denial of a change management item. A `suspended` value indicates the process didn't complete. A value of `cancelled` means the process has been cancelled permanently, A `completed` value means the change request is finished. An `error` value means there's an issue with the domain."""

    NEW = "new"
    RUNNING = "running"
    AWAITING_INPUT = "awaiting-input"
    SUSPENDED = "suspended"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    ERROR = "error"


class StatusInfoTypedDict(TypedDict):
    r"""The status for this change at this time."""

    deployment_schedule: DeploymentScheduleTypedDict
    r"""The schedule for when you want this change to deploy."""
    description: str
    r"""A description of the change's current status."""
    state: State
    r"""The change request's state. A value of `new` means the certificate is processed but the renewal process is not started. A `running` value means CPS is preparing to send your certificate to Let's Encrypt. An `awaiting-input` value means the process is waiting on a user input, for example the approval or denial of a change management item. A `suspended` value indicates the process didn't complete. A value of `cancelled` means the process has been cancelled permanently, A `completed` value means the change request is finished. An `error` value means there's an issue with the domain."""
    status: str
    r"""The general status of the change. This is a high level of description of the status for the change. See [Status values and descriptions](ref:status-values-and-descriptions) for the list of possible status values this operation may return."""
    error: NotRequired[Nullable[ErrorTypedDict]]
    r"""Error information for this change."""


class StatusInfo(BaseModel):
    r"""The status for this change at this time."""

    deployment_schedule: Annotated[
        DeploymentSchedule, pydantic.Field(alias="deploymentSchedule")
    ]
    r"""The schedule for when you want this change to deploy."""

    description: str
    r"""A description of the change's current status."""

    state: State
    r"""The change request's state. A value of `new` means the certificate is processed but the renewal process is not started. A `running` value means CPS is preparing to send your certificate to Let's Encrypt. An `awaiting-input` value means the process is waiting on a user input, for example the approval or denial of a change management item. A `suspended` value indicates the process didn't complete. A value of `cancelled` means the process has been cancelled permanently, A `completed` value means the change request is finished. An `error` value means there's an issue with the domain."""

    status: str
    r"""The general status of the change. This is a high level of description of the status for the change. See [Status values and descriptions](ref:status-values-and-descriptions) for the list of possible status values this operation may return."""

    error: OptionalNullable[Error] = UNSET
    r"""Error information for this change."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["error"]
        nullable_fields = ["error"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class GetEnrollmentChangeResponseBodyTypedDict(TypedDict):
    r"""Any change that you want to make to the network deployment of an enrollment."""

    allowed_input: List[AllowedInputTypedDict]
    r"""The resource path locations of data inputs allowed by this change. These could be required or optional for this change to proceed."""
    status_info: StatusInfoTypedDict
    r"""The status for this change at this time."""


class GetEnrollmentChangeResponseBody(BaseModel):
    r"""Any change that you want to make to the network deployment of an enrollment."""

    allowed_input: Annotated[List[AllowedInput], pydantic.Field(alias="allowedInput")]
    r"""The resource path locations of data inputs allowed by this change. These could be required or optional for this change to proceed."""

    status_info: Annotated[StatusInfo, pydantic.Field(alias="statusInfo")]
    r"""The status for this change at this time."""
