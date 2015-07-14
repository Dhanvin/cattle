#a = [[1,2,3],[4,5,6],[7,7,7],[[8,9,10], 11, 12]]
import numpy as np
import itertools
class SuDoku:

	#function to make SuDoku in the form of a list of lists
	def make_sudo_list(self, sudo_file, sudo_list):
		for row in sudo_file:
			char_list = list(itertools.chain.from_iterable(row))
			int_list = list(map(int, char_list[:sudo_size]))
			sudo_list.append(int_list)



	# function to replace any zeros by possibilities [1 to 9] , horizontal or vertical
	def replace_zeros(self, c, sudo_status, sudo_nums):
		if c == 'h':
			return [[j2 if j2 != 0 else sudo_nums for j2 in j1] for j1 in sudo_status]
		elif c == 'v':
			return [[j2 if j2 != 0 else sudo_nums for j2 in j1] for j1 in zip(*sudo_status)]



	# function to get vertical and horizontal constraints
	def h_v_cnstr(self, sudo_status, sudo_nums, sudo_cnstr):
		sudo_status_h = self.replace_zeros('h', sudo_status, sudo_nums)
		sudo_status_v = self.replace_zeros('v', sudo_status, sudo_nums)

		sudo_cnstr['horz'] = [sorted(list(set(sudo_nums) - set([j2 for j2 in j1 if j2 in sudo_nums]))) for j1 in sudo_status_h]
		sudo_cnstr['vert'] = [sorted(list(set(sudo_nums) - set([j2 for j2 in j1 if j2 in sudo_nums]))) for j1 in sudo_status_v]

		
		
		

	# function to get square constraints
	def sq_cnstr(self, sudo_status, sudo_nums, sudo_cnstr):
		sudo_cnstr_sq = []
		for i in range(3):
			for j in range(3):
				sudo_cnstr_sq.append(list(set(sudo_nums) - set([j2 for j1 in sudo_status[i*3:(i+1)*3] for j2 in j1[j*3:(j+1)*3] if j2 in sudo_nums])))

		sudo_cnstr['square'] = sudo_cnstr_sq


	
	# function to get unique values and indices in an irregular list of lists
	def get_uniq(self, sudo_status_list, sudo_nums, uniqs, uniq_inds):
		singles_flat  = [j1 for j1 in sudo_status_list if j1 in sudo_nums]
		irr_list = [[j1] if j1 in sudo_nums else j1 for j1 in sudo_status_list]
		flat_list = [j1 for j2 in irr_list for j1 in j2]
		uniqs.append(list(set([j1 for j1 in flat_list if flat_list.count(j1) == 1]) - set(singles_flat)))

		for i in range(len(uniqs[0])):
			uniq_inds.append([i1 for i1, j1 in enumerate(irr_list) if uniqs[0][i] in j1])
	
	
		
	# function to apply single possibility horizontal constraints
	def single_poss_h(self, sudo_status, sudo_nums):
		for i in range(len(sudo_nums)):
			uniqs = []
			uniq_inds = []
			self.get_uniq(sudo_status[i], sudo_nums, uniqs, uniq_inds)
			for ii in range(len(uniqs[0])):
				sudo_status[i][uniq_inds[ii][0]] = uniqs[0][ii]

				
	
	# function to apply single possibility vertical constraints
	def single_poss_v(self, sudo_status, sudo_nums):
		for i in range(len(sudo_nums)):
			uniqs = []
			uniq_inds = []
			self.get_uniq(zip(*sudo_status)[i], sudo_nums, uniqs, uniq_inds)
			for ii in range(len(uniqs[0])):
				sudo_status[uniq_inds[ii][0]][i] = uniqs[0][ii]
				
			
			
	# function to apply consolidated constraints
	def apply_cnstr(self, sudo_status, sudo_nums, sudo_cnstr):

		self.h_v_cnstr(sudo_status, sudo_nums, sudo_cnstr)
		self.sq_cnstr(sudo_status, sudo_nums, sudo_cnstr)
		sudo_status_h = self.replace_zeros('h', sudo_status, sudo_nums)
		multi_inds = [[i2 for i2, j2 in enumerate(j1) if j2 not in sudo_nums] for j1 in sudo_status_h]
		
		if np.array(multi_inds).size == 0:
			return 0
		
		for i1, j1 in enumerate(multi_inds):
			h_list = sudo_cnstr['horz'][i1]
			for i2, j2 in enumerate(j1):
				v_list = sudo_cnstr['vert'][j2]
				sq_list = sudo_cnstr['square'][int(i1/3)*3+int(j2/3)]
				all_poss = sorted(list(set(sudo_status_h[i1][j2]) & set(h_list) & set(v_list) & set(sq_list)))

				if len(all_poss) == 1:
					sudo_status[i1][j2] = all_poss[0]
				else:
		
					sudo_status[i1][j2] = all_poss
		
		self.single_poss_h(sudo_status, sudo_nums)
		self.single_poss_v(sudo_status, sudo_nums)
		return 1




sudo_file = open('SuEg1.txt', 'r+')
sudo_list = []

sudo_size = 9
sudo_nums = [n+1 for n in range(sudo_size)]
sudo_class = SuDoku()

sudo_class.make_sudo_list(sudo_file, sudo_list)
sudo_status = sudo_list
result = 1
count = 1
while (result == 1) & (count<25):
	sudo_cnstr = {}
	result = sudo_class.apply_cnstr(sudo_status, sudo_nums, sudo_cnstr)
	count = count + 1

print count
for line in sudo_status:
	print line

