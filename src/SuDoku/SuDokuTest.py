import itertools

# function to apply vertical and horizontal constraints
def v_h_cnstr(sudo_cnstr, sudo_nums):	
	
	multi_inds = [[i2 for i2, j2 in enumerate(j1) if j2 not in sudo_nums] for i1, j1 in enumerate(sudo_cnstr)]
	single_inds = [[i2 for i2, j2 in enumerate(j1) if j2 in sudo_nums] for i1, j1 in enumerate(sudo_cnstr)]
	single_vals = [[j2 for i2, j2 in enumerate(j1) if j2 in sudo_nums] for i1, j1 in enumerate(sudo_cnstr)]
	
	for i1, j1 in enumerate(multi_inds):
		h_list = single_vals[i1]
		for i2, j2 in enumerate(j1):
			v_list = [sudo_cnstr[i][j1[i2]] for i, j in enumerate(single_inds) if j2 in j]
			h_v_list = sorted(h_list + list(set(v_list) - set(h_list)))
			h_v_poss = sorted(list(set(sudo_cnstr[i1][j2]) - set(h_v_list)))

			if len(h_v_poss) == 1:
				sudo_cnstr[i1][j2] = h_v_poss[0]



sudo_file = open('SuEg1.txt', 'r+')
sudo_list = []
sudo_size = 9
sudo_nums = [n+1 for n in range(sudo_size)]

for row in sudo_file:
	char_list = list(itertools.chain.from_iterable(row))
	int_list = list(map(int, char_list[:sudo_size]))
	sudo_list.append(int_list)


sudo_cnstr = [[j2 if j2 != 0 else sudo_nums for i2, j2 in enumerate(j1) ] for i1, j1 in enumerate(sudo_list)]

v_h_cnstr(sudo_cnstr, sudo_nums)

