import numpy as np
import matplotlib.pyplot as plt
import math
import copy

# Data for a three-dimensional line
number_of_planets=2
number_of_lines=50
no_points=1000
zline = [0]*no_points
xline = [0]*no_points
yline = [0]*no_points

m = [1]*number_of_planets
size_planets=[]
for m_ in m:
    size_planets.append(m_*100)

kleur=['limegreen','brown']

dt=0.001
plot_interval=2000

def calculate_mass(x_p,y_p):
    mass=0
    for i in range(number_of_planets):
        mass=mass+m[i]*(1/(1+(x_p-x[i])**2+(y_p-y[i])**2))
    return -mass


x = [int(no_points/2)]*number_of_planets
y = [int(no_points/2)]*number_of_planets
vx = [0]*number_of_planets
vy = [0]*number_of_planets
fx = [0]*number_of_planets
fy = [0]*number_of_planets
m = [1]*number_of_planets
z = [0]*number_of_planets
m [0]= 10
m [1]= 9
x[0]=x[0]-100
x[1]=x[1]+100
vy[1]=0.10
vy[0]=-vy[1]*0.9    

x_past=[[],[]]
y_past=[[],[]]

for t in range (plot_interval*3600):    
    for i in range (number_of_planets):
        fx[i]=0
        fy[i]=0
        ftotal=0
        for j in range (number_of_planets):
            if i==j:
                pass
            else:
                distance_squared= (x[i]-x[j])**2+(y[i]-y[j])**2
                # standard Newton gravity formula
                ftotal=m[i]*m[j]/(distance_squared)
                fx[i]=fx[i]+ftotal*(x[j]-x[i])/math.sqrt(distance_squared)
                fy[i]=fy[i]+ftotal*(y[j]-y[i])/math.sqrt(distance_squared)
    for i in range (number_of_planets):
        vx[i]=vx[i]+fx[i]/m[i]*dt
        vy[i]=vy[i]+fy[i]/m[i]*dt
        total=vx[i]**2+vy[i]**2
        # The following part mimics the energy loss due to emmitting of waves. I assume it is sort of linear with the speed
        vx[i]=vx[i]*(1000000-total)/1000000  
        vy[i]=vy[i]*(1000000-total)/1000000
        #print(total)
        x[i]=x[i]+vx[i]*dt
        y[i]=y[i]+vy[i]*dt

    if t%plot_interval==0:
        for i in range (number_of_planets):
            x_past[i].append(x[i])
            y_past[i].append(y[i])
    if t%(plot_interval*100)==0:
        plt.figure(figsize=(20,20))
        plt.scatter(x_past,y_past)
        plt.xlim(400,600)
        plt.ylim(400,600)
        plt.show()
        print (t/(plot_interval*100))
        

print ('lengte',len (x_past[0]))        
'''
while (len (x_past[0])>800):
    x_past[0].pop(0)
    y_past[0].pop(0)
    x_past[1].pop(0)
    y_past[1].pop(0)
'''
plt.figure(figsize=(20,20))
plt.scatter(x_past,y_past)
plt.xlim(400,600)
plt.ylim(400,600)
plt.show()
 
o_x=copy.deepcopy(x_past)
o_y=copy.deepcopy(y_past)

for t in range(len (o_x[0])-770):
    x_past=[o_x[0][0:770],o_x[1][0:770]]    
    y_past=[o_y[0][0:770],o_y[1][0:770]]    
    x_p=[0]*1000*1000
    y_p=[0]*1000*1000
    z_p=[0]*1000*1000
    for i in range (1000):
        for k in range (1000):
            x_p[k+i*1000]=i
            y_p[k+i*1000]=k 
    
    for q in range(len (x_past[0])-1):
        j=q#int(800.0*q/len(x_past[0]))
        for x_walk in range (-int(j),int(j)+1):
            y_walk=int(math.sqrt(j**2-x_walk**2))
            for i in range (number_of_planets):
                kx1=x_walk+x_past[i][len(x_past[0])-1-q]
                ky1=int(y_past[i][len(x_past[0])-1-q])+y_walk
                ky2=int(y_past[i][len(x_past[0])-1-q])-y_walk
                if (kx1>0) and (kx1<1000) and (ky1>0) and (ky1<1000):
                    z_p[int(kx1+(ky1)*1000)]+=1000000/((j+100)**2)
                if (kx1>0) and (kx1<1000) and (ky2>0) and (ky2<1000):
                    z_p[int(kx1+(ky2)*1000)]+=1000000/((j+100)**2)
        for y_walk in range (-int(j),int(j)+1):
            x_walk=int(math.sqrt(j**2-y_walk**2))
            for i in range (number_of_planets):
                kx1=x_walk+x_past[i][len(x_past[0])-1-q]
                kx2=-x_walk+x_past[i][len(x_past[0])-1-q]
                ky1=int(y_past[i][len(x_past[0])-1-q])+y_walk
                if (kx1>0) and (kx1<1000) and (ky1>0) and (ky1<1000):
                    z_p[int(kx1+(ky1)*1000)]+=1000000/((j+100)**2)
                if (kx2>0) and (kx2<1000) and (ky1>0) and (ky1<1000):
                    z_p[int(kx2+(ky1)*1000)]+=1000000/((j+100)**2)
    
    '''
    fig = plt.figure(figsize=(20,20))
    ax = plt.axes(projection='3d')
    ax.plot3D(x_p, y_p, z_p)
    plt.show()
    '''
    print (t)
    
    ''' 
    plt.plot(z_p[500*1000:500*1000+1000])
    plt.show()
    '''  
    x = y = np.linspace(-1, 1, 1000)
    z = np.array([i*i+j*j for j in y for i in x])
    maxz=0
    for i in range (len(z_p)):
        z[i]=z_p[i]
        if z[i]> maxz:
            maxz=z[i]
    #print (maxz)
    maxz=550
    Z = z.reshape(1000, 1000)
    plt.figure(figsize = (20,20))
    plt.axis('off')
    plt.imshow(Z ,vmin=0, vmax=maxz/3)
    plt.savefig ('rotating'+str(10000+t)+'.png',bbox_inches='tight',pad_inches=0)
    plt.show()
    o_x[0].pop(0)
    o_x[1].pop(0)
    o_y[0].pop(0)
    o_y[1].pop(0)
