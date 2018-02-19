import pandas as pd

df1=pd.read_csv('ipl_2008.csv')
df2=pd.read_csv('ipl_2009.csv')
df3=pd.read_csv('ipl_2010.csv')
df4=pd.read_csv('ipl_2011.csv')
df5=pd.read_csv('ipl_2012.csv')
df6=pd.read_csv('ipl_2013.csv')
df7=pd.read_csv('ipl_2014.csv')
df8=pd.read_csv('ipl_2015.csv')
df9=pd.read_csv('ipl_2016.csv')
df10=pd.read_csv('ipl_2017.csv')



x=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10],axis=0)
kk=pd.DataFrame(x)

kk.to_csv("ipl_c.csv",index=False)
