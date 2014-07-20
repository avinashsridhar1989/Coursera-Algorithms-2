#!/usr/bin/env python
#  blitzavi89
# ----------------------------------------------------------------
# COURSERA ALGORITHMS-1 PROGRAMMING ASSIGNMENT-1 (Python 3.x)
# ----------------------------------------------------------------

def difference (w_list, l_list) :
	list_length = len(w_list)
	d_list = [str(int(w_list[i]) - int(l_list[i])) for i in range(list_length)]
	return d_list

def division (w_list, l_list) :
	list_length = len(w_list)
	d_list = [str(int(w_list[i]) / int(l_list[i])) for i in range(list_length)]
	return d_list

def division_sort (joblist, ds_list) :
	list_length = len(ds_list)
	ds_temp_list = [float(ds_list[i]) for i in range(list_length)]
	ds_temp_list, joblist = zip(*sorted(zip(ds_temp_list, joblist), reverse = True))
	#print (ds_temp_list)
	return joblist

def weighted_diff_sort (w_list, l_list, ds_list) :
	unique = []
	seen = []
	list_length = len(w_list)
	for data in ds_list :
		if (data not in seen) :
			unique.append(data)
			seen.append(data)
		else :
			seen.append(data)
	list_1 = []
	for diff_value in unique :
		list_2 = []
		list_temp_weight = []
		list_temp_length = []
		list_temp_weight = [int(w_list[i])for i in range(list_length) if str(int(w_list[i]) - int(l_list[i])) == diff_value]
		list_temp_length = [l_list[i]for i in range(list_length) if str(int(w_list[i]) - int(l_list[i])) == diff_value]
		temp_len = len(list_temp_weight)
		list_temp_weight, list_temp_length = zip(*sorted(zip(list_temp_weight, list_temp_length), reverse = True))
		list_2 = [str(list_temp_weight[i]) + ' ' + str(list_temp_length[i]) for i in range(temp_len)]  
		list_1 = list_1 + list_2
	return list_1

def list_split (joblist) :
	w_list = []
	l_list = []
	for data in joblist :
		temp_string = data
		w_list.append((temp_string.split(' '))[0])
		l_list.append((temp_string.split(' '))[1])
	return (w_list, l_list)

def compute_time (w_list, l_list) :
	total_time = 0
	length_sum = 0
	list_length = len(w_list)
	print (list_length)
	print ("\n\n\n")
	for i in range(list_length) :
		total_time += (length_sum + int(l_list[i]))*(int(w_list[i]))
		length_sum += int(l_list[i])
	return total_time

if __name__ == "__main__" :
	job_file = open("Jobs-Data.txt", "r+")
	job_list = []
	weight_list = []
	length_list = []
	job_list = [line.strip() for line in job_file]
	job_file.close()
	job_list.remove("10000")
	weight_list, length_list = list_split(job_list)
	diff_list = difference(weight_list, length_list)
	div_list = division(weight_list,length_list)
	diff_list.sort(key = int, reverse = True)
	fresh_sorted = weighted_diff_sort(weight_list,length_list,diff_list)
	weight_list, length_list = list_split(fresh_sorted)
	#print (fresh_sorted)
	print ("Total Computation Time = " + str(compute_time(weight_list, length_list)))
	weight_list, length_list = list_split(division_sort(job_list, div_list))
	print ("Total Computation Time based on decreasing ratio w/l = " + str(compute_time(weight_list, length_list)))






