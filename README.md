# mdp-planning

A simple implementation of a few algorithms to solve the MDP planning problem. A maze is also solved by piggybacking on this implementation.

## Task 1: MDP Planning 

`$ python3 planner.py --mdp MDP -- algorithm ALGORITHM`

Where
- `MDP` is the path to an MDP file (a few examples given in `data/mdp/`)
- `ALGORITHM` is one of `vi`, `hpi`, or `lp`

The program computes the optimal value function and an optimal policy using the algorithm specified. 
The output contains these two, where the first column is the former and the second the latter. 
`vi`, `hpi`, and `lp` refer to Value Iteration, Howard's Policy Iteration, and Linear Programming respectively.

## Task 2: Solving a Maze 

- `$ python3 visualize.py gridfile` to visualize the maze (a few example gridfiles given in `data/maze/`)
- `$ python3 encoder.py --grid gridfile > mdpfile` to encode the maze as an MDP into `mdpfile`
- `$ python3 planner.py --mdp mdpfile --algorithm ALGORITHM > vpfile` to solve the maze's MDP 
- `$ python3 decoder.py --grid gridfile --value_policy vpfile > pathfile` to simulate the optimal policy and output a shortest path from start to end
- `$ python3 visualize.py gridfile pathfile` to visualize the solution path
<p align="middle">
  <img src="figs/maze.png" width="40%"> <img src="figs/maze_solved.png" width="40%">
</p>


This project was done for a course assignment of IITB's [CS 747](https://www.cse.iitb.ac.in/~shivaram/teaching/old/cs747-a2020/index.html): Foundations of Intelligent and Learning Agents. The assignment's problem statement can be found [here](https://www.cse.iitb.ac.in/~shivaram/teaching/old/cs747-a2020/pa-2/programming-assignment-2.html). 
