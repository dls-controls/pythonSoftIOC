from softioc import softioc
from cothread.catools import caget, caput, camonitor

print(caget("MY-DEVICE-PREFIX:AI"))
print(caget("MY-DEVICE-PREFIX:AO"))
print(caput("MY-DEVICE-PREFIX:AO", "999"))
print(caget("MY-DEVICE-PREFIX:AO"))

softioc.interactive_ioc(globals())
