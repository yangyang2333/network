import  numpy as np
import matplotlib.mlab as malb
import math
from draw.draw_network import *
name_csv_path='E:\\ideaProject\\network\\name.csv'
hometown_csv_path='E:\\ideaProject\\network\\hometown.csv'
dialect_csv_path='E:\\ideaProject\\network\\dialect.csv'
name_mat=getData(name_csv_path)
hometown_mat=getData(hometown_csv_path)
dialect_mat=getData(dialect_csv_path)
name_adj_mat=get_undirect_mat(name_mat)
dialect_adj_mat=get_undirect_mat(dialect_mat)
hometown_adj_mat=get_undirect_mat(hometown_mat)

def get_shortest_length(adj_mat):
    #i,j =adj_mat.shape
    dis_mat=np.zeros(adj_mat.shape)
    path=np.zeros(adj_mat.shape)
    for i in range(adj_mat.shape[0]):
        for j in range(adj_mat.shape[1]):
            if adj_mat[i][j]==0 and i !=j:
                dis_mat[i][j]=65535
            else:
                if adj_mat[i][j]==1 and i!=j:
                    dis_mat[i][j]=1
    for i in range(dis_mat.shape[0]):
        for j in range(dis_mat.shape[0]):
            if (dis_mat[i, j] != 65535 and dis_mat[i, j] != 0):
                path[i][j] = i
    for a in range(dis_mat.shape[0]):
        for b in range(dis_mat.shape[0]):
            for c in range(dis_mat.shape[0]):
                if dis_mat[b, a] + dis_mat[a, c] < dis_mat[b, c]:
                    dis_mat[b, c] = dis_mat[b, a] + dis_mat[a, c]
                    path[b][c] = path[a][c]
    return dis_mat
def get_average_shortest_length(adj_mat):
    dis_mat=get_shortest_length(adj_mat)
    total=0
    num=0
    for i in range(dis_mat.shape[0]):
        for j in range(dis_mat.shape[1]):
            if dis_mat[i][j]!=0 and dis_mat[i][j]!=65535:
                num=num+1
                total=total+dis_mat[i][j]
    average=total/num
    return average

def get_node_degree(adj_mat):
    degree=np.zeros(adj_mat.shape[0])
    for i in range(adj_mat.shape[0]):
        for j in range(adj_mat.shape[1]):
            if adj_mat[i][j]==1:
                degree[i]=degree[i]+1
    return degree
def get_degree_distribution(adj_mat):
    degree=get_node_degree(adj_mat)
    u = np.mean(degree)  # P(k)=(u)**k*e**(-u)/k!
    print('平均度为',u)
    p=np.zeros(len(degree))
    for k in range(1,len(degree)):
         k_jiecheng=get_factorial(k)
         p[k]=u**k*math.exp(-u)/get_factorial(k)
    # # print(degree)
    plt.figure(figsize=(4,4))
    a = plt.hist(degree, normed=1, bins=19)
    plt.ylabel('num')
    plt.xlabel('degree')
    plt.plot(p, 'r')
    plt.grid()
    plt.show()

def get_node_with_max_degree(degree):
    max=0
    index=0
    for i in range(len(degree)):
        if degree[i]>max:
            max=degree[i]
            index=i
    return index
def get_cluster_coefficient(adj_mat):
    neighbor=[]
    degree=get_node_degree(adj_mat)
    C=[]
    for i in range(adj_mat.shape[0]):
        neighbor.clear()
        for j in range(adj_mat.shape[1]):
            if adj_mat[i][j]==1:
                neighbor.append(j)
        if degree[i]==0:
            C.append(0)
        else:
            C.append(2*get_edges_num_by_nodelist(neighbor,adj_mat)/(degree[i]*(degree[i]-1)))
    return C
def get_edges_num_by_nodelist(nodelist,adj_mat):
    num=0
    for i in range(len(nodelist)):
        for j in range(len(nodelist)):
            if i!=j and adj_mat[nodelist[i]][nodelist[j]]==1:
                num=num+1
    return num/2
def get_factorial(k):
    n=1
    while k>1:
        n=n*k
        k=k-1
    return n


def get_branch_num(adj_mat):
    visit = np.zeros(adj_mat.shape[0])
    n=0
    max=0
    global size
    for i in range(adj_mat.shape[0]):
        if visit[i]==0:
            size = 0
            n=n+1
            dfs(i,visit,adj_mat)
            if size>max:
                max=size
            #print(si

    return n,max


def dfs(node,visit,adj_mat):
    visit[node] = 1
    global size
    size=size+1
    for i in range(len(visit)):
        if adj_mat[node][i]==1 and visit[i]==0:
            dfs(i,visit,adj_mat)
def get_next_neighbor(i,j,adj_mat):
    for k in range(j+1,adj_mat.shape[1]):
        if adj_mat[i][k]==1:
            return k
#鲁棒性分析
def robust_analysis(adj_mat):
    mat1 = adj_mat.copy()
    mat2 = adj_mat.copy()
    a, b, c, d = random_attack(mat1)
    a1, b1, c1, d1 = intentional_attack(mat2)
    # plt.plot(c,'*')
    # plt.plot(c1,'-')
    plt.figure(figsize=[4, 4])
    x = np.linspace(0, 1, name_adj_mat.shape[0])
    p1, = plt.plot(x, d, 'r')
    p2, = plt.plot(x, d1, 'b')
    plt.grid(True)
    plt.xlabel('f')
    plt.ylabel('n')
    l1 = plt.legend([p2, p1, ], ['intentional attack', 'random attack'],loc='upper left',fontsize='6')
    plt.gca().add_artist(l1)

    plt.savefig('max.jpg')
    plt.show()
    p3, = plt.plot(x, c, 'r')
    p4, = plt.plot(x, c1, 'b')
    l1 = plt.legend([p4, p3, ], ['intentional attack', 'random attack'],loc='upper right')
    plt.show()
    pass
def random_attack(adj_mat):
    max_subgraph_size = []
    flag=np.zeros(adj_mat.shape[0])
    i=1
    delete_flag=np.zeros(adj_mat.shape[0])
    branch_num=[]
    # branch_num.append(get_branch_num(adj_mat)[0])
    # max_subgraph_size=get_branch_num(adj_mat)[1]
    while i<=adj_mat.shape[0]:
        node=math.floor(np.random.uniform(0,adj_mat.shape[0]))

        while flag[node]==1:
            node = math.floor(np.random.uniform(0, adj_mat.shape[0]))
        flag[node]=1
        print("被删除的节点是：",node)
        delete_flag[node]=1
        for j in range(adj_mat.shape[0]):
            adj_mat[node][j]=-1
            adj_mat[j][node]=-1
        n,max=get_branch_num(adj_mat)
        print('第',i,'次随机攻击后分支数目为:',n-i)
        branch_num.append(n-i)
        max_subgraph_size.append(max)
        draw_figure(adj_mat)
        i=i+1
    return adj_mat,delete_flag,max_subgraph_size,branch_num
def intentional_attack(adj_mat):
    max_subgraph_size = []
    branch_num=[]
    # branch_num.append(get_branch_num(adj_mat)[0])
    flag = np.zeros(adj_mat.shape[0])
    i = 1
    delete_flag = np.zeros(adj_mat.shape[0])
    while i <=adj_mat.shape[0]:
        degree=get_node_degree(adj_mat)
        node = get_node_with_max_degree(degree)
        flag[node] = 1
        print("被删除的节点是：", node)
        delete_flag[node] = 1
        for j in range(adj_mat.shape[0]):
            adj_mat[node][j] = -1
            adj_mat[j][node] = -1
        n, max = get_branch_num(adj_mat)
        print('第', i, '次故意攻击后分支数目为:', n-i)
        branch_num.append(n-i)
        max_subgraph_size.append(max)
        draw_figure(adj_mat)
        i = i + 1
    return adj_mat, delete_flag, max_subgraph_size,branch_num
def get_coreness(G,n,coreness):
    G2=G.copy()
    for node in G2.nodes:
        if G2.degree(node) <= n:
            G.remove_node(node)
            coreness[node]=n
            return get_coreness(G,n,coreness)
            break
    return G
def get_graph_coreness(adj_mat,coreness):
    G = draw_figure(adj_mat)
    print('工具包算出来的coreness',ns.core_number(G))
    print(max(ns.core_number(G).values()))
    G2 = G.copy()
    n = 0
    while len(G2.nodes) > 0:
        G2 = get_coreness(G2, n,coreness)
        #接下来几行代码是演示
        # ns.draw(G2, ns.circular_layout(G2), node_color='b', edge_color='r', with_labels=True, font_size=18,
        #         node_size=400)
        # plt.show()
        n = n + 1
    return n-1,coreness
robust_analysis(hometown_adj_mat)
#print(get_cluster_coefficient(hometown_adj_mat))