# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:37:08 2020

@author: wensh
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:02:00 2020

@author: wensh
"""
from math import log
import time
path="C:\\Users\\wensh.LAPTOP-GCSCJA7R\\Desktop\\web\\"
words = open("pinyin2.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

counts = {}
def infer_spaces(s):
    
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    out = []
    i = len(s)
    if(cost[i]<9e999):
        while i>0:
            c,k = best_match(i)
            assert c == cost[i]
            out.append(s[i-k:i])
            word=s[i-k:i]
            
            counts[word] = counts.get(word,0)+1
            #print(counts)
    
            i -= k
    return " ".join(reversed(out))
with open("csdn_ouput_DP.txt","w") as f2:
    with open("csdn_input.txt","rb") as f:
        cnt2,cnt3=0,0
        ss = time.time()
        c=0
        for sw in f.readlines():
            #s = sw[2:-1]
            c=c+1
            #if c>2000000000:
                #break
            s = sw.decode(encoding = "utf-8")  
            s=s[:-2]
            #t=s
            t="".join(filter(str.isalpha,s))
            #print(s.encode(encoding = "utf-8"))
            if(len(t)>1):
                cnt2=cnt2+1
            infer_spaces(t)
        items = list(counts.items())
        items.sort(key=lambda x:x[1],reverse=True)
        print(cnt2)
        cnt=0
        for i in range(len(items)):
            word,count = items[i]
            #if(len(word)<3):
                #continue
            #print(word,count)
            f2.write(word)
            f2.write(" ")
            f2.write(str(count))
            f2.write("\n")
            cnt=cnt+1
            #if cnt > 100:
                #break
print("TIME:  {0} ms!".format(round(1000 * (time.time() - ss), 3)))