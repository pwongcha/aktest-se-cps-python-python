"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from aktest_se_cps_python import models, utils
from aktest_se_cps_python._hooks import HookContext
from aktest_se_cps_python.types import OptionalNullable, UNSET
from typing import Optional


class Certificates(BaseSDK):
    r"""Get information on your certificates."""

    def get_active_certificates(
        self,
        *,
        contract_id: str,
        account_switch_key: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.GetActiveCertificatesResponseBody:
        r"""List active certificates

        __Limited availability__ Lists enrollments with active certificates. Note that the rate limit for this operation is 10 requests per minute per account. For details, see [Rate limiting](ref:rate-limiting).
        https://techdocs.akamai.com/cps/reference/get-active-certificates - See documentation for this operation in Akamai's Certificate Provisioning System API

        :param contract_id: Specify the contract on which to operate or view.
        :param account_switch_key: For customers who manage more than one account, this [runs the operation from another account](https://techdocs.akamai.com/developer/docs/manage-many-accounts-with-one-api-client). The Identity and Access Management API provides a [list of available account switch keys](https://techdocs.akamai.com/iam-api/reference/get-client-account-switch-keys).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.GetActiveCertificatesRequest(
            contract_id=contract_id,
            account_switch_key=account_switch_key,
        )

        req = self.build_request(
            method="GET",
            path="/active-certificates",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/vnd.akamai.cps.active-certificates.v2+json",
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="get-active-certificates",
                oauth2_scopes=[],
                security_source=None,
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(
            http_res, "200", "application/vnd.akamai.cps.active-certificates.v2+json"
        ):
            return utils.unmarshal_json(
                http_res.text, models.GetActiveCertificatesResponseBody
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def get_active_certificates_async(
        self,
        *,
        contract_id: str,
        account_switch_key: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.GetActiveCertificatesResponseBody:
        r"""List active certificates

        __Limited availability__ Lists enrollments with active certificates. Note that the rate limit for this operation is 10 requests per minute per account. For details, see [Rate limiting](ref:rate-limiting).
        https://techdocs.akamai.com/cps/reference/get-active-certificates - See documentation for this operation in Akamai's Certificate Provisioning System API

        :param contract_id: Specify the contract on which to operate or view.
        :param account_switch_key: For customers who manage more than one account, this [runs the operation from another account](https://techdocs.akamai.com/developer/docs/manage-many-accounts-with-one-api-client). The Identity and Access Management API provides a [list of available account switch keys](https://techdocs.akamai.com/iam-api/reference/get-client-account-switch-keys).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.GetActiveCertificatesRequest(
            contract_id=contract_id,
            account_switch_key=account_switch_key,
        )

        req = self.build_request_async(
            method="GET",
            path="/active-certificates",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/vnd.akamai.cps.active-certificates.v2+json",
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="get-active-certificates",
                oauth2_scopes=[],
                security_source=None,
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(
            http_res, "200", "application/vnd.akamai.cps.active-certificates.v2+json"
        ):
            return utils.unmarshal_json(
                http_res.text, models.GetActiveCertificatesResponseBody
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )
