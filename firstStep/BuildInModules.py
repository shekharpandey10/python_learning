"""
Build-in-Modules
"""

from math import sqrt
from datetime import datetime
from random import randint
import requests
print(datetime.now())
print(sqrt(25))
print(randint(1,100))
r=requests.get('https://www.google.com')
print(r.text)