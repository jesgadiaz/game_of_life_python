import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import copy 

#random.seed(4)

# Set grid size
n = 50  # height
m = 50   # width
g = 100  # number of photograms

grid = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(random.randint(0,1))
    grid.append(temp)


def getNumberOfNeighbors(i,j):
    counter = 0
    if i != 0 and j != 0 and i != n-1 and j!= m-1:
        counter =   grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] \
                  + grid[i][j-1]   + grid[i][j+1] \
                  + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
    else:
        if i == 0 and j != 0 and j != m-1:
            counter =   grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]\
                      + grid[i][j-1] + grid[i][j+1]\
                      + grid[n-1][j-1] + grid[n-1][j] + grid[n-1][j+1]
        elif i == n-1 and j != 0 and j != m-1:
            counter =   grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]\
                      + grid[i][j-1] + grid[i][j+1]\
                      + grid[0][j-1] + grid[0][j] + grid[0][j+1]
        elif j == 0 and i != 0 and i != n-1:
            counter =   grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1]\
                      + grid[i-1][j] + grid[i+1][j]\
                      + grid[i-1][m-1] + grid[i][m-1] + grid[i+1][m-1]
        elif j == m-1 and i != 0 and i != n-1:
            counter =   grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1]\
                      + grid[i-1][j] + grid[i+1][j]\
                      + grid[i-1][0] + grid[i][0] + grid[i+1][0]
        elif i == 0 and j == 0:
            counter =   grid[0][1] + grid[1][0] + grid[1][1]\
                      + grid[n-1][0] + grid[n-1][1] \
                      + grid[0][m-1] + grid[1][m-1] \
                      + grid[n-1][m-1]
        elif i == n-1 and j == 0:
            counter =   grid[n-2][0] + grid[n-2][1] + grid[n-1][1]\
                      + grid[0][0] + grid[0][1] \
                      + grid[n-1][m-1] + grid[n-2][m-1] \
                      + grid[0][m-1]
        elif i == 0 and j == m-1:
            counter =   grid[0][m-2] + grid[1][m-2] + grid[1][m-1]\
                      + grid[0][0] + grid[1][0] \
                      + grid[n-1][m-1] + grid[n-1][m-2] \
                      + grid[n-1][0]
        elif i == n-1 and j == m-1:
            counter =   grid[n-1][m-2] + grid[n-2][m-2] + grid[n-2][m-1]\
                      + grid[0][m-2] + grid[0][m-1] \
                      + grid[n-1][0] + grid[n-2][0] \
                      + grid[0][0]
    return counter
            

states = []
states.append(copy.deepcopy(grid))

new_grid = copy.deepcopy(grid)

for k in range(g):
    for i in range(n):
        for j in range(m):
            n_neighbors = getNumberOfNeighbors(i,j)
            if new_grid[i][j] == 1 and n_neighbors < 2:
                new_grid[i][j] = 0
            if new_grid[i][j] == 1 and (n_neighbors == 2 or n_neighbors == 3):
                new_grid[i][j] = 1
            if new_grid[i][j] == 1 and n_neighbors > 3:
                new_grid[i][j] = 0
            if new_grid[i][j] == 0 and n_neighbors == 3:
                new_grid[i][j] = 1
    grid = copy.deepcopy(new_grid)
    #print(grid)
    states.append(copy.deepcopy(grid))
    
ims = []
fig = plt.figure()
npa = np.zeros((g+1, n, m))
    
for i in range(g+1):
    npa[i] = np.asarray(states[i])
    im  = plt.imshow(npa[i], cmap = "Greys", vmin=0, vmax=1)
    #plt.show()
    ims.append([im])
    
ani = animation.ArtistAnimation(fig, ims, interval=300, blit=False, repeat_delay=10)
ani.save('gol.mp4', writer='ffmpeg')
