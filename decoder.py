import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--grid', help='Path to the input grid file')
parser.add_argument('--value_policy', help='Path to the value and policy file')
args = parser.parse_args()

gridfile = args.grid
vpfile = args.value_policy

f = open(gridfile, 'r')
lst = list(f)
f.close()

sz = len(lst)
grid = np.array([[int(x) for x in s.split()] for s in lst])

states = {}
cnt = 0
for i in range(sz):
	for j in range(sz):
		if grid[i,j] != 1:
			states[(i,j)] = cnt
			cnt += 1

n = len(states)

sx, sy = np.where(grid == 2)[0][0], np.where(grid == 2)[1][0]
ex, ey = np.where(grid == 3)[0][0], np.where(grid == 3)[1][0] 

f = open(vpfile, 'r')
lst = list(f)
f.close()

actions = np.array([float(s.split()[1]) for s in lst])
x,y = sx, sy

while (x,y) != (ex,ey):
	cnt += 1
	a = actions[states[(x,y)]] 
	if a == 0:
		print('S', end=' ')
		x += 1
	elif a == 1:
		print('E', end=' ')
		y += 1
	elif a == 2:
		print('N', end=' ')
		x -= 1
	elif a == 3:
		print('W', end=' ')
		y -= 1
print()




