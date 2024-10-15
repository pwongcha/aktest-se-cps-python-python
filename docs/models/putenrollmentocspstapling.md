# PutEnrollmentOcspStapling

Enable OCSP stapling for the enrollment. OCSP Stapling improves performance by including a valid OCSP response in every TLS handshake. Specify OCSP Stapling if you want to improve performance by allowing your site's visitors to query the Online Certificate Status Protocol (OCSP) server at regular intervals to obtain a signed time-stamped OCSP response. This response needs to be signed by the CA, not the server, therefore ensuring security. Disable OSCP Stapling if you want your site's visitors to contact the CA directly for an OSCP response. You can use OCSP to obtain a certificate's revocation status. You should enable this feature. Use `on` to enable OSCP Stapling, `off` to disable it, or `not-set` to ignore it.


## Values

| Name      | Value     |
| --------- | --------- |
| `ON`      | on        |
| `OFF`     | off       |
| `NOT_SET` | not-set   |