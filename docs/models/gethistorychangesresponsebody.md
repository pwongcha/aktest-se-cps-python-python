# GetHistoryChangesResponseBody

The change history includes all changes to a certificate. This is the equivalent of viewing the certificate activity in the CPS UI. You can view each change to your certificate, the status of your change, the last updated date, the date the change was created, and who created the change. You can also take actions on each change of the certificate, including viewing the CSR for the certificate, viewing the certificate, and viewing the trust chain for the certificate.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `changes`                                                                      | List[[models.GetHistoryChangesChanges](../models/gethistorychangeschanges.md)] | :heavy_check_mark:                                                             | Change history items.                                                          |