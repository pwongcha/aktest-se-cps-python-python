# Enrollments
(*enrollments*)

## Overview

Manage your certificate enrollments.

### Available Operations

* [post_enrollment](#post_enrollment) - Create an enrollment
* [get_enrollments](#get_enrollments) - List enrollments
* [get_enrollment](#get_enrollment) - Get an enrollment
* [put_enrollment](#put_enrollment) - Update an enrollment
* [delete_enrollment](#delete_enrollment) - Remove an enrollment
* [get_dv_history](#get_dv_history) - Get DV history
* [get_history_certificates](#get_history_certificates) - Get certificate history

## post_enrollment

Creates an enrollment that contains all the information about the process that your certificate goes through from the time you request it, through renewal, and as you obtain subsequent versions. To select a Client TLS Renegotiation option, use the CPS user interface. For details, see [Edit deployment settings](doc:view-edit-network-deploy-settings). Note that you can create one certificate every five minutes, per account. Creating a certificate for the same contract within the five-minute interval results in a 409 response.

See documentation for this operation in Akamai's Certificate Provisioning System API
<https://techdocs.akamai.com/cps/reference/post-enrollment>

### Example Usage

```python
import aktest_se_cps_python
from aktest_se_cps_python import AktestSeCpsPython

s = AktestSeCpsPython()

res = s.enrollments.post_enrollment(request={
    "contract_id": "K-0N7RAK7",
    "request_body": {
        "certificate_type": aktest_se_cps_python.CertificateType.THIRD_PARTY,
        "change_management": True,
        "csr": {
            "cn": "www.example.com",
            "c": "US",
            "l": "Cambridge",
            "o": "Akamai",
            "ou": "WebEx",
            "preferred_trust_chain": None,
            "sans": [
                "san1.example.com",
                "san2.example.com",
                "san3.example.com",
                "www.example.com",
            ],
            "st": "MA",
        },
        "enable_multi_stacked_certificates": False,
        "network_configuration": {
            "geography": aktest_se_cps_python.Geography.CORE,
            "quic_enabled": False,
            "secure_network": aktest_se_cps_python.SecureNetwork.ENHANCED_TLS,
            "sni_only": True,
            "client_mutual_authentication": {
                "authentication_options": {
                    "ocsp": {
                        "enabled": False,
                    },
                    "send_ca_list_to_client": False,
                },
                "set_id": "Custom_CPS-6134b_B-3-1AHBENT.xml",
            },
            "disallowed_tls_versions": [
                "TLSv1",
                "TLSv1_1",
            ],
            "dns_name_settings": {
                "clone_dns_names": False,
                "dns_names": [
                    "san2.example.com",
                    "san1.example.com",
                ],
            },
            "fips_mode": True,
            "must_have_ciphers": "ak-akamai-2020q1",
            "ocsp_stapling": aktest_se_cps_python.OcspStapling.ON,
            "preferred_ciphers": "ak-akamai-2020q1",
        },
        "ra": aktest_se_cps_python.Ra.THIRD_PARTY,
        "validation_type": aktest_se_cps_python.ValidationType.THIRD_PARTY,
        "admin_contact": {
            "address_line_one": "150 Broadway",
            "address_line_two": None,
            "city": "Cambridge",
            "country": "US",
            "email": "afero@akamai.com",
            "first_name": "R1",
            "last_name": "D1",
            "organization_name": "Akamai",
            "phone": "617-555-0111",
            "postal_code": "02142",
            "region": "MA",
            "title": "Adminstrator",
        },
        "assigned_slots": [
            1234,
        ],
        "auto_renewal_start_time": None,
        "certificate_chain_type": aktest_se_cps_python.CertificateChainType.DEFAULT,
        "id": "10001",
        "location": "/cps-api/enrollments/10001",
        "max_allowed_san_names": 100,
        "max_allowed_wildcard_san_names": 100,
        "org": {
            "address_line_one": "150 Broadway",
            "address_line_two": None,
            "city": "Cambridge",
            "country": "US",
            "name": "Akamai Technologies",
            "phone": "617-555-0111",
            "postal_code": "02142",
            "region": "MA",
        },
        "org_id": 645263546,
        "pending_changes": [
            {
                "location": "/cps-api/enrollments/10001/changes/10002",
                "change_type": aktest_se_cps_python.ChangeType.NEW_CERTIFICATE,
            },
        ],
        "production_slots": [
            1234,
        ],
        "signature_algorithm": None,
        "staging_slots": [
            1234,
        ],
        "tech_contact": {
            "address_line_one": "150 Broadway",
            "address_line_two": None,
            "city": "Cambridge",
            "country": "US",
            "email": "jsmith@akamai.com",
            "first_name": "R2",
            "last_name": "D2",
            "organization_name": "Akamai",
            "phone": "617-555-0111",
            "postal_code": "02142",
            "region": "MA",
            "title": "Technical Engineer",
        },
        "third_party": {
            "exclude_sans": False,
        },
    },
    "deploy_not_after": "2021-01-31",
    "deploy_not_before": "2021-01-31",
    "account_switch_key": "1-5C0YLB:1-8BYUX",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.PostEnrollmentRequest](../../models/postenrollmentrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.PostEnrollmentResponseBody](../../models/postenrollmentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_enrollments

A list of the names of each enrollment.

See documentation for this operation in Akamai's Certificate Provisioning System API
<https://techdocs.akamai.com/cps/reference/get-enrollments>

### Example Usage

```python
from aktest_se_cps_python import AktestSeCpsPython

s = AktestSeCpsPython()

res = s.enrollments.get_enrollments(contract_id="K-0N7RAK7", account_switch_key="1-5C0YLB:1-8BYUX")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                   | Example                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contract_id`                                                                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                            | Specify the contract on which to operate or view.                                                                                                                                                                                                                                                                                                             | K-0N7RAK7                                                                                                                                                                                                                                                                                                                                                     |
| `account_switch_key`                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | For customers who manage more than one account, this [runs the operation from another account](https://techdocs.akamai.com/developer/docs/manage-many-accounts-with-one-api-client). The Identity and Access Management API provides a [list of available account switch keys](https://techdocs.akamai.com/iam-api/reference/get-client-account-switch-keys). | 1-5C0YLB:1-8BYUX                                                                                                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                               |

### Response

**[models.GetEnrollmentsResponseBody](../../models/getenrollmentsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_enrollment

Gets an enrollment.

See documentation for this operation in Akamai's Certificate Provisioning System API
<https://techdocs.akamai.com/cps/reference/get-enrollment>

### Example Usage

```python
from aktest_se_cps_python import AktestSeCpsPython

s = AktestSeCpsPython()

res = s.enrollments.get_enrollment(enrollment_id=10000, account_switch_key="1-5C0YLB:1-8BYUX")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                   | Example                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enrollment_id`                                                                                                                                                                                                                                                                                                                                               | *int*                                                                                                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                            | Enrollment on which to perform the desired operation.                                                                                                                                                                                                                                                                                                         | 10000                                                                                                                                                                                                                                                                                                                                                         |
| `account_switch_key`                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | For customers who manage more than one account, this [runs the operation from another account](https://techdocs.akamai.com/developer/docs/manage-many-accounts-with-one-api-client). The Identity and Access Management API provides a [list of available account switch keys](https://techdocs.akamai.com/iam-api/reference/get-client-account-switch-keys). | 1-5C0YLB:1-8BYUX                                                                                                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                               |

### Response

**[models.GetEnrollmentResponseBody](../../models/getenrollmentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## put_enrollment

Updates an enrollment with changes. Response type varies depending on the type and impact of change. For example, changing SANs list may return HTTP 202 Accepted since the operation requires a new certificate and network deployment operations, and thus can't be completed without a change. On the contrary, for example a Technical Contact name change may return HTTP 200 OK assuming there are no active change and when the operation does not require a new certificate.

Note that `fipsMode` requires that TLS 1.2, TLS 1.3, or both are enabled on the certificate. You can’t list these TLS versions as disabled in the `disallowedTlsVersions` deployment object. When `fipsMode` is enabled, you need to use an active (non-deprecated) cipher profile for both `mustHaveCiphers` and `preferredCiphers`. For details, see [Update SSL/TLS cipher profiles](doc:cipher-profiles).

See documentation for this operation in Akamai's Certificate Provisioning System API
<https://techdocs.akamai.com/cps/reference/put-enrollment>

### Example Usage

```python
import aktest_se_cps_python
from aktest_se_cps_python import AktestSeCpsPython

s = AktestSeCpsPython()

res = s.enrollments.put_enrollment(request={
    "enrollment_id": 10000,
    "request_body": {
        "certificate_type": aktest_se_cps_python.PutEnrollmentCertificateType.THIRD_PARTY,
        "change_management": True,
        "csr": {
            "cn": "www.example.com",
            "c": "US",
            "l": "Cambridge",
            "o": "Akamai",
            "ou": "WebEx",
            "preferred_trust_chain": None,
            "sans": [
                "san1.example.com",
                "san2.example.com",
                "san3.example.com",
                "www.example.com",
            ],
            "st": "MA",
        },
        "enable_multi_stacked_certificates": False,
        "network_configuration": {
            "geography": aktest_se_cps_python.PutEnrollmentGeography.CORE,
            "quic_enabled": False,
            "secure_network": aktest_se_cps_python.PutEnrollmentSecureNetwork.ENHANCED_TLS,
            "sni_only": True,
            "client_mutual_authentication": {
                "authentication_options": {
                    "ocsp": {
                        "enabled": False,
                    },
                    "send_ca_list_to_client": False,
                },
                "set_id": "Custom_CPS-6134b_B-3-1AHBENT.xml",
            },
            "disallowed_tls_versions": [
                "TLSv1",
                "TLSv1_1",
            ],
            "dns_name_settings": {
                "clone_dns_names": False,
                "dns_names": [
                    "san2.example.com",
                    "san1.example.com",
                ],
            },
            "fips_mode": True,
            "must_have_ciphers": "ak-akamai-2020q1",
            "ocsp_stapling": aktest_se_cps_python.PutEnrollmentOcspStapling.ON,
            "preferred_ciphers": "ak-akamai-2020q1",
        },
        "ra": aktest_se_cps_python.PutEnrollmentRa.THIRD_PARTY,
        "validation_type": aktest_se_cps_python.PutEnrollmentValidationType.THIRD_PARTY,
        "admin_contact": {
            "address_line_one": "150 Broadway",
            "address_line_two": None,
            "city": "Cambridge",
            "country": "US",
            "email": "afero@akamai.com",
            "first_name": "R1",
            "last_name": "D1",
            "organization_name": "Akamai",
            "phone": "617-555-0111",
            "postal_code": "02142",
            "region": "MA",
            "title": "Adminstrator",
        },
        "assigned_slots": [
            1234,
        ],
        "auto_renewal_start_time": None,
        "certificate_chain_type": aktest_se_cps_python.PutEnrollmentCertificateChainType.DEFAULT,
        "id": "10001",
        "location": "/cps-api/enrollments/10001",
        "max_allowed_san_names": 100,
        "max_allowed_wildcard_san_names": 100,
        "org": {
            "address_line_one": "150 Broadway",
            "address_line_two": None,
            "city": "Cambridge",
            "country": "US",
            "name": "Akamai Technologies",
            "phone": "617-555-0111",
            "postal_code": "02142",
            "region": "MA",
        },
        "org_id": 645263546,
        "pending_changes": [
            {
                "location": "/cps-api/enrollments/10001/changes/10002",
                "change_type": aktest_se_cps_python.PutEnrollmentChangeType.NEW_CERTIFICATE,
            },
        ],
        "production_slots": [
            1234,
        ],
        "signature_algorithm": None,
        "staging_slots": [
            1234,
        ],
        "tech_contact": {
            "address_line_one": "150 Broadway",
            "address_line_two": None,
            "city": "Cambridge",
            "country": "US",
            "email": "jsmith@akamai.com",
            "first_name": "R2",
            "last_name": "D2",
            "organization_name": "Akamai",
            "phone": "617-555-0111",
            "postal_code": "02142",
            "region": "MA",
            "title": "Technical Engineer",
        },
        "third_party": {
            "exclude_sans": False,
        },
    },
    "allow_cancel_pending_changes": True,
    "allow_staging_bypass": True,
    "deploy_not_after": "2021-01-31",
    "deploy_not_before": "2021-01-31",
    "force_renewal": True,
    "renewal_date_check_override": True,
    "allow_missing_certificate_addition": True,
    "account_switch_key": "1-5C0YLB:1-8BYUX",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.PutEnrollmentRequest](../../models/putenrollmentrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PutEnrollmentResponse](../../models/putenrollmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete_enrollment

Removes an enrollment from CPS. The response code varies depending on the state of the enrollment. Deleting an enrollment in the future, or deleting when the enrollment has a certificate deployed to the network, may result in a 202 response. Deleting an enrollment that hasn't yet deployed any certificate to the network responds immediately with a 200 code.

See documentation for this operation in Akamai's Certificate Provisioning System API
<https://techdocs.akamai.com/cps/reference/delete-enrollment>

### Example Usage

```python
from aktest_se_cps_python import AktestSeCpsPython

s = AktestSeCpsPython()

res = s.enrollments.delete_enrollment(request={
    "enrollment_id": 10000,
    "allow_cancel_pending_changes": True,
    "deploy_not_after": "2021-01-31",
    "deploy_not_before": "2021-01-31",
    "account_switch_key": "1-5C0YLB:1-8BYUX",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.DeleteEnrollmentRequest](../../models/deleteenrollmentrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.DeleteEnrollmentResponse](../../models/deleteenrollmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_dv_history

Domain name Validation history for the enrollment.

See documentation for this operation in Akamai's Certificate Provisioning System API
<https://techdocs.akamai.com/cps/reference/get-dv-history>

### Example Usage

```python
from aktest_se_cps_python import AktestSeCpsPython

s = AktestSeCpsPython()

res = s.enrollments.get_dv_history(enrollment_id=10000, account_switch_key="1-5C0YLB:1-8BYUX")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                   | Example                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enrollment_id`                                                                                                                                                                                                                                                                                                                                               | *int*                                                                                                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                            | Enrollment on which to perform the desired operation.                                                                                                                                                                                                                                                                                                         | 10000                                                                                                                                                                                                                                                                                                                                                         |
| `account_switch_key`                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | For customers who manage more than one account, this [runs the operation from another account](https://techdocs.akamai.com/developer/docs/manage-many-accounts-with-one-api-client). The Identity and Access Management API provides a [list of available account switch keys](https://techdocs.akamai.com/iam-api/reference/get-client-account-switch-keys). | 1-5C0YLB:1-8BYUX                                                                                                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                               |

### Response

**[models.GetDvHistoryResponseBody](../../models/getdvhistoryresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_history_certificates

View the certificate history. To view deployed certificates and their expiration dates, run the [Get production deployment](ref:get-deployments-production) operation. Note that for enrollments with six certificates or fewer, the response yields up to twelve years of data per certificate. If there are more than six certificates in the enrollment, the response shows a truncated set. To view all changes or certificates, use the `includeAll=true` query parameter in the request.

See documentation for this operation in Akamai's Certificate Provisioning System API
<https://techdocs.akamai.com/cps/reference/get-history-certificates>

### Example Usage

```python
from aktest_se_cps_python import AktestSeCpsPython

s = AktestSeCpsPython()

res = s.enrollments.get_history_certificates(enrollment_id=10000, include_all=True, account_switch_key="1-5C0YLB:1-8BYUX")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                   | Example                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enrollment_id`                                                                                                                                                                                                                                                                                                                                               | *int*                                                                                                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                            | Enrollment on which to perform the desired operation.                                                                                                                                                                                                                                                                                                         | 10000                                                                                                                                                                                                                                                                                                                                                         |
| `include_all`                                                                                                                                                                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Retrieve all changes or certificates.                                                                                                                                                                                                                                                                                                                         | true                                                                                                                                                                                                                                                                                                                                                          |
| `account_switch_key`                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | For customers who manage more than one account, this [runs the operation from another account](https://techdocs.akamai.com/developer/docs/manage-many-accounts-with-one-api-client). The Identity and Access Management API provides a [list of available account switch keys](https://techdocs.akamai.com/iam-api/reference/get-client-account-switch-keys). | 1-5C0YLB:1-8BYUX                                                                                                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                               |

### Response

**[models.GetHistoryCertificatesResponseBody](../../models/gethistorycertificatesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |