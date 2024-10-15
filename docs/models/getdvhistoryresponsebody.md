# GetDvHistoryResponseBody

If you use domain validation, the CA that issued the certificate validates that you have control of the domain. CPS supports DV certificates issued by Let's Encrypt, an automated, and open CA, run for public benefit. Use the domain validation history to view your Akamai managed DV certificates' history and errors. These certificates expire in 90 days.


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `results`                                                                             | List[[models.Results](../models/results.md)]                                          | :heavy_check_mark:                                                                    | Domain Validation (DV) challenges are used by Let's Encrypt to verify domain control. |