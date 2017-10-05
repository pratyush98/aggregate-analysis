import matplotlib.pyplot as plt
import matplotlib.patches
from matplotlib.pyplot import Figure, subplot
from numpy import random
fig=plt.figure(1)
plt.axis([0,400,0,400])
ax=fig.add_subplot(1,1,1)
x_=[]
y_=[]
r_=[]
radu=[20,10,5,2]
allarea=[5,10,10,10]
var=1
ctr=0
area=0
for i in range(0,10000,1):

 while(var==1):
  x=random.randint(0,400,1)
  y=random.randint(0,400,1)
  c=0

  if x_.__sizeof__()!=0:
   for a, b ,rad in zip(x_, y_, r_):
    if ((x-a)*(x-a)+(y-b)*(y-b)<(rad+radu[ctr])**2)or((x>400-radu[ctr])or(x<radu[ctr])or(y>400-radu[ctr])or(y<radu[ctr])):
       c=1
       break

  if x_.__sizeof__()==0:
    circ = plt.Circle((x, y), radius=radu[ctr], color=str(ctr*0.1), fill=True)
    x_.append(x)
    y_.append(y)
    r_.append(radu[ctr])
    area=area+3.14*radu[ctr]*radu[ctr]
    print ctr
    break
  if c==0:

       circ=plt.Circle((x,y), radius=radu[ctr], color=str(ctr*0.1), fill=True)
       x_.append(x)
       y_.append(y)
       r_.append(radu[ctr])
       ax.add_patch(circ)
       area = area + 3.14 * radu[ctr] * radu[ctr]
       print area
       break
 if area > allarea[ctr] / 100.0 * 400 * 400:
  ctr = ctr + 1
  area = 0
 if ctr==4:
   break

plt.show()
print x_.__len__()