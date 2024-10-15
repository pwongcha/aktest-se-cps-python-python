# PendingCertificate

The snapshot of the pending certificate for the enrollment when this change takes effect.


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `certificate_type`                        | *str*                                     | :heavy_check_mark:                        | The kind of certificate created.          |
| `full_certificate`                        | *str*                                     | :heavy_check_mark:                        | Displays the contents of the certificate. |
| `signature_algorithm`                     | *Nullable[str]*                           | :heavy_check_mark:                        | Displays the signature algorithm.         |