import itertools

# function to apply vertical and horizontal constraints
def VertHorz_Const(ex_const, ex_size):
	ex_options = [num+1 for num in range(ex_size)]
	
	zero_inds = [[i2 for i2, j2 in enumerate(j1) if j2 not in ex_options] for i1, j1 in enumerate(ex_const)]
	nonzero_inds = [[i2 for i2, j2 in enumerate(j1) if j2 in ex_options] for i1, j1 in enumerate(ex_const)]
	nonzero_vals = [[j2 for i2, j2 in enumerate(j1) if j2 in ex_options] for i1, j1 in enumerate(ex_const)
	
	for i1, z1 in enumerate(zero_inds):
		row_list = nonzero_vals[i1]
		set_row = set(row_list)
		for i2, z2 in enumerate(z1):
			col_list = [ex_const[ind][z1[i2]] for ind, val in enumerate(nonzero_inds) if z2 in val]
			set_col = set(col_list)
			row_col_list = sorted(row_list + list(set_col - set_row))

			if ex_const[i1][z2] == 0:
				row_col_poss = sorted(list(set(ex_options) - set(row_col_list)))
			else:
				row_col_poss = sorted(list(set(ex_const[i1][z2]) - set(row_col_list)))

			if len(row_col_poss) == 1:
				ex_const[i1][z2] = row_col_list[0]
	


ex_file = open('SuEg1.txt', 'r+')
ex_list = []
ex_size = 9
for line in ex_file:
	char_list = list(itertools.chain.from_iterable(line))
	int_list = list(map(int, char_list[:ex_size]))
	ex_list.append(int_list)


ex_const = ex_list
print ex_list
VertHorz_Const(ex_const, ex_size)

