#! /usr/bin/env python
"""
Date: 8-23-2021
Twitter Link: https://twitter.com/labeveryday/status/1429469481559117826?s=20
Results: https://www.youtube.com/watch?v=rtR0B8npE4g
-----------------------------------------------------------------------------

Python quiz question for the day?

bills = ["house", "car", "phone", "onlyfans"]

for bill in range(len(bills)):
    print(bill)

If we execute this code, which bill will print?

#LabEverydayDailyPythonQuiz

A.All items
B. None
C. onlyfans
D. TypeError

"""

# Assign list of strings data types to the bills variable
bills = ["house", "car", "phone", "onlyfans"]

# 1. Use len() to convert bills into and int
# 2. Use the range() to iterate n number of times
# 3. Through each iteration print bill
for bill in range(len(bills)):
    print(bill)
