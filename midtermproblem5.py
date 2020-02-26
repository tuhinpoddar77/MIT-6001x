#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:10:09 2020

@author: tuhinpoddar
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    fullList = []
    uniList = []
    keyList = []
    tracker = 0
    
    #place all values into a list
    for value in aDict.values():
      fullList.append(value)
    
    #create a unique list of values
    for i in range(len(fullList)):
      tracker = fullList.count(fullList[i])
      if tracker == 1:
        uniList.append(fullList[i])
    
    #create a list of unique keys
    for key, value in aDict.items():
      if value in uniList:
        keyList.append(key)
    
    #sort list
    keyList.sort()
    
    return keyList