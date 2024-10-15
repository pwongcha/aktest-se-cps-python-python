# PendingState

The snapshot of the pending state for the enrollment when this change takes effect.


## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `pending_network_configuration`                                                                     | [models.PendingNetworkConfiguration](../models/pendingnetworkconfiguration.md)                      | :heavy_check_mark:                                                                                  | The snapshot of the pending network configuration for the enrollment when this change takes effect. |
| `pending_certificate`                                                                               | [Optional[models.PendingCertificate]](../models/pendingcertificate.md)                              | :heavy_minus_sign:                                                                                  | The snapshot of the pending certificate for the enrollment when this change takes effect.           |