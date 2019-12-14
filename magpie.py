import os
import api


i = 0
dic_nf = {}
dic_fn = {}
dic_nf_= {}
for root,dirs,files in os.walk(r"workdir"):
    for file in files:
        if file[-2:] == "py" and file != "__init__.py":
            #print(os.path.join(root,file))
            dic_nf[i] = ( (os.path.join(root,file)[:-3])[8:] ).replace("/",".")
            dic_nf_[i]= os.path.join(root,file)
            #print(i)
            #print(dic_nf[i])
            dic_fn[dic_nf[i]] = i
            i = i + 1

n = i
print(n)

for i in range(n):
    print(i , dic_nf[i]),
    print("******"),
    print(dic_nf[i] , dic_fn[dic_nf[i]])

graph_import = api.graph_init(dic_nf , dic_fn , dic_nf_ , n)

#for i in range(n):
#    print("")
#    for j in range(n):
#        print(graph_import[i][j]),

print("")
opt = raw_input("u wanna manu add the graph edge?(choose 'n' if there is no homeless items or finishing) y/n:")
while opt == "y":
    (pred , next) = api.manu_add_import(dic_fn)
    graph_import[pred][next] = 1
    opt = raw_input("continue? y/n:")
#for i in range(n):
#    print("")
#    for j in range(n):
#        print(graph_import[i][j]),
os.system("reset")

api.circle_preprocessor(graph_import , n)

flag_circle_exist = 0
circle_node  = []
for i in range(n):
    for j in range(n):
        if graph_import[i][j] == 1:
            circle_node.append(i)
            circle_node.append(j)
            flag_circle_exist = flag_circle_exist + 1       

if flag_circle_exist > 0:
    print("")
    print("WARNING : IMPORT CIRCLE EXIST!")
    print("edge amount of circle: " + str(flag_circle_exist))
    news_circle_node = list(set(circle_node))
    news_circle_node.sort(key=circle_node.index)
    print("nodes in circle:")
    for i in news_circle_node:
        print(i)
else:
    print("NO CIRCLE FOUND.")
 
 
print("")
new_nodes = []
for i in range(n):
    new_nodes.append(i)
    for j in range(n):
        if graph_import[i][j]:
            print(i),
            print("->"),
            print(j)

print("============================================================") 
for i in range(n):
    for j in range(n):
        if graph_import[i][j]:
            print(dic_nf[i]),
            print("->"),
            print(dic_nf[j])

#api.DFS_circle_search(graph_import , new_nodes)


