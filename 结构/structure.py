# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:23:50 2020

@author: wensh
"""

with open("yahoo_input.txt","rb") as f:
    cnt,cnt1,cnt2,cnt3=0,0,0,0
    cntA,cntN=0,0
    for sw in f.readlines():
        s = sw.decode(encoding = "utf-8")
        s=s.strip()
        s=str(s)
        if len(s)<1:
            continue
        cnt=cnt+1
        a="".join(filter(str.isdigit,s))
        b="".join(filter(str.isalpha,s))
        c="".join(filter(str.isalnum,s))
      
        if c==s:
            cnt3=cnt3+1
        if a==s:
            cnt1=cnt1+1
            continue
        if b==s:
            cnt2=cnt2+1
            continue
        AANN=b+a
        NNAA=a+b
        if AANN==s:
            cntA=cntA+1
        if NNAA==s:
            cntN=cntN+1
print(cnt,cnt1,cnt2,cnt3,cnt-cnt3,cntA,cntN)
print(cnt,cnt1/cnt,cnt2/cnt,cnt3/cnt,(cnt-cnt3)/cnt,cntA/cnt,cntN/cnt)            