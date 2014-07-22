#!/usr/bin/env python
#  blitzavi89
# ----------------------------------------------------------------
# COURSERA ALGORITHMS-2 PROGRAMMING ASSIGNMENT-2 PROBLEM-2 (Python 3.x)
# ----------------------------------------------------------------
parent = dict()
rank = dict()
cluster = dict()

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
	#print ("FINDSET",temp1, temp2)
	#print ("VERTICES",vertice1, vertice2)
	if temp1 != temp2 :
		if rank[temp1] > rank[temp2] :
			parent[temp2] = temp1
		elif rank[temp1] < rank[temp2] :
			parent[temp1] = temp2
		elif rank[temp1] == rank[temp2] :
			parent[temp2] = parent[temp1]
			rank[temp2] +=1
			#print ("rank incremented")
		return True
	else :
		return False

def xor_lists() :
	one_1_poss = []
	two_1_poss = []
	temp_val = int("0b111111111111111111111111", 2)
	for i in range(temp_val) :
		if bin(i+1).count("1") == 1 :
			one_1_poss.append(i+1)
		elif bin(i+1).count("1") == 2:
			two_1_poss.append(i+1)
		else :
			pass
	return (one_1_poss, two_1_poss)

def one_spacing_list(int_value, one_1_poss):
	new_one_spaced = []
	new_one_spaced = [(int_value ^ i) for i in one_1_poss]
	return new_one_spaced

def two_spacing_list(int_value, two_1_poss) :
	new_two_spaced = []
	new_two_spaced = [(int_value ^ i) for i in two_1_poss]
	return new_two_spaced

def edge_builder(one_1_poss, two_1_poss, graph_list_integer, count) :
	len_list = len(graph_list_integer)
	for index in range(len_list) :
		#print (graph_list_integer)
		new_one_spaced = one_spacing_list(graph_list_integer[index], one_1_poss)
		#print (new_one_spaced)
		new_two_spaced = two_spacing_list(graph_list_integer[index], two_1_poss)
		#print (new_two_spaced)
		#print ("element" + str(graph_list_integer[index]))
		x = 0
		for index2 in range(len_list) :
			if ((graph_list_integer[index2] in new_one_spaced) or (graph_list_integer[index2] in new_two_spaced)) and (graph_list_integer[index2] != graph_list_integer[index]) and x <=300:
				#print (index+1, index2+1)
				bool_check = union_set(index+1, index2+1)
				if bool_check == True :
					count = count - 1
					#print ("COUNT DECREMENTED! = " + str(count))
					x = x + 1
				else :
					pass
			else :
				pass
			if x >= 300 :
				break
			else :
				pass
	print ("FINAL COUNT = " + str(count))

if __name__ == "__main__" :
	graph_list = []
	graph_file = open("clustering_big.txt", "r+")
	graph = [line.strip() for line in graph_file]
	graph_file.close()
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

# Store the binary values of all the above representations in graph_list_bin
	graph_list_bin = [bin(data) for data in graph_list_integer]
	x = [int(data, 2) for data in graph_list_bin]
	#print (graph_list_integer)
	print (len(graph_list))
	count_initial = len(graph_list)
	print (graph_list_integer)
	one_1_poss, two_1_poss = xor_lists()
	x = [bin(i) for i in one_1_poss]
	y = [bin(i) for i in two_1_poss]
	print (one_1_poss)
	print (two_1_poss)
	print (x)
	print (y)
	edge_builder(one_1_poss, two_1_poss, graph_list_integer, count_initial)




