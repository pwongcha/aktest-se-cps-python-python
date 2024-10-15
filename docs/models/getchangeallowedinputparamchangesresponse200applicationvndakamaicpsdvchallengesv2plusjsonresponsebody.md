# GetChangeAllowedInputParamChangesResponse200ApplicationVndAkamaiCpsDvChallengesV2PlusJSONResponseBody

When using certificates with domain validation, you prove that you have control over each of the domains listed in the certificate. When you create a new DV enrollment that generates a certificate signing request (CSR), CPS automatically sends it to Let's Encrypt for signing. Let's Encrypt sends back a challenge for each domain listed on your certificate. You prove that you have control over the domains listed in the CSR by redirecting your traffic to Akamai, or placing a token in the domain's DNS zone. This allows Akamai to complete the challenge process for you by detecting the redirect or DNS token, and answering Let's Encrypt's challenge. You need to complete one of the challenges for each domain to validate the certificate. To validate a domain, only one challenge for each domain needs to be complete. Let's Encrypt automatically verifies the domain after it receives an answer to the challenge, and marks the domain as validated.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `dv`                                                     | List[[models.Dv](../models/dv.md)]                       | :heavy_check_mark:                                       | Domain validation entities returned in query parameters. |