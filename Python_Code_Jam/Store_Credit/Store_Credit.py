from collections import OrderedDict

with open("A-large-practice.in", "r") as f:
	n=int(f.readline())
	cases = OrderedDict()
	for i in xrange(n):
		t1 = int(f.readline())
		_ = f.readline()
		t2 = map(int, f.readline().split())
		cases[t1] = t2

sums = {}

def find_matches(total, list1):
	for i in xrange(len(list1)):
		for j in xrange(i+1, len(list1)):
			if list1[i] + list1[j] == total:
				return i+1, j+1

with open("output.txt", "r+") as out:
	for i,k in zip(xrange(1,n+1), cases):
		first, second = find_matches(k, cases[k])
		out.write("Case #%d: %d %d\n"%(i,first,second))