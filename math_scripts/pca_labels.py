from mpl_toolkits.mplot3d import Axes3D


import matplotlib.pyplot as plt



fig = plt.figure(figsize=(10,10))
plt.gca()
ax = fig.add_subplot(111, projection='3d')

p = pca.components_
centroid = pca.mean_
segments = np.arange(-40, 40)[:, np.newaxis] * p


x =[1, 6, 11, 7]
y =[0, 14, 28, 21]
z =[.5, 3, 5.5, 3.5]


fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c='r', marker='o')
#ax.plot(pca.components_[:,0]*10,pca.components_[:,1]*10,pca.components_[:,2]*10 )
#ax.scatter(pca.components_[0][0]*100, pca.components_[0][1]*100, pca.components_[0][2]*100)
ax.plot(*(centroid + segments).T, color="red")

for i in range(X.shape[0]): #plot each point + it's index as text above
 #ax.scatter(m[i,0],m[i,1],m[i,2],color='b')
 ax.text(X[i][0], X[i][1] ,X[i][2],  '%s' % (str(i+1)), size=20, zorder=1,
 color='k')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
