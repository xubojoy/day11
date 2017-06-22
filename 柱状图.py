#Author:xubojoy

import os
from lightning import Lightning
from numpy import random
from IPython.core.getipython import get_ipython

lgn = Lightning(ipython=True, host='http://public.lightning-viz.org')
print(lgn)
values = random.rand(100)
print(values)

# lgn.histogram(values, 10, zoom=False)