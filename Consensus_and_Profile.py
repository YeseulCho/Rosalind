# yeseul cho
# USAGE : python Consensus_and_Profile.py

dataset = open('rosalind_cons.txt', 'r').readlines()
result = open('result.txt', 'w')

dic_base = {}
def count_base() :
	
	line_list = []
	base_line = ''
	for line in dataset :
		
		if line[0] == '>' :
			line_list.append(base_line)
			base_line = ''


		else :			
			tmp_base_line = line.strip()
			base_line += tmp_base_line

	line_list.append(base_line)


	for total_base in line_list[1:] :
		base_len = len(total_base)

		for num in range(base_len) :
			base = total_base[num]

			if num not in dic_base :
				dic_base[num] = [0,0,0,0]

			if base == 'A' :
				dic_base[num][0] += 1	

			elif base == 'C' :
				dic_base[num][1] += 1

			elif base == 'G' :
				dic_base[num][2] += 1

			else :
				dic_base[num][3] += 1

	return dic_base


def consensus_base(dictionary_base) :

	final_base = ''
	for v in dictionary_base.values() :

		tmp = 0 
		for cnt in v :
			if cnt >= tmp :
				tmp = cnt

		max_index = v.index(tmp)

		if max_index == 0 :
			max_base = 'A'
	
		elif max_index == 1 :
			max_base = 'C'

		elif max_index == 2 :
			max_base = 'G'

		else : 
			max_base = 'T' 

		final_base += max_base

	return final_base


dic_sort_base = {}
def sort_base_cnt(dictionary_base) :

	for v in dictionary_base.values() :
		
		for num in range(len(v)) :
			
			if num not in dic_sort_base :
				dic_sort_base[num] = '%s\t'%(v[num])

			else :
				tmp = '%s\t'%(v[num])
				dic_sort_base[num] += tmp

	tmp_val = dic_sort_base.values()

	return tmp_val

	
def main() :
	count_base()
	cons_base = consensus_base(dic_base)
	sort_base = sort_base_cnt(dic_base)

	tmp_cons = '%s\n'%(cons_base)
	result.write(tmp_cons)

	tmp_A = 'A: %s\n'%(sort_base[0])
	tmp_C = 'C: %s\n'%(sort_base[1])
	tmp_G = 'G: %s\n'%(sort_base[2])
	tmp_T = 'T: %s\n'%(sort_base[3])

	tmp_base = tmp_A + tmp_C + tmp_G + tmp_T
	result.write(tmp_base)

main()
