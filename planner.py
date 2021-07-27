import numpy as np
import argparse
from pulp import *
#####################################################################

def b_star(func):
	return np.max(np.sum(T*(R + gamma*func), axis=2), axis=1)

def get_pi(Q):
	return np.argmax(Q, axis=1)

def get_V(pi):
	A = gamma*T[np.arange(n), pi, :] - np.eye(n)
	b = -np.sum(T[np.arange(n), pi, :] * R[np.arange(n), pi, :], axis=1)
	return np.linalg.solve(A,b)

def get_Q(V):
	return np.sum(T*(R+gamma*V), axis=2)

def print_v_and_pi(arr):
	for i in range(n):
		print(arr[0,i], arr[1,i])

####################################################################

def value_iteration():
	old_val = np.random.randn(n)/10
	while True:
		new_val = b_star(old_val)
		if np.max(np.abs(new_val - old_val)) < 1e-10: break
		else: old_val = new_val 
	return np.array([old_val, get_pi(get_Q(old_val))])

###################################################################

def policy_improvement(pi):
	Q = get_Q(get_V(pi))
	return np.argmax(Q, axis=1)

def howards_policy_iteration():
	old_pi = np.random.randint(0, k, n)
	while True:
		new_pi = policy_improvement(old_pi)
		if (new_pi == old_pi).all() : break
		else: old_pi = new_pi
	return np.array([get_V(old_pi), old_pi])


###################################################################

def linear_programming():
	N = range(n); K = range(k)
	
	prob = LpProblem("MDP_Planning", LpMinimize)
	V = LpVariable.dicts('V', (N,))

	prob += lpSum(V)
	for s in N:
		for a in K:
			prob += V[s] >= lpSum(
				[T[s,a,s2] * (R[s,a,s2] + gamma*V[s2]) for s2 in N])

	prob.solve(PULP_CBC_CMD(msg=0))

	val = np.array([V[i].value() for i in N])
	return np.array([val, get_pi(get_Q(val))]) 


###################################################################

parser = argparse.ArgumentParser()
parser.add_argument('--mdp', help='Path to the input MDP file')
parser.add_argument('--algorithm', help='One of vi, hpi, and lp')
args = parser.parse_args() 

ifile = args.mdp 
algo = args.algorithm

n = 0; k = 0

f = open(ifile, 'r')

for line in f:
	words = line.split()
	if words[0] == 'numStates': n = int(words[1])
	elif words[0] == 'numActions': k = int(words[1])
	else: break

R = np.zeros((n,k,n)); T = np.zeros((n,k,n))
gamma = 0
mdptype = ''

for line in f:
	words = line.split()
	if words[0] == 'transition':
		s1, a, s2 = [int(x) for x in words[1:4]]
		r, p = [float(x) for x in words[4:]]			
		T[s1,a,s2] = p
		R[s1,a,s2] = r

	elif words[0] == 'mdptype': mdptype = words[1]
	elif words[0] == 'discount': gamma = float(words[1])

f.close()


if algo == 'vi': print_v_and_pi(value_iteration())
elif algo == 'hpi': print_v_and_pi(howards_policy_iteration())
elif algo == 'lp': print_v_and_pi(linear_programming())
else: print('Not implemented yet')



