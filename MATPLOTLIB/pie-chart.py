# Matplotlib prgm3:  creating pie chart
import matplotlib.pyplot as plt
l='Java','Python','PHP','JavaScript','C#','C++'
p=[22.2,17.6,8.8,8,7.7,6.7]
c=["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b"]
e=(0.1,0,0,0,0,0)
plt.pie(p,explode=e,labels=l,colors=c,autopct='%1.1f%%',
        shadow=True,startangle=140)
plt.axis('Equal')
plt.show()
    
