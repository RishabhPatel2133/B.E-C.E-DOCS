#1st line chart
from django.forms import inlineformset_factory
import matplotlib.pyplot as plt
value = [5,8,9,4,1,6,7,2,3,8]
plt.plot(range(1,11),value,c='b',lw=2,ls="--",marker='>')
#to save we use plt.savefig('figname.filetype',format='filetype')
plt.show()


#2nd pie chart
#import matplotlib.pyplot as plt
#%matplotlib notebook
value=[1,3,4,5] 
l=['car','books','cloth','shoes'] #labels
c=['r','b','g','y'] # colors
e=[0,0.4,0,0,] #explode - distans from the chart
plt.pie(value,labels=l,colors=c,explode=e)
plt.show()

#3rd bar chart
#import matplotlib.pyplotas plt
#%matplotlib notebook
x=[1,2,3,4] #x-axies
y=[2.2,3.3,2.5,5.5] #y-axies
l=['1st','2nd','3rd','4th'] #label
w=[0.2,0.5,0.3,0.7] #widht
c=['b','g','y','r'] #colors
plt.title('random bar chart') #to give a title to chart
plt.bar(x,y,color=c,label=l,width=w)
plt.show()

#4th histogram chart
#import matplotlib.pyplot
import numpy as np
#%matplotlib notebook
clips= np.random.randint(0,10,100)
plt.hist(clips,bins=10,histtype='stepfilled',align='mid',label='clips hist')
plt.show()

'''line chart
    import matplotlib.pyplot as plt
    %matplotlib inline
    value=[10,20,30,40]
    plt.plot(random(0,10),value,c='b',marker='0',ls='--',lw='4')
    plt.show()'''

'''pie chart
    import matplotlib.pyplot as plt
    %matplotlib notebook
    value=[10,20,30,40]
    l=['books','author','price','parts']
    c=['b','r','y','g']
    e=[0,0.5,0,0.2]
    plt.pie(value,colors=c,labels=l,expode=e)
    plt.show()'''

'''bar chart
    import matplotlib.pyplot as plt
    %matplotlib notebook
    x=[2,3,4,5]
    y=[2,4,2,3]
    c=['b','y','g','r']
    w=[0.2,0.4,0.3,0.2]
    l=['1st','2nd','3rd','4th']
    plt.bar(x,y,label=l,color=c,width=w)
    plt.show()'''