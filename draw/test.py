from  draw.properties import *
from draw.draw_network import *
# print(get_shortest_length(dialect_adj_mat)[10:32])
# degree=get_node_degree(name_adj_mat)
# print(degree)
# u=np.mean(degree)#P(k)=(u)**k*e**(-u)/k!
# print('平均度为',u)
# p=np.zeros(len(degree))
# for k in range(1,len(degree)):
#     k_jiecheng=get_factorial(k)
#     p[k]=u**k*math.exp(-u)/get_factorial(k)
# # print(degree)
# plt.figure(figsize=(8,5))
# a=plt.hist(degree,normed=1,bins=19)
# plt.ylabel('num')
# plt.xlabel('degree')
# # y2=malb.normpdf(bins)
# # x = np.random.poisson(lam=5, size=10000)  # lam为λ size为k
# # pillar = 15
# # a = plt.hist(x, bins=pillar, normed=True, range=[0, pillar], color='g', alpha=0.5)
# plt.plot(p, 'r')
# plt.grid()
# plt.show()
#print(get_cluster_coefficient(name_adj_mat))
# np.set_printoptions(1,suppress=True)
# mat1,mat2=np.array(get_shortest_length(new_mat))
# print(mat1[35])
# print(mat2[0:10])
# print(get_branch_num(hometown_adj_mat))
#mat_attack,delete_flag=random_attack(name_adj_mat)
# print(get_shortest_length(mat_attack))
print("---------------------name-----------------------")
coreness=np.zeros(name_adj_mat.shape[0])
print('coreness',get_graph_coreness(name_adj_mat,coreness))
print('cluster_coefficient',np.mean(get_cluster_coefficient(name_adj_mat)))
print('degree',get_node_degree(name_adj_mat))
print('degree_distribution',get_degree_distribution(name_adj_mat))
print('average_shortest_length',get_average_shortest_length(name_adj_mat))

print("---------------------HOMETOWN-----------------------")
coreness=np.zeros(hometown_adj_mat.shape[0])
print('coreness',get_graph_coreness(hometown_adj_mat,coreness))
print('cluster_coefficient',np.mean(get_cluster_coefficient(hometown_adj_mat)))
print('degree',get_node_degree(hometown_adj_mat))
print('degree_distribution',get_degree_distribution(hometown_adj_mat))
print('average_shortest_length',get_average_shortest_length(hometown_adj_mat))

print("---------------------dialect-----------------------")
coreness=np.zeros(dialect_adj_mat.shape[0])
print('coreness',get_graph_coreness(dialect_adj_mat,coreness))
print('cluster_coefficient',np.mean(get_cluster_coefficient(dialect_adj_mat)))
print('degree',get_node_degree(dialect_adj_mat))
print('degree_distribution',get_degree_distribution(dialect_adj_mat))
print('average_shortest_length',get_average_shortest_length(dialect_adj_mat))

#
# G=draw_figure(dialect_adj_mat)
# print(ns.clustering(G))
# print(get_cluster_coefficient(dialect_adj_mat))