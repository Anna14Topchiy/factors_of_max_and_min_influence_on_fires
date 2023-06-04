import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

array_min = np.zeros((10, 10))  ## create empty matrix for min values
array_max = np.zeros((10, 10))  ## create empty matrix for min values
array_0 = np.array([[0, 0, 0.3, 0.8, 0.6, 0.7, 0.9, 0.9, 0.4, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0.2, 0, 0, 0, 0.3, 0, 0.3, 0.3, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0.2, 0, 0, 0.3, 0.2, 0.2, 0.2, 0.4, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

array_1 = np.array([[0, 0, 0.3, 0.8, 0.6, 0.7, 0.9, 0.9, 0.4, 1],   # crreate that have initial values and doesn't perform it to inf
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0.2, 0, 0, 0, 0.3, 0, 0.3, 0.3, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0.2, 0, 0, 0.3, 0.2, 0.2, 0.2, 0.4, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

weighted_array = np.array([[0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

for i in range(0, 10):  # replace values which == 0 to infinity(it it step according to the classic Floid )
    for j in range(0, 10):
        if array_0[i][j] == 0.0:
            array_0[i][j] = float('inf')

for m in range(1, 10):  ## calculate for each matrix
    for u in range(0, 10):
        if u == 0:
            for v in range(0, 10):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]), array_0[u][v])
        if u == 1:
            for v in range(0, 10):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]), array_0[u][v])
        if u == 2:
            for v in range(0, 10):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]), array_0[u][v])
        if u == 3:
            for v in range(0, 10):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]), array_0[u][v])
        if u == 4:
            for v in range(0, 10):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]), array_0[u][v])
        if u == 5:
            for v in range(0, 10):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]), array_0[u][v])
        if u == 6:
            for v in range(0, 10):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]), array_0[u][v])
        if u == 7:
            for v in range(0, 10):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]), array_0[u][v])
        if u == 8:
            for v in range(0, 10):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]), array_0[u][v])
        if u == 9:
            for v in range(0, 10):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]), array_0[u][v])
        if u == 10:
            for v in range(0, 10):
                array_min[u][v] = min((array_0[u][m] + array_0[m][v]), array_0[u][v])
                if array_min[u][
                    v] == 0.0:  ## it is just according that the latest row with all infinity values doesn't show as infinity
                    array_min[u][v] = float('inf')
## replace all 0.0 to float('inf') for correct min values
for i in range(0, 10):
    for j in range(0, 10):
        if array_min[i][j] == 0.0:
            array_min[i][j] = float('inf')

# find indexes where min value to estimate which factors have the minimum influence on the fires
min_value = np.min(array_min)  ## show the value of minimum element

for i in range(0, 10):
    for j in range(0, 10):
        if array_min[i][j] == min_value:
            print(f"the minimum value is {i}{j} and equal {min_value}")

for i in range(0, 10):
    for j in range(0, 10):
        array_max[i][j] = array_min[i][j]
        if array_max[i][j] == float('inf') or array_max[i][j] == - float('inf'):
            array_max[i][j] = 0.0
        if array_max[i][j] == 1:
            array_max[i][j] = 0.0
max_value = np.max(array_max)  ## show the value of maximum element

for i in range(0, 10):
    for j in range(0, 10):
        if array_max[i][j] == max_value:
            print(f"the maximum value is {i}{j} and equal {max_value}")

# print(max_value)
# print(min_value)
# print(array_max)


array_for_plotting = weighted_array * array_1
G = nx.from_numpy_array(array_for_plotting)

# colors for edges and weights
edge_colors = ['red','green','blue','orange','yellow','purple','cyan','magenta','brown' ,'gray' ,'black']
edge_labels = nx.get_edge_attributes(G, 'weight')

pos = nx.spring_layout(G)  # Определяем позиции вершин графа #Determine the position of verticles graph
label_pos = 0.4 #distance from the middle of the edge
nx.draw(G, pos, with_labels=True, edge_color=edge_colors,arrows = True, arrowstyle='->',width=2.0, node_size = 1000, font_color = 'red',font_size = 14)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=label_pos, font_color = 'green')
plt.axis('off')
plt.show()