#!/usr/bin/env python
#  blitzavi89
# ----------------------------------------------------------------
# COURSERA ALGORITHMS-2 PROGRAMMING ASSIGNMENT-2 PROBLEM-1 (Python 3.x)
# ----------------------------------------------------------------

parent = dict()
rank = dict()

def make_set(vertice) :
	parent[vertice] = vertice
	rank[vertice] = 0

def find_set(vertice) :
	if parent[vertice] != vertice :
		parent[vertice] = find_set(parent[vertice])
	return parent[vertice]

def union_set(vertice1, vertice2) :
	temp1 = find_set(vertice1)
	temp2 = find_set(vertice2)
	print (temp1, temp2)
	print (vertice1, vertice2)
	if temp1 != temp2 :
		if rank[temp1] > rank[temp2] :
			parent[temp2] = temp1
		elif rank[temp1] < rank[temp2] :
			parent[temp1] = temp2
		elif rank[temp1] == rank[temp2] :
			parent[temp2] = parent[temp1]
			rank[temp2] +=1
			print ("rank incremented")
		return True
	else :
		return False

# Function to extract edges and distances from the clustering1.txt list provided
def extract_edge_dist(graph_list) :
	costs = []
	edge = []
	for data in graph_list :
		temp_string = data
		costs.append((temp_string.split(' '))[2])
		edge.append([(temp_string.split(' '))[0], (temp_string.split(' '))[1]])
	return (costs, edge)

# Function to sort the edges based on their increasing distances/costs
def sort_edge_dist(cost_sort, edge_sort) :
	len_list = len(cost_sort)
	cost_int = [int(cost_sort[i]) for i in range(len_list)]
	cost_int, cost_sort, edge_sort = zip(*sorted(zip(cost_int, cost_sort, edge_sort)))
	return (cost_sort, edge_sort)

def Cluster_Kruskal (costs, edges) :
	Cluster_Size = 500
	i = 0
	while Cluster_Size > 4 :
		bool_check = union_set(int(edge[i][0]), int(edge[i][1]))
		if bool_check is True :
			Cluster_Size -= 1
			print (edge[i])
			i = i + 1
		else :
			i = i + 1
	print ("Cluster Limit Hit = " + str(Cluster_Size))

if __name__ == "__main__" :
	graph_file = open("clustering1.txt", "r+")
	graph_list = [line.strip() for line in graph_file]
	graph_file.close()
	graph_list.remove("500")

# Number of vertices is number of nodes under the range field in for loop. While creating vertice we add 1 in range(). i.e. 500 + 1
	vertice = [i for i in range(501) if i != 0]
	for i in range(500) :
		make_set(vertice[i])
	costs, edge = extract_edge_dist(graph_list)

# Edges are sorted based on their increasing costs
	costs, edge = sort_edge_dist(costs, edge)

# Implement Kruskal Algorithm till we hit k = 4 as per the clustering question
	Cluster_Kruskal(costs, edge)
	new_remains = [i for i in rank if rank[i] == 0]
	print (new_remains)

# Calculate the minimum spacing between any of the clusters
	max = 1000000
	edge_length = len(edge)
	print (edge_length)
	for index in range(edge_length) :
		if find_set(int(edge[index][0])) != find_set(int(edge[index][1])) :
			if int(costs[index]) < max :
				max = int(costs[index])
				x = int(edge[index][1])
			else :
				pass
	print ("Minimum space between any of the clusters = " + str(max))

