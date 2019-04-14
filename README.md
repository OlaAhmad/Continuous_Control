
[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif "Double-joined arm Agent"

# Project 2: Continuous_Control

### Introduction


In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. The goal of the agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

### Getting started

Download the Continous_Control repository from the top-right button. You can also clone the repository and downloaded from a terminal in your workspace directory using the following command line:
    
    git clone https://github.com/OlaAhmad/Continuous_Control.git
        
### Usage

Go to the Navigation folder and open the Navigation notebook to train the DQN agent as follows:

    cd Continuous_Control
    Jupyter notebook Continuous_Control-2.ipynb

When runing the notebook, the actor-critic agent will start training over a number of episodes; Two neural networks will start training and simultaneously update their parameters every number of iterations. The updated parameters of the trained acrchitectures are saved in checkpoint files

### Codes

We added two files to train the agent for the notebook: 
1. model.py: builds actor and critic neural network architectures. 
2. dqn_agent.py: interacts with Banana enviornement and learns the agent from it.
We used and adapted the codes from the lesson (ddpg-pendulum).

### Resources

* udacity/deep-reinforcement-learning

