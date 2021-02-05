# Runtime Status Library

A useful tool to print helpful runtime status messages


## Installation 

`pip install rtstatlib`

## Example

```
import logging
from rtstatlib import rtstat as rs   

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

rs.sync_log()

```
