import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()
#read file
readFile=open("libraryUpgrade.txt","r")
for line in readFile:
	spline=line.split(",")
	if (int (spline[2])==1):
		G.add_edge(spline[0],spline[1],color='r')
	else:
		G.add_edge(spline[0],spline[1],color='g')
		

	    


pos=nx.circular_layout(G)
edges=G.edges()
colors=[G[u][v]['color']for u,v in edges]

nx.draw(G,pos,node_color='b', with_labels=True,edges=edges,edge_color=colors)

plt.show()	