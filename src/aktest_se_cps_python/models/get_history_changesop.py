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
from datetime import datetime
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetHistoryChangesRequestTypedDict(TypedDict):
    enrollment_id: int
    r"""Enrollment on which to perform the desired operation."""
    include_all: NotRequired[bool]
    r"""Retrieve all changes or certificates."""
    account_switch_key: NotRequired[str]
    r"""For customers who manage more than one account, this [runs the operation from another account](https://techdocs.akamai.com/developer/docs/manage-many-accounts-with-one-api-client). The Identity and Access Management API provides a [list of available account switch keys](https://techdocs.akamai.com/iam-api/reference/get-client-account-switch-keys)."""


class GetHistoryChangesRequest(BaseModel):
    enrollment_id: Annotated[
        int,
        pydantic.Field(alias="enrollmentId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Enrollment on which to perform the desired operation."""

    include_all: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeAll"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Retrieve all changes or certificates."""

    account_switch_key: Annotated[
        Optional[str],
        pydantic.Field(alias="accountSwitchKey"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""For customers who manage more than one account, this [runs the operation from another account](https://techdocs.akamai.com/developer/docs/manage-many-accounts-with-one-api-client). The Identity and Access Management API provides a [list of available account switch keys](https://techdocs.akamai.com/iam-api/reference/get-client-account-switch-keys)."""


class Action(str, Enum):
    r"""Show every change on the certificate. The possible changes are `import-certificate`, `renew`, `new-certificate`, `modify-san`, `update-network-configuration`."""

    IMPORT_CERTIFICATE = "import-certificate"
    RENEW = "renew"
    NEW_CERTIFICATE = "new-certificate"
    MODIFY_SAN = "modify-san"
    UPDATE_NETWORK_CONFIGURATION = "update-network-configuration"


class GetHistoryChangesMultiStackedCertificatesTypedDict(TypedDict):
    certificate: Nullable[str]
    r"""Certificate text."""
    csr: str
    r"""Certificate CSR."""
    key_algorithm: str
    r"""Key algorithm of the certificate."""
    trust_chain: Nullable[str]
    r"""Certificate trust chain."""


class GetHistoryChangesMultiStackedCertificates(BaseModel):
    certificate: Nullable[str]
    r"""Certificate text."""

    csr: str
    r"""Certificate CSR."""

    key_algorithm: Annotated[str, pydantic.Field(alias="keyAlgorithm")]
    r"""Key algorithm of the certificate."""

    trust_chain: Annotated[Nullable[str], pydantic.Field(alias="trustChain")]
    r"""Certificate trust chain."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["certificate", "trustChain"]
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


class GetHistoryChangesPrimaryCertificateTypedDict(TypedDict):
    r"""Primary Certificate."""

    certificate: Nullable[str]
    r"""Certificate text."""
    csr: str
    r"""Certificate CSR."""
    key_algorithm: str
    r"""Key algorithm of the certificate."""
    trust_chain: Nullable[str]
    r"""Certificate trust chain."""


class GetHistoryChangesPrimaryCertificate(BaseModel):
    r"""Primary Certificate."""

    certificate: Nullable[str]
    r"""Certificate text."""

    csr: str
    r"""Certificate CSR."""

    key_algorithm: Annotated[str, pydantic.Field(alias="keyAlgorithm")]
    r"""Key algorithm of the certificate."""

    trust_chain: Annotated[Nullable[str], pydantic.Field(alias="trustChain")]
    r"""Certificate trust chain."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["certificate", "trustChain"]
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


class PrimaryCertificateOrderDetailsTypedDict(TypedDict):
    r"""CA order details for this Change."""

    order_id: str
    r"""Order ID."""


class PrimaryCertificateOrderDetails(BaseModel):
    r"""CA order details for this Change."""

    order_id: Annotated[str, pydantic.Field(alias="orderId")]
    r"""Order ID."""


class Status(str, Enum):
    r"""The status of the change. The possible changes are `incomplete`, `cancelled`, `completed`."""

    INCOMPLETE = "incomplete"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class GetHistoryChangesChangesTypedDict(TypedDict):
    action: Action
    r"""Show every change on the certificate. The possible changes are `import-certificate`, `renew`, `new-certificate`, `modify-san`, `update-network-configuration`."""
    action_description: str
    r"""A description of each change."""
    created_by: str
    r"""The username of the user who initiated the change."""
    created_on: datetime
    r"""A date and timestamp when the change started."""
    multi_stacked_certificates: List[GetHistoryChangesMultiStackedCertificatesTypedDict]
    r"""Dual-stacked certificates."""
    ra: str
    r"""The certificate authority that issued the certificate."""
    status: Status
    r"""The status of the change. The possible changes are `incomplete`, `cancelled`, `completed`."""
    business_case_id: NotRequired[Nullable[str]]
    r"""The company name appears to be **Salesforce**."""
    last_updated: NotRequired[Nullable[str]]
    r"""A date and timestamp when the change was last updated."""
    primary_certificate: NotRequired[
        Nullable[GetHistoryChangesPrimaryCertificateTypedDict]
    ]
    r"""Primary Certificate."""
    primary_certificate_order_details: NotRequired[
        Nullable[PrimaryCertificateOrderDetailsTypedDict]
    ]
    r"""CA order details for this Change."""


class GetHistoryChangesChanges(BaseModel):
    action: Action
    r"""Show every change on the certificate. The possible changes are `import-certificate`, `renew`, `new-certificate`, `modify-san`, `update-network-configuration`."""

    action_description: Annotated[str, pydantic.Field(alias="actionDescription")]
    r"""A description of each change."""

    created_by: Annotated[str, pydantic.Field(alias="createdBy")]
    r"""The username of the user who initiated the change."""

    created_on: Annotated[datetime, pydantic.Field(alias="createdOn")]
    r"""A date and timestamp when the change started."""

    multi_stacked_certificates: Annotated[
        List[GetHistoryChangesMultiStackedCertificates],
        pydantic.Field(alias="multiStackedCertificates"),
    ]
    r"""Dual-stacked certificates."""

    ra: str
    r"""The certificate authority that issued the certificate."""

    status: Status
    r"""The status of the change. The possible changes are `incomplete`, `cancelled`, `completed`."""

    business_case_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="businessCaseId")
    ] = UNSET
    r"""The company name appears to be **Salesforce**."""

    last_updated: Annotated[
        OptionalNullable[str], pydantic.Field(alias="lastUpdated")
    ] = UNSET
    r"""A date and timestamp when the change was last updated."""

    primary_certificate: Annotated[
        OptionalNullable[GetHistoryChangesPrimaryCertificate],
        pydantic.Field(alias="primaryCertificate"),
    ] = UNSET
    r"""Primary Certificate."""

    primary_certificate_order_details: Annotated[
        OptionalNullable[PrimaryCertificateOrderDetails],
        pydantic.Field(alias="primaryCertificateOrderDetails"),
    ] = UNSET
    r"""CA order details for this Change."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "businessCaseId",
            "lastUpdated",
            "primaryCertificate",
            "primaryCertificateOrderDetails",
        ]
        nullable_fields = [
            "businessCaseId",
            "lastUpdated",
            "primaryCertificate",
            "primaryCertificateOrderDetails",
        ]
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


class GetHistoryChangesResponseBodyTypedDict(TypedDict):
    r"""The change history includes all changes to a certificate. This is the equivalent of viewing the certificate activity in the CPS UI. You can view each change to your certificate, the status of your change, the last updated date, the date the change was created, and who created the change. You can also take actions on each change of the certificate, including viewing the CSR for the certificate, viewing the certificate, and viewing the trust chain for the certificate."""

    changes: List[GetHistoryChangesChangesTypedDict]
    r"""Change history items."""


class GetHistoryChangesResponseBody(BaseModel):
    r"""The change history includes all changes to a certificate. This is the equivalent of viewing the certificate activity in the CPS UI. You can view each change to your certificate, the status of your change, the last updated date, the date the change was created, and who created the change. You can also take actions on each change of the certificate, including viewing the CSR for the certificate, viewing the certificate, and viewing the trust chain for the certificate."""

    changes: List[GetHistoryChangesChanges]
    r"""Change history items."""
