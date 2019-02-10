import matplotlib.pyplot as plt
import numpy as np
d='Philosophy'
with open("text1.txt") as f1:
    a=f1.read()
c=a.split()
 
yaxis=[]
xaxis=["text1","text2","text3"]
for i in c:
        count1=c.count(d)
yaxis.append(count1)
with open("text2.txt") as f2:
    b=f2.read()
e=b.split()
 

for i in e:
        count2=e.count(d)
yaxis.append(count2)
with open("text3.txt") as f3:
    f=f3.read()
g=f.split()
 
for i in g:
        count3=g.count(d)
yaxis.append(count3)
index = np.arange(len(xaxis))
plt.bar(index, yaxis)
plt.xlabel('text', fontsize=5)
plt.ylabel('frequency', fontsize=5)
plt.xticks(index, xaxis, fontsize=5, rotation=30)
plt.title('string search')
plt.show()