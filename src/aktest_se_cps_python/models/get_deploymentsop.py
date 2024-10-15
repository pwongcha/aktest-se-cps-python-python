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


class GetDeploymentsRequestTypedDict(TypedDict):
    enrollment_id: int
    r"""Enrollment on which to perform the desired operation."""
    account_switch_key: NotRequired[str]
    r"""For customers who manage more than one account, this [runs the operation from another account](https://techdocs.akamai.com/developer/docs/manage-many-accounts-with-one-api-client). The Identity and Access Management API provides a [list of available account switch keys](https://techdocs.akamai.com/iam-api/reference/get-client-account-switch-keys)."""


class GetDeploymentsRequest(BaseModel):
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


class GetDeploymentsKeyAlgorithm(str, Enum):
    r"""The key algorithm for the multi-stacked certificate. This is either `ECDSA` or `RSA`."""

    ECDSA = "ECDSA"
    RSA = "RSA"


class GetDeploymentsSignatureAlgorithm(str, Enum):
    r"""Indicates the SHA (Secure Hash Algorithm) function. You can use either `SHA-1` for a 160-bit (20-byte) hash or `SHA-256` for a 256-bit (32-byte) hash."""

    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"


class GetDeploymentsMultiStackedCertificatesTypedDict(TypedDict):
    certificate: Nullable[str]
    r"""The certificate text."""
    trust_chain: Nullable[str]
    r"""The trust chain for the certificate."""
    expiry: NotRequired[str]
    r"""The expiration date for the certificate."""
    key_algorithm: NotRequired[GetDeploymentsKeyAlgorithm]
    r"""The key algorithm for the multi-stacked certificate. This is either `ECDSA` or `RSA`."""
    signature_algorithm: NotRequired[Nullable[GetDeploymentsSignatureAlgorithm]]
    r"""Indicates the SHA (Secure Hash Algorithm) function. You can use either `SHA-1` for a 160-bit (20-byte) hash or `SHA-256` for a 256-bit (32-byte) hash."""


class GetDeploymentsMultiStackedCertificates(BaseModel):
    certificate: Nullable[str]
    r"""The certificate text."""

    trust_chain: Annotated[Nullable[str], pydantic.Field(alias="trustChain")]
    r"""The trust chain for the certificate."""

    expiry: Optional[str] = None
    r"""The expiration date for the certificate."""

    key_algorithm: Annotated[
        Optional[GetDeploymentsKeyAlgorithm], pydantic.Field(alias="keyAlgorithm")
    ] = None
    r"""The key algorithm for the multi-stacked certificate. This is either `ECDSA` or `RSA`."""

    signature_algorithm: Annotated[
        OptionalNullable[GetDeploymentsSignatureAlgorithm],
        pydantic.Field(alias="signatureAlgorithm"),
    ] = UNSET
    r"""Indicates the SHA (Secure Hash Algorithm) function. You can use either `SHA-1` for a 160-bit (20-byte) hash or `SHA-256` for a 256-bit (32-byte) hash."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["expiry", "keyAlgorithm", "signatureAlgorithm"]
        nullable_fields = ["certificate", "trustChain", "signatureAlgorithm"]
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


class GetDeploymentsGeography(str, Enum):
    r"""Specifies the type of network where you want to deploy your certificate.  Use `core` to deploy across most of the world except for specially licensed areas.  Use `china+core` to include China, or `russia+core` to include Russia. Any non-`core` deployment needs to be enabled on your contract based on approval from the Chinese or Russian governments."""

    CORE = "core"
    CHINA_PLUS_CORE = "china+core"
    RUSSIA_PLUS_CORE = "russia+core"


class GetDeploymentsOcspStapling(str, Enum):
    r"""Indicates the OCSP stapling setting for the deployment. Use `on` to enable OCSP stapling, `off` to disable it, or `not-set` to ignore it."""

    ON = "on"
    OFF = "off"
    NOT_SET = "not-set"


class GetDeploymentsSecureNetwork(str, Enum):
    r"""Identifies the type of deployment network. An `enhanced-tls` value means Akamai's more secure network with PCI compliance capability, while `standard-tls` means Akamai's standard secure network."""

    ENHANCED_TLS = "enhanced-tls"
    STANDARD_TLS = "standard-tls"


class GetDeploymentsNetworkConfigurationTypedDict(TypedDict):
    r"""Your certificate's deployment configuration settings on production."""

    quic_enabled: bool
    r"""QUIC transport layer network protocol."""
    sni_only: bool
    r"""Server Name Indication (SNI) is an extension of the Transport Layer Security (TLS) networking protocol. It allows a server to present many certificates on the same IP address. All modern web browsers support the SNI extension. If you have the same SAN on two or more certificates with the SNI-only option set, Akamai may serve traffic using any certificate that matches the requested SNI hostname. You should avoid any certificates with overlapping SAN names when using SNI-only."""
    disallowed_tls_versions: NotRequired[List[str]]
    r"""Disallowed TLS protocols."""
    dns_names: NotRequired[List[str]]
    r"""Names served by SNI-only enabled enrollments."""
    fips_mode: NotRequired[bool]
    r"""Enables Federal Information Processing Standards (FIPS) for the enrollment."""
    geography: NotRequired[GetDeploymentsGeography]
    r"""Specifies the type of network where you want to deploy your certificate.  Use `core` to deploy across most of the world except for specially licensed areas.  Use `china+core` to include China, or `russia+core` to include Russia. Any non-`core` deployment needs to be enabled on your contract based on approval from the Chinese or Russian governments."""
    must_have_ciphers: NotRequired[str]
    r"""Ciphers that you definitely want to include for your enrollment while deploying it on the network."""
    ocsp_stapling: NotRequired[GetDeploymentsOcspStapling]
    r"""Indicates the OCSP stapling setting for the deployment. Use `on` to enable OCSP stapling, `off` to disable it, or `not-set` to ignore it."""
    preferred_ciphers: NotRequired[str]
    r"""Ciphers that you preferably want to include for your enrollment while deploying it on the network."""
    secure_network: NotRequired[GetDeploymentsSecureNetwork]
    r"""Identifies the type of deployment network. An `enhanced-tls` value means Akamai's more secure network with PCI compliance capability, while `standard-tls` means Akamai's standard secure network."""


class GetDeploymentsNetworkConfiguration(BaseModel):
    r"""Your certificate's deployment configuration settings on production."""

    quic_enabled: Annotated[bool, pydantic.Field(alias="quicEnabled")]
    r"""QUIC transport layer network protocol."""

    sni_only: Annotated[bool, pydantic.Field(alias="sniOnly")]
    r"""Server Name Indication (SNI) is an extension of the Transport Layer Security (TLS) networking protocol. It allows a server to present many certificates on the same IP address. All modern web browsers support the SNI extension. If you have the same SAN on two or more certificates with the SNI-only option set, Akamai may serve traffic using any certificate that matches the requested SNI hostname. You should avoid any certificates with overlapping SAN names when using SNI-only."""

    disallowed_tls_versions: Annotated[
        Optional[List[str]], pydantic.Field(alias="disallowedTlsVersions")
    ] = None
    r"""Disallowed TLS protocols."""

    dns_names: Annotated[Optional[List[str]], pydantic.Field(alias="dnsNames")] = None
    r"""Names served by SNI-only enabled enrollments."""

    fips_mode: Annotated[Optional[bool], pydantic.Field(alias="fipsMode")] = None
    r"""Enables Federal Information Processing Standards (FIPS) for the enrollment."""

    geography: Optional[GetDeploymentsGeography] = None
    r"""Specifies the type of network where you want to deploy your certificate.  Use `core` to deploy across most of the world except for specially licensed areas.  Use `china+core` to include China, or `russia+core` to include Russia. Any non-`core` deployment needs to be enabled on your contract based on approval from the Chinese or Russian governments."""

    must_have_ciphers: Annotated[
        Optional[str], pydantic.Field(alias="mustHaveCiphers")
    ] = None
    r"""Ciphers that you definitely want to include for your enrollment while deploying it on the network."""

    ocsp_stapling: Annotated[
        Optional[GetDeploymentsOcspStapling], pydantic.Field(alias="ocspStapling")
    ] = None
    r"""Indicates the OCSP stapling setting for the deployment. Use `on` to enable OCSP stapling, `off` to disable it, or `not-set` to ignore it."""

    preferred_ciphers: Annotated[
        Optional[str], pydantic.Field(alias="preferredCiphers")
    ] = None
    r"""Ciphers that you preferably want to include for your enrollment while deploying it on the network."""

    secure_network: Annotated[
        Optional[GetDeploymentsSecureNetwork], pydantic.Field(alias="secureNetwork")
    ] = None
    r"""Identifies the type of deployment network. An `enhanced-tls` value means Akamai's more secure network with PCI compliance capability, while `standard-tls` means Akamai's standard secure network."""


class GetDeploymentsDeploymentsKeyAlgorithm(str, Enum):
    r"""The key algorithm for the multi-stacked certificate. This is either `ECDSA` or `RSA`."""

    ECDSA = "ECDSA"
    RSA = "RSA"


class GetDeploymentsDeploymentsSignatureAlgorithm(str, Enum):
    r"""Indicates the SHA (Secure Hash Algorithm) function. You can use either `SHA-1` for a 160-bit (20-byte) hash or `SHA-256` for a 256-bit (32-byte) hash."""

    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"


class GetDeploymentsPrimaryCertificateTypedDict(TypedDict):
    r"""Primary certificate of the enrollment."""

    certificate: Nullable[str]
    r"""The certificate text."""
    trust_chain: Nullable[str]
    r"""The trust chain for the certificate."""
    expiry: NotRequired[str]
    r"""The expiration date for the certificate."""
    key_algorithm: NotRequired[GetDeploymentsDeploymentsKeyAlgorithm]
    r"""The key algorithm for the multi-stacked certificate. This is either `ECDSA` or `RSA`."""
    signature_algorithm: NotRequired[
        Nullable[GetDeploymentsDeploymentsSignatureAlgorithm]
    ]
    r"""Indicates the SHA (Secure Hash Algorithm) function. You can use either `SHA-1` for a 160-bit (20-byte) hash or `SHA-256` for a 256-bit (32-byte) hash."""


class GetDeploymentsPrimaryCertificate(BaseModel):
    r"""Primary certificate of the enrollment."""

    certificate: Nullable[str]
    r"""The certificate text."""

    trust_chain: Annotated[Nullable[str], pydantic.Field(alias="trustChain")]
    r"""The trust chain for the certificate."""

    expiry: Optional[str] = None
    r"""The expiration date for the certificate."""

    key_algorithm: Annotated[
        Optional[GetDeploymentsDeploymentsKeyAlgorithm],
        pydantic.Field(alias="keyAlgorithm"),
    ] = None
    r"""The key algorithm for the multi-stacked certificate. This is either `ECDSA` or `RSA`."""

    signature_algorithm: Annotated[
        OptionalNullable[GetDeploymentsDeploymentsSignatureAlgorithm],
        pydantic.Field(alias="signatureAlgorithm"),
    ] = UNSET
    r"""Indicates the SHA (Secure Hash Algorithm) function. You can use either `SHA-1` for a 160-bit (20-byte) hash or `SHA-256` for a 256-bit (32-byte) hash."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["expiry", "keyAlgorithm", "signatureAlgorithm"]
        nullable_fields = ["certificate", "trustChain", "signatureAlgorithm"]
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


class ProductionTypedDict(TypedDict):
    r"""Encapsulates information about your certificate's deployment on the production network."""

    multi_stacked_certificates: List[GetDeploymentsMultiStackedCertificatesTypedDict]
    r"""Dual-stacked certificates include an ECDSA certificate in addition to an RSA certificate."""
    network_configuration: GetDeploymentsNetworkConfigurationTypedDict
    r"""Your certificate's deployment configuration settings on production."""
    primary_certificate: Nullable[GetDeploymentsPrimaryCertificateTypedDict]
    r"""Primary certificate of the enrollment."""
    ocsp_stapled: NotRequired[bool]
    r"""OCSP Stapling improves performance by including a valid OCSP response in every TLS handshake. We recommend all customers enable this feature."""
    ocsp_uris: NotRequired[Nullable[List[str]]]
    r"""URI used for OCSP stapling validation."""


class Production(BaseModel):
    r"""Encapsulates information about your certificate's deployment on the production network."""

    multi_stacked_certificates: Annotated[
        List[GetDeploymentsMultiStackedCertificates],
        pydantic.Field(alias="multiStackedCertificates"),
    ]
    r"""Dual-stacked certificates include an ECDSA certificate in addition to an RSA certificate."""

    network_configuration: Annotated[
        GetDeploymentsNetworkConfiguration, pydantic.Field(alias="networkConfiguration")
    ]
    r"""Your certificate's deployment configuration settings on production."""

    primary_certificate: Annotated[
        Nullable[GetDeploymentsPrimaryCertificate],
        pydantic.Field(alias="primaryCertificate"),
    ]
    r"""Primary certificate of the enrollment."""

    ocsp_stapled: Annotated[Optional[bool], pydantic.Field(alias="ocspStapled")] = None
    r"""OCSP Stapling improves performance by including a valid OCSP response in every TLS handshake. We recommend all customers enable this feature."""

    ocsp_uris: Annotated[
        OptionalNullable[List[str]], pydantic.Field(alias="ocspUris")
    ] = UNSET
    r"""URI used for OCSP stapling validation."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["ocspStapled", "ocspUris"]
        nullable_fields = ["primaryCertificate", "ocspUris"]
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


class GetDeploymentsDeploymentsResponseKeyAlgorithm(str, Enum):
    r"""The key algorithm for the multi-stacked certificate. This is either `ECDSA` or `RSA`."""

    ECDSA = "ECDSA"
    RSA = "RSA"


class GetDeploymentsDeploymentsResponseSignatureAlgorithm(str, Enum):
    r"""Indicates the SHA (Secure Hash Algorithm) function. You can use either `SHA-1` for a 160-bit (20-byte) hash or `SHA-256` for a 256-bit (32-byte) hash."""

    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"


class GetDeploymentsDeploymentsMultiStackedCertificatesTypedDict(TypedDict):
    certificate: Nullable[str]
    r"""The certificate text."""
    trust_chain: Nullable[str]
    r"""The trust chain for the certificate."""
    expiry: NotRequired[str]
    r"""The expiration date for the certificate."""
    key_algorithm: NotRequired[GetDeploymentsDeploymentsResponseKeyAlgorithm]
    r"""The key algorithm for the multi-stacked certificate. This is either `ECDSA` or `RSA`."""
    signature_algorithm: NotRequired[
        Nullable[GetDeploymentsDeploymentsResponseSignatureAlgorithm]
    ]
    r"""Indicates the SHA (Secure Hash Algorithm) function. You can use either `SHA-1` for a 160-bit (20-byte) hash or `SHA-256` for a 256-bit (32-byte) hash."""


class GetDeploymentsDeploymentsMultiStackedCertificates(BaseModel):
    certificate: Nullable[str]
    r"""The certificate text."""

    trust_chain: Annotated[Nullable[str], pydantic.Field(alias="trustChain")]
    r"""The trust chain for the certificate."""

    expiry: Optional[str] = None
    r"""The expiration date for the certificate."""

    key_algorithm: Annotated[
        Optional[GetDeploymentsDeploymentsResponseKeyAlgorithm],
        pydantic.Field(alias="keyAlgorithm"),
    ] = None
    r"""The key algorithm for the multi-stacked certificate. This is either `ECDSA` or `RSA`."""

    signature_algorithm: Annotated[
        OptionalNullable[GetDeploymentsDeploymentsResponseSignatureAlgorithm],
        pydantic.Field(alias="signatureAlgorithm"),
    ] = UNSET
    r"""Indicates the SHA (Secure Hash Algorithm) function. You can use either `SHA-1` for a 160-bit (20-byte) hash or `SHA-256` for a 256-bit (32-byte) hash."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["expiry", "keyAlgorithm", "signatureAlgorithm"]
        nullable_fields = ["certificate", "trustChain", "signatureAlgorithm"]
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


class GetDeploymentsDeploymentsGeography(str, Enum):
    r"""Specifies the type of network where you want to deploy your certificate.  Use `core` to deploy across most of the world except for specially licensed areas.  Use `china+core` to include China, or `russia+core` to include Russia. Any non-`core` deployment needs to be enabled on your contract based on approval from the Chinese or Russian governments."""

    CORE = "core"
    CHINA_PLUS_CORE = "china+core"
    RUSSIA_PLUS_CORE = "russia+core"


class GetDeploymentsDeploymentsOcspStapling(str, Enum):
    r"""Indicates the OCSP stapling setting for the deployment. Use `on` to enable OCSP stapling, `off` to disable it, or `not-set` to ignore it."""

    ON = "on"
    OFF = "off"
    NOT_SET = "not-set"


class GetDeploymentsDeploymentsSecureNetwork(str, Enum):
    r"""The type of deployment network. A value of `standard-tls` means Akamai's standard secure network, while `enhanced-tls` means Akamai's more secure network with PCI compliance capability."""

    ENHANCED_TLS = "enhanced-tls"
    STANDARD_TLS = "standard-tls"


class GetDeploymentsDeploymentsNetworkConfigurationTypedDict(TypedDict):
    r"""Encapsulates information about your certificate's deployment configuration settings on staging."""

    quic_enabled: bool
    r"""QUIC transport layer network protocol."""
    sni_only: bool
    r"""Server Name Indication (SNI) is an extension of the Transport Layer Security (TLS) networking protocol. It allows a server to present many certificates on the same IP address. All modern web browsers support the SNI extension. If you have the same SAN on two or more certificates with the SNI-only option set, Akamai may serve traffic using any certificate which matches the requested SNI hostname. You should avoid any certificates with overlapping SAN names when using SNI-only."""
    disallowed_tls_versions: NotRequired[List[str]]
    r"""Disallowed TLS protocols."""
    dns_names: NotRequired[List[str]]
    r"""Names served by SNI-only enabled enrollments."""
    fips_mode: NotRequired[bool]
    r"""Enables Federal Information Processing Standards (FIPS) for the enrollment."""
    geography: NotRequired[GetDeploymentsDeploymentsGeography]
    r"""Specifies the type of network where you want to deploy your certificate.  Use `core` to deploy across most of the world except for specially licensed areas.  Use `china+core` to include China, or `russia+core` to include Russia. Any non-`core` deployment needs to be enabled on your contract based on approval from the Chinese or Russian governments."""
    must_have_ciphers: NotRequired[str]
    r"""Ciphers that you definitely want to include for your enrollment while deploying it on the network."""
    ocsp_stapling: NotRequired[GetDeploymentsDeploymentsOcspStapling]
    r"""Indicates the OCSP stapling setting for the deployment. Use `on` to enable OCSP stapling, `off` to disable it, or `not-set` to ignore it."""
    preferred_ciphers: NotRequired[str]
    r"""Ciphers that you preferably want to include for your enrollment while deploying it on the network."""
    secure_network: NotRequired[GetDeploymentsDeploymentsSecureNetwork]
    r"""The type of deployment network. A value of `standard-tls` means Akamai's standard secure network, while `enhanced-tls` means Akamai's more secure network with PCI compliance capability."""


class GetDeploymentsDeploymentsNetworkConfiguration(BaseModel):
    r"""Encapsulates information about your certificate's deployment configuration settings on staging."""

    quic_enabled: Annotated[bool, pydantic.Field(alias="quicEnabled")]
    r"""QUIC transport layer network protocol."""

    sni_only: Annotated[bool, pydantic.Field(alias="sniOnly")]
    r"""Server Name Indication (SNI) is an extension of the Transport Layer Security (TLS) networking protocol. It allows a server to present many certificates on the same IP address. All modern web browsers support the SNI extension. If you have the same SAN on two or more certificates with the SNI-only option set, Akamai may serve traffic using any certificate which matches the requested SNI hostname. You should avoid any certificates with overlapping SAN names when using SNI-only."""

    disallowed_tls_versions: Annotated[
        Optional[List[str]], pydantic.Field(alias="disallowedTlsVersions")
    ] = None
    r"""Disallowed TLS protocols."""

    dns_names: Annotated[Optional[List[str]], pydantic.Field(alias="dnsNames")] = None
    r"""Names served by SNI-only enabled enrollments."""

    fips_mode: Annotated[Optional[bool], pydantic.Field(alias="fipsMode")] = None
    r"""Enables Federal Information Processing Standards (FIPS) for the enrollment."""

    geography: Optional[GetDeploymentsDeploymentsGeography] = None
    r"""Specifies the type of network where you want to deploy your certificate.  Use `core` to deploy across most of the world except for specially licensed areas.  Use `china+core` to include China, or `russia+core` to include Russia. Any non-`core` deployment needs to be enabled on your contract based on approval from the Chinese or Russian governments."""

    must_have_ciphers: Annotated[
        Optional[str], pydantic.Field(alias="mustHaveCiphers")
    ] = None
    r"""Ciphers that you definitely want to include for your enrollment while deploying it on the network."""

    ocsp_stapling: Annotated[
        Optional[GetDeploymentsDeploymentsOcspStapling],
        pydantic.Field(alias="ocspStapling"),
    ] = None
    r"""Indicates the OCSP stapling setting for the deployment. Use `on` to enable OCSP stapling, `off` to disable it, or `not-set` to ignore it."""

    preferred_ciphers: Annotated[
        Optional[str], pydantic.Field(alias="preferredCiphers")
    ] = None
    r"""Ciphers that you preferably want to include for your enrollment while deploying it on the network."""

    secure_network: Annotated[
        Optional[GetDeploymentsDeploymentsSecureNetwork],
        pydantic.Field(alias="secureNetwork"),
    ] = None
    r"""The type of deployment network. A value of `standard-tls` means Akamai's standard secure network, while `enhanced-tls` means Akamai's more secure network with PCI compliance capability."""


class GetDeploymentsDeploymentsResponse200KeyAlgorithm(str, Enum):
    r"""The key algorithm for the multi-stacked certificate. This is either `ECDSA` or `RSA`."""

    ECDSA = "ECDSA"
    RSA = "RSA"


class GetDeploymentsDeploymentsResponse200SignatureAlgorithm(str, Enum):
    r"""Identifies the SHA (Secure Hash Algorithm) function. The NSA (National Security Agency) designed this function to produce a hash of certificate contents, which is used in a digital signature. This is either `SHA-1` for a 160-bit (20-byte) hash or `SHA-256` for a 256-bit (32-byte) hash. To ensure a secure hash function, use `SHA-256`."""

    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"


class GetDeploymentsDeploymentsPrimaryCertificateTypedDict(TypedDict):
    r"""The primary certificate of the enrollment."""

    certificate: Nullable[str]
    r"""The certificate text."""
    trust_chain: Nullable[str]
    r"""The trust chain for the certificate."""
    expiry: NotRequired[str]
    r"""The expiration date for the certificate."""
    key_algorithm: NotRequired[GetDeploymentsDeploymentsResponse200KeyAlgorithm]
    r"""The key algorithm for the multi-stacked certificate. This is either `ECDSA` or `RSA`."""
    signature_algorithm: NotRequired[
        Nullable[GetDeploymentsDeploymentsResponse200SignatureAlgorithm]
    ]
    r"""Identifies the SHA (Secure Hash Algorithm) function. The NSA (National Security Agency) designed this function to produce a hash of certificate contents, which is used in a digital signature. This is either `SHA-1` for a 160-bit (20-byte) hash or `SHA-256` for a 256-bit (32-byte) hash. To ensure a secure hash function, use `SHA-256`."""


class GetDeploymentsDeploymentsPrimaryCertificate(BaseModel):
    r"""The primary certificate of the enrollment."""

    certificate: Nullable[str]
    r"""The certificate text."""

    trust_chain: Annotated[Nullable[str], pydantic.Field(alias="trustChain")]
    r"""The trust chain for the certificate."""

    expiry: Optional[str] = None
    r"""The expiration date for the certificate."""

    key_algorithm: Annotated[
        Optional[GetDeploymentsDeploymentsResponse200KeyAlgorithm],
        pydantic.Field(alias="keyAlgorithm"),
    ] = None
    r"""The key algorithm for the multi-stacked certificate. This is either `ECDSA` or `RSA`."""

    signature_algorithm: Annotated[
        OptionalNullable[GetDeploymentsDeploymentsResponse200SignatureAlgorithm],
        pydantic.Field(alias="signatureAlgorithm"),
    ] = UNSET
    r"""Identifies the SHA (Secure Hash Algorithm) function. The NSA (National Security Agency) designed this function to produce a hash of certificate contents, which is used in a digital signature. This is either `SHA-1` for a 160-bit (20-byte) hash or `SHA-256` for a 256-bit (32-byte) hash. To ensure a secure hash function, use `SHA-256`."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["expiry", "keyAlgorithm", "signatureAlgorithm"]
        nullable_fields = ["certificate", "trustChain", "signatureAlgorithm"]
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


class StagingTypedDict(TypedDict):
    r"""Encapsulates information about your certificate's deployment on the staging network."""

    multi_stacked_certificates: List[
        GetDeploymentsDeploymentsMultiStackedCertificatesTypedDict
    ]
    r"""Dual-stacked certificates today include an ECDSA certificate in addition to an RSA certificate."""
    network_configuration: GetDeploymentsDeploymentsNetworkConfigurationTypedDict
    r"""Encapsulates information about your certificate's deployment configuration settings on staging."""
    primary_certificate: Nullable[GetDeploymentsDeploymentsPrimaryCertificateTypedDict]
    r"""The primary certificate of the enrollment."""
    ocsp_stapled: NotRequired[bool]
    r"""OCSP Stapling improves performance by including a valid OCSP response in every TLS handshake. You should enable this feature."""
    ocsp_uris: NotRequired[Nullable[List[str]]]
    r"""URI used for OCSP stapling validation."""


class Staging(BaseModel):
    r"""Encapsulates information about your certificate's deployment on the staging network."""

    multi_stacked_certificates: Annotated[
        List[GetDeploymentsDeploymentsMultiStackedCertificates],
        pydantic.Field(alias="multiStackedCertificates"),
    ]
    r"""Dual-stacked certificates today include an ECDSA certificate in addition to an RSA certificate."""

    network_configuration: Annotated[
        GetDeploymentsDeploymentsNetworkConfiguration,
        pydantic.Field(alias="networkConfiguration"),
    ]
    r"""Encapsulates information about your certificate's deployment configuration settings on staging."""

    primary_certificate: Annotated[
        Nullable[GetDeploymentsDeploymentsPrimaryCertificate],
        pydantic.Field(alias="primaryCertificate"),
    ]
    r"""The primary certificate of the enrollment."""

    ocsp_stapled: Annotated[Optional[bool], pydantic.Field(alias="ocspStapled")] = None
    r"""OCSP Stapling improves performance by including a valid OCSP response in every TLS handshake. You should enable this feature."""

    ocsp_uris: Annotated[
        OptionalNullable[List[str]], pydantic.Field(alias="ocspUris")
    ] = UNSET
    r"""URI used for OCSP stapling validation."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["ocspStapled", "ocspUris"]
        nullable_fields = ["primaryCertificate", "ocspUris"]
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


class GetDeploymentsResponseBodyTypedDict(TypedDict):
    r"""Deploys your certificate to a network."""

    production: ProductionTypedDict
    r"""Encapsulates information about your certificate's deployment on the production network."""
    staging: StagingTypedDict
    r"""Encapsulates information about your certificate's deployment on the staging network."""


class GetDeploymentsResponseBody(BaseModel):
    r"""Deploys your certificate to a network."""

    production: Production
    r"""Encapsulates information about your certificate's deployment on the production network."""

    staging: Staging
    r"""Encapsulates information about your certificate's deployment on the staging network."""
