# GetChangeAllowedInputParamChangesSni

Server Name Indication (SNI) setting for this Enrollment.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `clone_dns_names`                                                    | *bool*                                                               | :heavy_check_mark:                                                   | Descriptive text for the cloned DNS.                                 |
| `dns_names`                                                          | List[*str*]                                                          | :heavy_minus_sign:                                                   | Descriptive text for the DNS served by SNI-only enabled enrollments. |