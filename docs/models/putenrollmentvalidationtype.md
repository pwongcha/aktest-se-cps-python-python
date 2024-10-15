# PutEnrollmentValidationType

CPS supports several types of validation: `dv`, `ev`, `ov`, or `third-party`. Domain Validation (`dv`) offers the lowest level of validation. The CA validates that you have control of the domain. CPS supports DV certificates issued by Let's Encrypt, a free, automated, and open CA, run for public benefit. Organization Validation (`ov`) offers the next level of validation. The CA validates that you have control of the domain. Extended Validation (`ev`) offers the highest level of validation, in which you need to have signed letters and notaries sent to the CA before signing. You can also specify `third-party` if you want to use a signed certificate you obtain from a CA that CPS doesn't directly support.


## Values

| Name          | Value         |
| ------------- | ------------- |
| `DV`          | dv            |
| `EV`          | ev            |
| `OV`          | ov            |
| `THIRD_PARTY` | third-party   |