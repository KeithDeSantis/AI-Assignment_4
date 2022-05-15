# AI-Assignment-4

This is the submission for Project 4: Reinforcement Learning for CS 4341: Artificial Intelligence in C22 at WPI. \
Our implementation is written in python and was developed using the 3.10 interpreter.

Run ```qlearn.py <board-file-path> <time-to-run> <probability-of-moving-in-desired-direction> <constant-reward>``` to run the program on the given board with the given parameters.

The project was to create a game-playing agent using Reinforcement Learning to play a game where the agent was placed at a starting point, and was tasked
with getting to a terminating point (a spot with a number). There is a penalty for each "time step" spent moving, and a given probability of deflecting
whenever the agent attempts to move in a direction. Using reinforcement learning, the agent determines the best course of action based on starting position
and board.

This submission contains the following files:

* ```agent.py```
* ```board.py```
* ```main.py```
* ```qlearn.py```
* ```boardgenerator.py```
* ```qtable.py```

Book-keeping and record files:
* ```README.md``` (this file)

Sample Boards:
* ```sample.txt```

Sample Output:

`python3 qlearn.py sample.txt 5 0.8 -0.04`
```
0	0	0	0	0	0	
0	-1	0	0	8	0	
0	0	0	0	0	0	
0	0	0	0	0	0	
9	0	0	0	0	0	
0	0	0	0	0	0	
------------------------
▼	▲	▶	▼	◀	▼	
◀	-1	▶	▼	8	▼	
▼	▼	▼	▼	▼	▼	
▼	◀	◀	◀	◀	◀	
9	◀	◀	◀	◀	◀	
▲	◀	◀	◀	◀	◀	

```

If you have any trouble running our code, feel free to contact us at kshah2@wpi.edu, lsdias@wpi.edu, or kwdesantis@wpi.edu.
