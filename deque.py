# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:27:18 2019

@author: Administrator
"""
from collections import deque
ram = deque(["ravi","raju","muna","jitendra"])
print (ram)
ram.append("deep")
print(ram)
ram.append("jagan")
print(ram)
print (ram.popleft())
print(ram)