import numpy as np
import matplotlib.pyplot as plt
import math

# Data for a three-dimensional line
number_of_planets=6
number_of_lines=50
no_points=200
zline = [0]*no_points
xline = [0]*no_points
yline = [0]*no_points
x = [int(no_points/2)]*number_of_planets
y = [int(no_points/2)]*number_of_planets
vx = [0]*number_of_planets
vy = [0]*number_of_planets
fx = [0]*number_of_planets
fy = [0]*number_of_planets
m = [1]*number_of_planets
z = [0]*number_of_planets


m[0]=1.00E+00   # sun
m[1]=2.45E-06   # venus
m[2]=3.00E-06   # aarde
m[3]=3.23E-07   # mars
m[4]=9.54E-04   # jupiter
m[5]=1.66E-07   # jupiter

au=19
x[1]=x[1]+0.72*au
x[2]=x[2]+1*au
x[3]=x[3]+1.52*au
x[4]=x[4]+5.20*au
x[5]=x[5]+0.38*au

vy[1]=0.267
vy[2]=0.227
vy[3]=0.183
vy[4]=0.1
vy[5]=0.363

size_planets=[]
for m_ in m:
    size_planets.append(m_*10000000)
size_planets=[3000,300,300,200,1000,150]

kleur=['yellow','cyan','blue','orange','brown','grey']

dt=0.005
plot_interval=250

def calculate_mass(x_p,y_p):
    mass=0
    for i in range(1,number_of_planets):
        mass=mass+m[i]*(100000/(1+(x_p-x[i])**2+(y_p-y[i])**2))
    return -mass


    
for t in range (23000000):    
    for i in range (number_of_planets):
        fx[i]=0
        fy[i]=0
        ftotal=0
        for j in range (number_of_planets):
            if i==j:
                pass
            else:
                distance_squared= (x[i]-x[j])**2+(y[i]-y[j])**2
                ftotal=m[i]*m[j]/(distance_squared)
                fx[i]=fx[i]+ftotal*(x[j]-x[i])/math.sqrt(distance_squared)
                fy[i]=fy[i]+ftotal*(y[j]-y[i])/math.sqrt(distance_squared)
    for i in range (number_of_planets):
        vx[i]=vx[i]+fx[i]/m[i]*dt
        vy[i]=vy[i]+fy[i]/m[i]*dt
        x[i]=x[i]+vx[i]*dt
        y[i]=y[i]+vy[i]*dt
                
    if t%plot_interval==0:
        #fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,20))
        fig = plt.figure(figsize=(40,20))

        # =============
        # First subplot
        # =============
        # set up the axes for the first plot
        ax1 = fig.add_subplot(1, 2, 1, projection='3d')
        ax2 = fig.add_subplot(1, 2, 2, projection='3d')
        #fig = plt.figure(figsize=(20,40))
        #ax1 = plt.axes(projection='3d')
        #ax2 = plt.axes(projection='3d')
        for i in range (number_of_lines+1):
            for k in range (no_points):
                xline[k]=k
                yline[k]=i *(no_points/number_of_lines)
                zline[k]=calculate_mass (xline[k],yline[k])        
            ax1.plot3D(xline, yline, zline, 'gray')
            ax2.plot3D(xline, yline, zline, 'gray')
        for i in range (number_of_lines+1):
            for k in range (no_points):
                xline[k]=i*(no_points/number_of_lines)
                yline[k]=k
                zline[k]=calculate_mass (xline[k],yline[k])
            ax1.scatter3D(x, y, z,s=size_planets,c=kleur);
            ax1.plot3D(xline, yline, zline, 'gray')
            ax2.scatter3D(x, y, z,s=size_planets,c=kleur);
            ax2.plot3D(xline, yline, zline, 'gray')
        '''
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])
        ax.set_xticks([]) 
        ax.set_yticks([]) 
        ax.set_zticks([])
        plt.figure(frameon=False)
        '''
        ax1.set_xlim(10, 190)
        ax1.set_ylim(10, 190)
        ax1.set_zlim(-1, 0)
        ax2.set_xlim(70, 130)
        ax2.set_ylim(70, 130)
        ax1.set_zlim(-1, 0)
        ax2.set_zlim(-1, 0)
        ax1.axis("off")
        ax2.axis('off')
        plt.savefig('solar'+str(10000+int(t/plot_interval))+'.png',bbox_inches='tight',pad_inches=0)
        plt.show()
        print (t)
        if (t/plot_interval)>20000:
            break

