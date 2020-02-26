#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:42:19 2020

@author: tuhinpoddar
"""

# Paste your function here
def applyF_filterG(L, f, g):
    tempL = L[:]
    for i in tempL:
        if not g(f(i)):
            L.remove(i)
    if len(L) > 0:  
        return max(L)
    else:
        return -1
        