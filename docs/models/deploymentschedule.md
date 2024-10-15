# DeploymentSchedule

The schedule for when you want this change to deploy.


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `not_after`                                    | *Nullable[str]*                                | :heavy_check_mark:                             | Don't deploy the certificate after this date.  |
| `not_before`                                   | *Nullable[str]*                                | :heavy_check_mark:                             | Don't deploy the certificate before this date. |