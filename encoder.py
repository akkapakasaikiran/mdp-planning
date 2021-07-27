import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--grid', help='Path to the input grid file')
args = parser.parse_args()

gridfile = args.grid

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

print(f'numStates {n}')
print('numActions 4')
print('start -1')
print('end -1')
for i in range(n):
	x,y = list(states.keys())[list(states.values()).index(i)]
	if(grid[x,y] == 3): continue
	neighbors = [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]
	for a,b in neighbors:
		if (a,b) in states:
			if grid[a,b] == 0:
				print(f'transition {i} {neighbors.index((a,b))} {states[(a,b)]} 0 1')
			elif grid[a,b] == 3:
				print(f'transition {i} {neighbors.index((a,b))} {states[(a,b)]} 1 1')

print('mdptype continuing')
print('discount 0.9')
			

