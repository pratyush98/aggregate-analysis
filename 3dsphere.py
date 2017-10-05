from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")

# draw cube
inp=raw_input('enter l1')
y1=int(inp)
inp=raw_input('enter l2')
y2=int(inp)
inp=raw_input('enter l3')
y3=int(inp)
l1= [-y1, y1]
l2= [-y2,y2]
l3= [-y3,y3]
for s, e in combinations(np.array(list(product(l1, l2, l3))), 2):
    if np.sum(np.abs(s-e)) == l1[1]-l1[0] or np.sum(np.abs(s-e)) == l2[1]-l2[0] or np.sum(np.abs(s-e)) == l3[1]-l3[0]:
        ax.plot3D(*zip(s, e), color="b")

# draw sphere
'''u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(200*x, 200*y, 200*z, color="r")'''
from numpy import random
x_=[]
y_=[]
z_=[]
r_=[]
radu=[20,10,5,2]
allarea=[5,10,10,10]
var=1
ctr=0
area=0
for i in range(0,10000,1):
 if (area>(allarea[ctr]/100.0)*y1*y2*y3*8):
  ctr = ctr + 1
  area = 0
 if ctr==4:
    break
 while(var==1):
  x=random.randint(-y1,y1,1)
  y=random.randint(-y2,y2,1)
  z=random.randint(-y3,y3,1)
  c=0

  if x_.__sizeof__()!=0:
   for a, b , c ,rad in zip(x_, y_,z_, r_):
    if ((x-a)*(x-a)+(y-b)*(y-b)+(z-c)*(z-c)<(rad+radu[ctr])**2)or((x>y1-radu[ctr])or(x<-y1+radu[ctr])or(y>y2-radu[ctr])or(y<-y2+radu[ctr])or(z>y3-radu[ctr])or(z<-y3+radu[ctr])):
       c=1
       break

  if x_.__sizeof__()==0:
    u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
    xr = np.cos(u) * np.sin(v)
    yr = np.sin(u) * np.sin(v)
    zr = np.cos(v)
    if(ctr==0):
     ax.plot_wireframe(radu[ctr]* xr+x,radu[ctr]* yr+y,radu[ctr]*zr+z, color="r")
    if(ctr == 1):
     ax.plot_wireframe(radu[ctr] * xr + x, radu[ctr] * yr + y, radu[ctr] * zr + z, color="g")
    if(ctr == 2):
     ax.plot_wireframe(radu[ctr] * xr + x, radu[ctr] * yr + y, radu[ctr] * zr + z, color="b")
    if(ctr == 3):
     ax.plot_wireframe(radu[ctr] * xr + x, radu[ctr] * yr + y, radu[ctr] * zr + z, color="y")
    x_.append(x)
    y_.append(y)
    z_.append(z)
    r_.append(radu[ctr])
    area=area+4.1887*radu[ctr]*radu[ctr]*radu[ctr]
    print ctr
    break
  if c==0:
    u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
    xr = np.cos(u) * np.sin(v)
    yr = np.sin(u) * np.sin(v)
    zr = np.cos(v)
    if (ctr == 0):
        ax.plot_wireframe(radu[ctr] * xr + x, radu[ctr] * yr + y, radu[ctr] * zr + z, color="r")
    if (ctr == 1):
        ax.plot_wireframe(radu[ctr] * xr + x, radu[ctr] * yr + y, radu[ctr] * zr + z, color="g")
    if (ctr == 2):
        ax.plot_wireframe(radu[ctr] * xr + x, radu[ctr] * yr + y, radu[ctr] * zr + z, color="b")
    if (ctr == 3):
        ax.plot_wireframe(radu[ctr] * xr + x, radu[ctr] * y1 + y, radu[ctr] * zr + z, color="y")
    x_.append(x)
    y_.append(y)
    z_.append(z)
    r_.append(radu[ctr])
    area = area + 4.1887 * radu[ctr] * radu[ctr] * radu[ctr]
    break

plt.show()
print x_.__len__()
# draw a point
'''ax.scatter([0], [0], [0], color="g", s=100)

# draw a vector
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


class Arrow3D(FancyArrowPatch):

    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

a = Arrow3D([0, 1], [0, 1], [0, 1], mutation_scale=20,
            lw=1, arrowstyle="-|>", color="k")
ax.add_artist(a)'''