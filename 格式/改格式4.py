# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:46:53 2020

@author: wensh
"""

import time
with open('C:\\Users\\wensh.LAPTOP-GCSCJA7R\\Desktop\\web\\name2.txt', 'w') as f2:
    with open("C:\\Users\\wensh.LAPTOP-GCSCJA7R\\Desktop\\web\\name.txt","rb") as f:
        cnt1,cnt2=0,0
        ss = time.time()
        for sw in f.readlines():
            cnt1=cnt1+1
            if cnt1%2==0:
                continue
            s = sw.decode(encoding = "utf-8")  
            s=s.strip()
            #print(s)
            t,u=s.capitalize(),s.lower()
            #print(s,t,u)
            #f2.write(t)
            f2.write(s)
            f2.write("\n")
            f2.write(t)
            f2.write("\n")
            f2.write(u)
            f2.write("\n")