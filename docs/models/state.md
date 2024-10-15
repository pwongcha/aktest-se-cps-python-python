# State

The change request's state. A value of `new` means the certificate is processed but the renewal process is not started. A `running` value means CPS is preparing to send your certificate to Let's Encrypt. An `awaiting-input` value means the process is waiting on a user input, for example the approval or denial of a change management item. A `suspended` value indicates the process didn't complete. A value of `cancelled` means the process has been cancelled permanently, A `completed` value means the change request is finished. An `error` value means there's an issue with the domain. 


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `NEW`            | new              |
| `RUNNING`        | running          |
| `AWAITING_INPUT` | awaiting-input   |
| `SUSPENDED`      | suspended        |
| `CANCELLED`      | cancelled        |
| `COMPLETED`      | completed        |
| `ERROR`          | error            |