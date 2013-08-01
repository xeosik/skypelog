#!/usr/bin/env python
from skypelog import *
data = SkypeDBB("/home/user/.Skype/account/call256.dbb")
    for r in data.records():
        print r
      
