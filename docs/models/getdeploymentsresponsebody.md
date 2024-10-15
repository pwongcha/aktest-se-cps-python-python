# GetDeploymentsResponseBody

Deploys your certificate to a network.


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `production`                                                                            | [models.Production](../models/production.md)                                            | :heavy_check_mark:                                                                      | Encapsulates information about your certificate's deployment on the production network. |
| `staging`                                                                               | [models.Staging](../models/staging.md)                                                  | :heavy_check_mark:                                                                      | Encapsulates information about your certificate's deployment on the staging network.    |