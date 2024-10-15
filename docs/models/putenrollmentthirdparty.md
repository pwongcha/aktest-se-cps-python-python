# PutEnrollmentThirdParty

Specifies that you want to use a third party certificate. This is any certificate that is not issued through CPS.


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `exclude_sans`                                                                                         | *bool*                                                                                                 | :heavy_check_mark:                                                                                     | If this is `true`, then the SANs in the enrollment don't appear in the CSR that CPS submits to the CA. |