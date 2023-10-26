
```python
#!/usr/bin/env python3

import sys
import time
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionExecption

ip = sys.argv[1]
client = ModbusClient(ip, port=502)
client.connect()
while True:
    client.write_register(1, 0) #le 1 correspond au register sur lequel écrire et le 0 la valeur à insérer, possibilité d'avoir plusieurs lignes
    client.write_coils(40, 1)

```
