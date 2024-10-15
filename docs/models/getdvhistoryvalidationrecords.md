# GetDvHistoryValidationRecords


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `hostname`                                                             | *str*                                                                  | :heavy_check_mark:                                                     | The records that Let's Encrypt returns to you to validate your domain. |
| `port`                                                                 | *str*                                                                  | :heavy_check_mark:                                                     | Port used for validation.                                              |
| `resolved_ip`                                                          | List[*str*]                                                            | :heavy_check_mark:                                                     | IPs resolved for name being validated.                                 |
| `url`                                                                  | *str*                                                                  | :heavy_check_mark:                                                     | URL attempted validated.                                               |
| `used_ip`                                                              | *str*                                                                  | :heavy_check_mark:                                                     | IP from `resolvedIp` used for this validation.                         |