f = open('/usr/share/dict/british-english','r+')
count = 1
wanted_list = []
wanted_len = 4

curr_count = 1
curr_char = 'a'
curr_list = []

for line in f:
	if line.isupper():
		continue
	elif line[0].isupper():
		continue
	elif line[-3:] == '\'S\n':
		continue
	elif line[-3:] == '\'s\n':
		continue
	elif len(line) == wanted_len + 1:
		if line[0] == curr_char:
			curr_list.append(line[:-1])
		else:
			wanted_list.append(curr_list)
			#curr_char = chr(ord(curr_char) + 1) 
				# --> creates problems as x has no 4-ltr words
			curr_char = line[0]
			curr_count = curr_count + 1
			curr_list = []
			curr_list.append(line[:-1])
		
wanted_list.append(curr_list)

print wanted_list
print len(wanted_list)
print curr_count

