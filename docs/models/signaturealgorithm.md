# SignatureAlgorithm

Identifies the SHA (Secure Hash Algorithm) function. The NSA (National Security Agency) designed this function to produce a hash of certificate contents, for use in a digital signature. This is either `SHA-1` for a 160-bit (20-byte) hash or `SHA-256` for a 256-bit (32-byte) hash. To ensure a secure hash function, use `SHA-256`.


## Values

| Name      | Value     |
| --------- | --------- |
| `SHA_1`   | SHA-1     |
| `SHA_256` | SHA-256   |