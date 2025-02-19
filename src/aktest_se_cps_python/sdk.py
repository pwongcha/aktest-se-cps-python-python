"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from aktest_se_cps_python import utils
from aktest_se_cps_python._hooks import SDKHooks
from aktest_se_cps_python.certificates import Certificates
from aktest_se_cps_python.changes import Changes
from aktest_se_cps_python.deployments import Deployments
from aktest_se_cps_python.enrollments import Enrollments
from aktest_se_cps_python.types import OptionalNullable, UNSET
import httpx
from typing import Dict, Optional


class AktestSeCpsPython(BaseSDK):
    r"""https://techdocs.akamai.com/cps/reference - See documentation for Akamai's Certificate Provisioning System API"""

    certificates: Certificates
    r"""Get information on your certificates."""
    enrollments: Enrollments
    r"""Manage your certificate enrollments."""
    changes: Changes
    r"""Manage changes to an enrollment's network deployment."""
    deployments: Deployments
    r"""Manage your certificate deployments."""

    def __init__(
        self,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                async_client=async_client,
                server_url=server_url,
                server_idx=server_idx,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, self.sdk_configuration.client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self._init_sdks()

    def _init_sdks(self):
        self.certificates = Certificates(self.sdk_configuration)
        self.enrollments = Enrollments(self.sdk_configuration)
        self.changes = Changes(self.sdk_configuration)
        self.deployments = Deployments(self.sdk_configuration)
