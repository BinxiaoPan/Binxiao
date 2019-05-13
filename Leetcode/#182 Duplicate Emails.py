# -*- coding: utf-8 -*-
"""
Created on Mon May 13 00:10:04 2019

@author: binxi
"""

# Write your MySQL query statement below
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*)>1