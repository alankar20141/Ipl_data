import requests
from bs4 import BeautifulSoup


r=requests.get('http://www.cricbuzz.com/cricket-series/2115/indian-premier-league-2012/matches')
course_list=[]

soup = BeautifulSoup(r.content)

print(soup.prettify())
ff=[]
gg=[]
hh=[]
jj=[]

g_data1=soup.find_all("div",{"class":"cb-col-100 cb-col cb-srs-gray-strip"})
for item in g_data1:
    print item.contents[0].text
    print item.contents[1].text
    print item.contents[2].text
                       
g_data1=soup.find_all("div",{"class":"cb-col-60 cb-col cb-srs-mtchs-tm"})
for item in g_data1:
    #x=item.contents[-1].text
    y= item.contents[0].text
    z= item.contents[1].text
    a= item.contents[2].text
    print y
    print z
    print a
    #course=[y,z,a]
    jj.append(z)
    course_list.append([y,z,a])
    #print course_list
    #print y
    #print z
    #print a
    
    m,n=y.split(',')
    #print m
    #print n
    aa,bb=m.split('vs')
    ff.append(aa)
    gg.append(bb)
    #print ff
    #print gg
    str1='won'
    if str1 in a:
        q,w=a.split('won')
        hh.append(q)
    else:
        hh.append(a)
   
import pandas as pd
df=pd.DataFrame(ff,columns=["first_team"])
df['second_team']=gg
df['stadium']=jj
df['winner']=hh
print df
    

import pandas as pd
#df=pd.read_csv('aa.csv')
#file_name=aa.csv
#df.to_csv(file_name, sep='\t')

df.to_csv("ipl_2012.csv",index=False)
