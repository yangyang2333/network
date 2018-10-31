import matplotlib.pyplot as plt
import numpy as np
from file.datasets import getData
import networkx as ns

def get_undirect_mat(mat):
    width=(mat.shape)[0]
    height=(mat.shape)[1]
    new_mat=np.zeros(mat.shape)
    for i in range(width):
        for j in range(height):
            if mat[i][j]=='y':
                new_mat[i][j]=1
                new_mat[j][i]=1
    return new_mat

def draw_figure(adj_mat):
    G = ns.Graph()
    edges = []
    for i in range(len(adj_mat)):
        for j in range(i):
            if adj_mat[i][j] == 1:
                edges.append((i, j))
        #print(edges)
    for i in range(len(adj_mat)):
            G.add_node(i)
    G.add_edges_from(edges)
    ns.draw(G, ns.circular_layout(G), node_color='b', edge_color='r', with_labels=True, font_size=18, node_size=400)
    plt.show()
    return G
#
# G=ns.Graph()
# name_csv_path='E:\\ideaProject\\network\\name.csv'
# hometown_csv_path='E:\\ideaProject\\network\\hometown.csv'
# dialect_csv_path='E:\\ideaProject\\network\\dialect.csv'
# name_mat=getData(name_csv_path)
# hometown_mat=getData(hometown_csv_path)
# dialect_mat=getData(dialect_csv_path)
# # print(name_mat.shape[0])
# #
# new_mat=get_undirect_mat(dialect_mat)
# draw_figure(new_mat)
# # print(new_mat[:20][:20])
# edges=[]
# for i in range(len(new_mat)):
#     for j in range(i):
#         if new_mat[i][j]==1:
#             edges.append((i,j))
# print(edges)
# for i in range(len(new_mat)):
#     G.add_node(i)
# G.add_edges_from(edges)
#
# print(G.degree())
# #G.remove_node(9)
# get_coreness(G,9)
# if G.number_of_nodes()==0:
#     print("边没了")
# ns.draw(G,ns.circular_layout(G),node_color = 'b',edge_color = 'r',with_labels = True,font_size =18,node_size =400)
# plt.show()
# print(G.degree)
#
# print(ns.clustering(G))
