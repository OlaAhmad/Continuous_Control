import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

def hidden_init(layer):
    fan_in = layer.weight.data.size()[0]
    lim = 1. / np.sqrt(fan_in)
    return (-lim, lim)

class Actor(nn.Module):
    """
    Actor (policy) model
    """
    def __init__(self, state_size, action_size, seed, fc1_units=128, fc2_units=128, fc3_units=256):
        """
        initialize class.
        
        :param state_size: 
        :param action_size: 
        :param seed: 
        :param fc1_units: 
        :param fc2_units: 
        """
        super(Actor, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)
        self.fc3 = nn.Linear(fc2_units, fc3_units)
        self.fc4 = nn.Linear(fc3_units, action_size)

        self.bn1 = nn.LayerNorm(fc1_units)
        self.bn2 = nn.LayerNorm(fc2_units)
        self.bn3 = nn.LayerNorm(fc3_units)

        self.reset_parameters()

    def reset_parameters(self):
        self.fc1.weight.data.uniform_(*hidden_init(self.fc1))
        self.fc2.weight.data.uniform_(*hidden_init(self.fc2))
        self.fc3.weight.data.uniform_(*hidden_init(self.fc3))
        self.fc4.weight.data.uniform_(-3e-3, 3e-3)

    def forward(self, state):
        x = F.relu(self.bn1(self.fc1(state)))
        x = F.relu(self.bn2(self.fc2(x)))
        x = F.relu(self.bn3(self.fc3(x)))
        return torch.tanh(self.fc4(x))

class Critic(nn.Module):
    """
    Critic model for state value
    """

    def __init__(self, state_size, action_size, seed, fcs1_units=128, fcs2_units=128, fc3_units=256):
        """
        initialize class.

        :param state_size: 
        :param action_size: 
        :param seed: 
        :param fc1_units: 
        :param fc2_units: 
        """
        super(Critic, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fcs1 = nn.Linear(state_size, fcs1_units)
        self.fcs2 = nn.Linear(fcs1_units+action_size, fcs2_units)
        self.fc3 = nn.Linear(fcs2_units + action_size, fc3_units)
        self.fc4 = nn.Linear(fc3_units, 1)

        self.bn1 = nn.LayerNorm(fcs1_units)
        self.bn2 = nn.LayerNorm(fcs2_units)
        self.bn3 = nn.LayerNorm(fc3_units)

        self.reset_parameters()

    def reset_parameters(self):
        self.fcs1.weight.data.uniform_(*hidden_init(self.fcs1))
        self.fcs2.weight.data.uniform_(*hidden_init(self.fcs2))
        self.fc3.weight.data.uniform_(*hidden_init(self.fc3))
        self.fc4.weight.data.uniform_(-3e-3, 3e-3)

    def forward(self, state, action):
        xs = F.relu(self.bn1(self.fcs1(state)))
        x = torch.cat((xs, action), dim=1)
        xs = F.relu(self.bn2(self.fcs2(x)))
        x = torch.cat((xs, action), dim=1)
        x = F.relu(self.bn3(self.fc3(x)))
        return self.fc4(x)
