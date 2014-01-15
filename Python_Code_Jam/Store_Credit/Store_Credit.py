#For loops make everything easier.

txt = open("input_large.txt")

n = int(txt.readline())

c = []
l = []
p = []

for i in range(n):
	c.append(map(int, txt.readline().split())[0])
	l.append(map(int, txt.readline().split())[0])
	p.append(map(int, txt.readline().split()))

def find_match(total, xs, start = 1):
	head, tail = xs[0], xs[1:]
	for i in range(len(tail)):
		if head + tail[i] == total:
			return start, i+start+1
	return find_match(total, tail, start = start+1)

with open("output_large.txt","a+") as output:
	for i in range(n):
		t = find_match(c[i], p[i])
		output.write("Case #%s: %d %d\n"%(i+1, min(t), max(t)))
