# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:32:55 2019

@author: Administrator
"""

from treelib import node, Tree

ram_my = Tree()
ram_my.create_node("n1",1)
ram_my.create_node("n2",2,parent=1)

ram_my.create_node("n3",3, parent=2)
ram_my.create_node("n4",4, parent=3)
ram_my.create_node("n5",5, parent=4)
ram_my.show()