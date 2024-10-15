<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from aktest_se_cps_python import AktestSeCpsPython

s = AktestSeCpsPython()

res = s.certificates.get_active_certificates(contract_id="K-0N7RAK7", account_switch_key="1-5C0YLB:1-8BYUX")

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
from aktest_se_cps_python import AktestSeCpsPython
import asyncio

async def main():
    s = AktestSeCpsPython()
    res = await s.certificates.get_active_certificates_async(contract_id="K-0N7RAK7", account_switch_key="1-5C0YLB:1-8BYUX")
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->