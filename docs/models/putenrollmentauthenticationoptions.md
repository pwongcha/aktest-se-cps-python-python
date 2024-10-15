# PutEnrollmentAuthenticationOptions

Contains the configuration options for the selected trust chain.


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `ocsp`                                                                                           | [Nullable[models.PutEnrollmentOcsp]](../models/putenrollmentocsp.md)                             | :heavy_check_mark:                                                                               | Whether you want to enable OCSP stapling for client certificates.                                |
| `send_ca_list_to_client`                                                                         | *Nullable[bool]*                                                                                 | :heavy_check_mark:                                                                               | Whether you want to enable the server to send the certificate authority (CA) list to the client. |