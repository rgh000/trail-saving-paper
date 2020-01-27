import os
import math
import sys

f = open(sys.argv[1], 'r')
os.system('rm ' + sys.argv[2])
f0 = open(sys.argv[2], 'w')
f1 = open('2' + sys.argv[2], 'w')
lines = f.read().split('\r')
inter = {}
incr = 0.2
extreme_neg = 0
extreme_pos = 0
intervals = [-2.0, -1.8, -1.6, -1.4, -1.2, -1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
total = 0
for i in intervals:
	inter[i] = 0

for l in lines[1:]:
	a, b = (float)(l.split('\t')[0]), (float)(l.split('\t')[1])
	data = math.log((a+1e-8) / (b+1e-8), 2.0)
	if data >= intervals[0] - incr / 2.0 and data < intervals[len(intervals)-1] + incr / 2.0:
		for i in intervals:
			if data >= i - incr / 2.0 and data < i + incr / 2.0:
				inter[i] += 1
				total += 1
				break
	elif data < intervals[0] - incr / 2.0:
		extreme_neg += 1
	elif data >= intervals[len(intervals)-1] + incr / 2.0:
		extreme_pos += 1

for i in intervals:
	if i < 0:
		f0.write((str)(-i) + '\t' + (str)(inter[i]) + '\n')
	elif i > 0:
		f1.write((str)(i) + '\t' + (str)(inter[i]) + '\n')

print inter[0], ' ', extreme_neg, ' ', extreme_pos, ' ', total
f.close()
f0.close()
f1.close()