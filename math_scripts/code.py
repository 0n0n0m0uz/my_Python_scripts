# Creates matrix of coords based on the size of both inputs. 
# For ex the 1st input of meshgrid() above is 1 x 6 and the 2nd is 1 x 4 
# which means we are making a grid of 6 xcoords and 4 ycoords

np.meshgrid(np.arange(1, 13, 2), np.arange(-15, -3, 3))

[array([[ 1,  3,  5,  7,  9, 11],
        [ 1,  3,  5,  7,  9, 11],
        [ 1,  3,  5,  7,  9, 11],
        [ 1,  3,  5,  7,  9, 11]]),
 array([[-15, -15, -15, -15, -15, -15],
        [-12, -12, -12, -12, -12, -12],
        [ -9,  -9,  -9,  -9,  -9,  -9],
        [ -6,  -6,  -6,  -6,  -6,  -6]])]

x.ravel()

array([ 1,  3,  5,  7,  9, 11,  1,  3,  5,  7,  9, 11,  1,  3,  5,  7,  9,
       11,  1,  3,  5,  7,  9, 11])

# Create Individual Tuples for each point in an array



coords = [(a, b) for a, b in zip(x.ravel(), y.ravel())]
XYpairs = np.dstack([XX, YY]).reshape(-1, 2)`       
np.vstack([XX.ravel(), YY.ravel()]).T

# For 3D points
data = np.concatenate((x[:, np.newaxis], y[:, np.newaxis], z[:, np.newaxis]),
                      axis=1)

 
[(1, -15),
 (3, -15),
 (5, -15),
 (7, -15),
 (9, -15),
 (11, -15),
 (1, -12),
 (3, -12),
 (5, -12),
 (7, -12),
 (9, -12),
 (11, -12),
 (1, -9),
 (3, -9),
 (5, -9),
 (7, -9),
 (9, -9),
 (11, -9),
 (1, -6),
 (3, -6),
 (5, -6),
 (7, -6),
 (9, -6),
 (11, -6)]

# To get array for each axis
XYpairs = np.vstack([ x.reshape(-1), y.reshape(-1) ])[0]


array([ 1,  3,  5,  7,  9, 11,  1,  3,  5,  7,  9, 11,  1,  3,  5,  7,  9,
       11,  1,  3,  5,  7,  9, 11])