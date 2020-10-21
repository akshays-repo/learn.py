#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:19:52 2020

@author: akshays
"""
from datetime import date

def server_cost(d1, m1, y1, d2, m2, y2):
    created_day = date(y1, m1, d1)
    deleted_day = date(y2, m2, d2)
    differnce_in_day  =  deleted_day - created_day
    day = differnce_in_day.days
    
    if created_day == deleted_day:
        return 20
    if (day > 1 & day <= 31) & (m1 == m2):
        return 30 * day
    if (day > 31 & day <= 365) & (y1 == y2):
        return 1000 * day
    else:
        return 2000

if __name__ == '__main__':
    d1M1Y1 = input().split()
    d1 = int(d1M1Y1[0])
    m1 = int(d1M1Y1[1])
    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()
    d2 = int(d2M2Y2[0])
    m2 = int(d2M2Y2[1])
    y2 = int(d2M2Y2[2])

    result = server_cost(d1, m1, y1, d2, m2, y2)
    print(str(result) + '\n')