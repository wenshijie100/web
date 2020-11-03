# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:43:04 2020

@author: wensh
"""

import time 
 
class node(object):
    def __init__(self,number,lable):
        self.next = {}       
        self.fail = None     
        self.isWord = False  
        self.word = ""      
        self.num=number
        self.lb=lable
 
counts = {}
a=1
ct=0
l=[chr(i) for i in range(48,58)]+[chr(i) for i in range(97,123)]+[chr(i) for i in range(65,91)]
class ac_automation(object):
 
    def __init__(self, user_dict_path):
        self.root = node('@',1)
        self.user_dict_path = user_dict_path
        self.c=0
 
    def add(self, word):
        global a
        #self.root.next['@']=self.root
        self.c=self.c+1
        #if len(word) <=2 or self.c>5000:
            #return
        temp_root = self.root
        for char in word:
            if char not in temp_root.next:
                a=a+1
                temp_root.next[char] = node(char,a)
            temp_root = temp_root.next[char]
            #temp_root.next['@']=self.root
            print(temp_root.lb)
        temp_root.isWord = True
        temp_root.word = word
        
    def addword(self, word):
        global a
        temp_root = self.root
        for char in word:
            if char not in temp_root.next:
                a=a+1
                temp_root.next[char] = node(char,a)
            temp_root = temp_root.next[char]
        temp_root.isWord = True
        temp_root.word = word 
 
 
    def add_keyword(self):
        #print("test")
        #self.add('abc')
        #self.add('aaa')
        #return
        cnt=0
       
        for line in l:
            #print(line)
            cnt=cnt+1
            self.addword(line)
        print(cnt)
 
    def make_fail(self):
        global l
        temp_que = []
        #temp_que.append(self.root)
        temp=self.root
        self.root.fail=self.root
        for key in (l):
            if not temp.next.get(key):
                temp.next[key]=self.root
            else :
                temp.next[key].fail=self.root
                temp_que.append(temp.next[key])
        while len(temp_que) != 0:
            temp = temp_que.pop(0)
            p = None
            for key in  (l):
                if not temp.next.get(key):
                    temp.next[key]=temp.fail.next[key]
                else :
                    temp.next[key].fail=temp.fail.next[key]
                    temp_que.append(temp.next[key])
                
    def search(self, content):
        p = self.root
        result = set()
        index = 0
        currentposition = 0
        while currentposition < len(content):
            word = content[currentposition]
            while True:
                #print("T:",p.num,word in p.next)
                if  p == self.root:
                    break
                if  word in p.next:
                    break
                if p.fail:
                    p = p.fail
                else :
                    p=self.root
            #print("A:",currentposition,p.num,word)    

            if word in p.next:
                #print("GREAT")
                p = p.next[word]
            else:
                p = self.root
            t=p
            #print("B",currentposition,p.num,word)
            while t!=self.root:
                if t.isWord:
                   # print("find it%s"%p.word)
                    end_index = currentposition + 1
                    result.add((t.word, end_index - len(t.word), end_index))
                  
                   #print("find it:%s",p.word)
                    counts[t.word]=counts.get(t.word,0)+1
                    #print(content,t.word)
                if t.fail:
                    t = t.fail
                else :
                    t =self.root
                    #break
            currentposition += 1
        return result
path='C:\\Users\\wensh.LAPTOP-GCSCJA7R\\Desktop\\web\\wenshijie\\拼音\\'
ac = ac_automation(user_dict_path="word2.txt")
ac.add_keyword()  
ac.make_fail()
with open('yahoo_alpha.txt', 'w') as f2:
    with open("yahoo_input.txt","rb") as f:
        cnt2,cnt3=0,0
        ss = time.time()
        for sw in f.readlines():
            
            #s = sw[2:-1]
            s = sw.decode(encoding = "utf-8")  
            s=s.strip()
        
            t="".join(filter(str.isalpha,s))
            #print(t)
            if(len(t)>1):
                cnt2=cnt2+1
            #print(t)
            #print(s)
            res = ac.search(t)
        item=list(counts.items())
        item.sort(key=lambda x:x[1],reverse=True)
        print(cnt2)
        cnt=0;
    
        for i in range(len(item)):
            word,count = item[i]
            #if(len(word)<3):
                #continue
            #print(word,count)
            #tmp="  ".join(word,count)
            f2.write(word)
            f2.write("  ")
            f2.write(str(count))
            f2.write("\n")
            #f2.write("123abc")
            cnt=cnt+1
            #if cnt > 100:
                #break
print("TIME:  {0} ms!".format(round(1000 * (time.time() - ss), 3)))
    