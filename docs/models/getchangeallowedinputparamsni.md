# GetChangeAllowedInputParamSni

Server Name Indication (SNI) setting for this enrollment.


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `clone_dns_names`                                             | *bool*                                                        | :heavy_check_mark:                                            | When `true`, all certificate SANs are included in `dnsNames`. |
| `dns_names`                                                   | List[*str*]                                                   | :heavy_minus_sign:                                            | Names served by SNI-only enabled enrollments.                 |