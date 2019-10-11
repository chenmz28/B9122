#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:59:02 2019

@author: cqy
"""

#Question 1
def EMI(rate: float, N: int, PV: int, FV: int):
       emi=(PV+FV/((1+rate)**N))*rate*((1+rate)**N)/((1+rate)**N-1)
       print(emi)

EMI(0.05,30,10000,2000)

#Question 2
f=open("question4.txt", "r")
content=f.read()
words=content.split()  
lower=[]
for i in words:
    lower.append(i.lower())

dict={i:lower.count(i) for i in lower}

sorted_d=sorted(dict.items(), key= lambda x: x[1],reverse=True)

tuple_strings = ['(%s, %s)' % tuple for tuple in sorted_d]

result = '\n '.join(tuple_strings)

out=open("out.txt","w+")
for i in tuple_strings:
    j=i.replace("(","")
    k=j.replace(")","")
    out.write(k)
    out.write("\n")