# ValidationRecords


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `authorities`                                   | List[*str*]                                     | :heavy_check_mark:                              | Validation authorities.                         |
| `hostname`                                      | *str*                                           | :heavy_check_mark:                              | Domain name being validated.                    |
| `port`                                          | *str*                                           | :heavy_check_mark:                              | Port used for validation.                       |
| `resolved_ip`                                   | List[*str*]                                     | :heavy_check_mark:                              | IPs resolved for name being validated.          |
| `tried_ip`                                      | *str*                                           | :heavy_check_mark:                              | IP from `resolvedIp` tried for this validation. |
| `url`                                           | *str*                                           | :heavy_check_mark:                              | URL attempted validated.                        |
| `used_ip`                                       | *str*                                           | :heavy_check_mark:                              | IP from `resolvedIp` used for this validation.  |