import numpy as np

array_0 = np.array([[0,0,0,0.3,0.8,0.6,0.7,0.9,0.9,0.4,1],
           [0.1,0,0,0,0,0,0.1,0.1,0.1,0.2,1],
           [0,0.1,0,0,0,0.2,0.2,0.3,0.4,0,1],
           [0,0,0,0,0,0,0,0,0,0,1],
           [0,0,0.2,0,0,0,0.3,0,0.3,0.3,1],
           [0,0,0,0,0,0,0,0,0,0,1],
           [0,0,0,0,0,0,0,0,0,0,1],
           [0,0,0,0,0,0,0,0,0,0,1],
           [0,0,0,0,0,0,0,0,0,0,1],
           [0.2,0,0,0,0.3,0.2,0.2,0.2,0.4,0,1],
           [0,0,0,0,0,0,0,0,0,0,0]])


for i in range(0,10):  # replace values which == 0 to infinity(it it step according to the classic Floid )
    for j in range(0,10):
        if array_0[i][j] == 0:
            array_0[i][j] = float('inf')

# print(array_0)

array_min = np.zeros((11,11)) ## create empty matrix for min values


for m in range(1,11): ## calculate for each matrix
    for u in range(0,11):
        if u == 0:
            for v in range(0,11):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]),array_0[u][v])
        if u == 1:
            for v in range(0,11):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]),array_0[u][v])
        if u == 2:
            for v in range(0,11):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]),array_0[u][v])
        if u == 3:
            for v in range(0,11):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]),array_0[u][v])
        if u == 4:
            for v in range(0,11):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]),array_0[u][v])
        if u == 5:
            for v in range(0,11):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]),array_0[u][v])
        if u == 6:
            for v in range(0,11):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]),array_0[u][v])
        if u == 7:
            for v in range(0,11):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]),array_0[u][v])
        if u == 8:
            for v in range(0,11):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]),array_0[u][v])
        if u == 9:
            for v in range(0,11):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]),array_0[u][v])
        if u == 10:
            for v in range(0,11):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]),array_0[u][v])
                if array_min[u][v] == 0:       ## it is just according that the latest row with all infinity values doesn't show as infinity
                    array_min[u][v] = float('inf')


min_value = np.min(array_min)  ## show the value of minimum element
print(f"the minimum value is {min_value}")

# find indexes where min value to estimate which factors have the minimum influence on the fires
for i in range(0,11):
    for j in range(0,11):
        if array_min[i][j] == min_value:
            print(f"the element in matrix is {i}{j}")












