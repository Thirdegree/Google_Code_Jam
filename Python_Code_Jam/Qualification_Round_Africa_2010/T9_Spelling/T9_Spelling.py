#Problem C: T9 Spelling
#This program works on any size file

file = open('C-large-practice.txt', 'r+')

n = int(file.readline()) # n test cases

string_list = {}
convert_list = {'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333', 'g': '4', 'h': '44', 'i': '444', 
				'j': '5', 'k': '55', 'l': '555', 'm': '6', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777',
				's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99', 'y': '999', 'z': '9999', ' ': '0', '\n': ''}

#populates the Dict string_list
for i in range(n):
	string_list[i] = file.readline()
	
file = open('C-large-practice-solution.txt', 'r+')

#Changes each letter to it's numeric equivalent according to convert_list	
def convert(word_list):
	s = list(word_list)
	for i in range(len(s)):
		s[i] = convert_list[s[i]]
	s.remove('')
	return s


#applies the required formatting convention.
for i in range(n):
	converted = convert(string_list[i])
	converted_temp = []
	print converted
	for n in range(len(converted)):
		if n-1 == -1:
			converted_temp.append(converted[n])
		elif converted[n] in converted[n-1] or converted[n-1] in converted[n]: #there may be a better way to do this, but I don't know of one
			converted_temp.append(' ')
			converted_temp.append(converted[n])
		else: 
			converted_temp.append(converted[n])
	converted_temp =  ''.join(converted_temp)
	string_list[i] = converted_temp
	
#output
for i in range(len(string_list)):
	file.write("Case #" + str(i+1) + ': ' + str(string_list[i]) + '\n')
	print "Case #" + str(i+1) + ': ' + str(string_list[i]) + '\n'
	