import numpy as np
import matplotlib.pyplot as plt
import math

# Data for a three-dimensional line
number_of_planets=4
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
m [0]= 10
m [1]= 10
x[0]=x[0]-30
x[1]=x[1]+30
x[2]=x[2]-5
x[3]=x[3]+5
y[2]=y[2]
y[3]=y[3]

vy[1]=0.3
vy[0]=-vy[1]
#y[3]=y[3]+5
vy[3]=0.9
vy[2]=-vy[3]
size_planets=[]
for m_ in m:
    size_planets.append(m_*100)

kleur=['limegreen','brown','green','red']

dt=0.001
plot_interval=2500

def calculate_mass(x_p,y_p):
    mass=0
    for i in range(number_of_planets):
        mass=mass+m[i]*(1/(1+(x_p-x[i])**2+(y_p-y[i])**2))
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
        
        fig = plt.figure(figsize=(20,20))
        ax = plt.axes(projection='3d')
        for i in range (number_of_lines+1):
            for k in range (no_points):
                xline[k]=k
                yline[k]=i *(no_points/number_of_lines)
                zline[k]=calculate_mass (xline[k],yline[k])        
            ax.plot3D(xline, yline, zline, 'gray')
        for i in range (number_of_lines+1):
            for k in range (no_points):
                xline[k]=i*(no_points/number_of_lines)
                yline[k]=k
                zline[k]=calculate_mass (xline[k],yline[k])
            ax.scatter3D(x, y, z,s=size_planets,c=kleur);
            ax.plot3D(xline, yline, zline, 'gray')
        '''
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])
        ax.set_xticks([]) 
        ax.set_yticks([]) 
        ax.set_zticks([])
        plt.figure(frameon=False)
        '''
        ax.set_xlim(10, 190)
        ax.set_ylim(10, 190)
        ax.set_zlim(-1, 0)
        plt.axis('off')
        plt.savefig('plot'+str(10000+int(t/plot_interval))+'.png',bbox_inches='tight',pad_inches=0)
        plt.show()
        print (t)
        if (t/plot_interval)>20000:
            break

