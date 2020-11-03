# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 19:32:11 2020

@author: wensh
"""
import time
with open('C:\\Users\\wensh.LAPTOP-GCSCJA7R\\Desktop\\web\\pinyin2.txt', 'w') as f2:
    with open("C:\\Users\\wensh.LAPTOP-GCSCJA7R\\Desktop\\web\\pinyin.txt","rb") as f:
        cnt1,cnt2=0,0
        ss = time.time()
        for sw in f.readlines():
            cnt1=cnt1+1
            if cnt1%2==0:
                continue
            s = sw.decode(encoding = "utf-8")  
            s=s.strip()
            #print(s)
            t=s.split()
            t.pop(len(t)-1)
            t.pop(0)
            #print(str(t))
            u="\n".join([str(t[i]) for i in range(0, len(t))])
            #print(u)
            f2.write(u)
            f2.write("\n")