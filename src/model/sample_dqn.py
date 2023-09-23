# DQN Model for Multi UAVs
import torch
import torch.nn as nn

class SampleDQN(nn.Module):
    def __init__(self, input_dim, num_actions, num_of_uav):
        super(SampleDQN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 256)
        self.fc2 = nn.Linear(256, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, int(num_actions * num_of_uav))  # Output Q-values for each action for each UAV

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        return self.fc4(x)
