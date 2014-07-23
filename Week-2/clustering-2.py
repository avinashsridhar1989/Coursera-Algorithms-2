#!/usr/bin/env python
#  blitzavi89
# ----------------------------------------------------------------
# COURSERA ALGORITHMS-2 PROGRAMMING ASSIGNMENT-2 PROBLEM-2 (Python 3.x)
# ----------------------------------------------------------------
import timeit

parent = dict()
rank = dict()
cluster = dict()

# Implementation of make, find, and union structure algorithms
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
	if temp1 != temp2 :
		if rank[temp1] > rank[temp2] :
			parent[temp2] = temp1
		elif rank[temp1] < rank[temp2] :
			parent[temp1] = temp2
		elif rank[temp1] == rank[temp2] :
			parent[temp2] = parent[temp1]
			rank[temp2] +=1
		return True
	else :
		return False

# Implemented set of 24 bit numbers with one 1 and two 1s using bit shift manipulation
def xor_lists(num_bits) :
	one_1_poss = []
	two_1_poss = []
	for i in range(num_bits) :
		one_1_poss.append(1 << i)
	for i in range(num_bits) :
		temp1 = 1 << i
		for j in range(num_bits) :
			if j != i :
				temp2 = temp1 + (1 << j)
				if temp2 not in two_1_poss :
					two_1_poss.append(temp2)
				else : pass
			else : pass	
	return (one_1_poss, two_1_poss)

# Return new_one_spaced and two_one_spaced which have the XOR operations with every vertex node and 300 bit combinations
def one_spacing_list(int_value, one_1_poss):
	new_one_spaced = []
	new_one_spaced = [(int_value ^ i) for i in one_1_poss]
	return new_one_spaced

def two_spacing_list(int_value, two_1_poss) :
	new_two_spaced = []
	new_two_spaced = [(int_value ^ i) for i in two_1_poss]
	return new_two_spaced

# Calcuate value of K (max. clusters value) for spacing of 1 and 2 hamming distances (Similar to Kruskal Algorithm)
def k_cluster_kruskal(one_1_poss, two_1_poss, graph_list_integer, count) :
	len_list = len(graph_list_integer)
	for index in range(len_list) :

		new_one_spaced = one_spacing_list(graph_list_integer[index], one_1_poss)

		new_two_spaced = two_spacing_list(graph_list_integer[index], two_1_poss)
		for element in new_one_spaced :
			if (element != graph_list_integer[index]) and (element in cluster) :
				bool_check = union_set(index + 1, cluster[element])
				if bool_check == True :
					count = count - 1
					#print ("Current Value of Count = " + str(count))
				else :
					pass
			else :
				pass
		for element in new_two_spaced :
			if (element != graph_list_integer[index]) and (element in cluster) :
				bool_check = union_set(index + 1, cluster[element])
				if bool_check == True :
					count = count - 1
					#print ("Current Value of Count = " + str(count))
				else :
					pass
			else :
				pass	
	return count

if __name__ == "__main__" :
	graph_list = []
	graph_file = open("clustering_big.txt", "r+")
	graph = [line.strip() for line in graph_file]
	graph_file.close()

# Obtain number of bits in distance field for each node
	num_bits = int(graph[0].split(' ')[1])
	graph.remove("200000 24")
	vertice = [i for i in range(200001) if i != 0]

# Number of vertices is number of nodes under the range field in for loop and while creating it we add one in range()
	for i in range(200000) :
		make_set(vertice[i])

# Remove the spaces in between each binary digit for every binary value string
	graph = [data.replace(' ', '') for data in graph]

# Remove Duplicate Values
	graph_list = list(set(graph))

# Store the integer values of all binary representations in graph_list_integer
	graph_list_integer = [int(data, base = 2) for data in graph_list]

# Create dictionary with all the decimal values of 24 bit numbers	
	x = 1
	for i in graph_list_integer :
		cluster[i] = x
		x += 1

	count_initial = len(graph_list)

# start and stop invoke timers to check speed of program, Final execution of program
	start = timeit.default_timer()
	one_1_poss, two_1_poss = xor_lists(num_bits)
	final_count = k_cluster_kruskal(one_1_poss, two_1_poss, graph_list_integer, count_initial)
	print ("\nFinal value of K for cluster is " + str(final_count))
	stop = timeit.default_timer()
	print (stop - start)



