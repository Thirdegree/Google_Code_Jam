lines = []
linesR = []

with open("B-large-practice.in") as t:
	n = int(t.readline())
	for i in xrange(n):
		lines.append(t.readline().split())

for i in lines:
	linesR.append(reversed(i))

with open("output", "r+") as o:
	for i,k in zip(xrange(1,len(linesR)+1), linesR):
		o.write("Case #%d: %s\n"%(i, " ".join(k)))

