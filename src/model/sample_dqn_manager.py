import random

from torch import nn

from src.model.sample_dqn import SampleDQN
from src.replay_memory import ReplayMemory
from src.uav_config import UavConfig
import torch


class SampleDQNManager:
    epsilon: float
    model_type: str
    model = None
    num_of_uav: int
    num_of_actions: int
    epsilon: float
    epsilon_end: float
    memory: ReplayMemory
    batch_size: int
    learning_rate: float
    gamma: float
    optimizer = None
    criterion = None

    def __init__(self, config: UavConfig):
        self.memory = ReplayMemory(capacity=1000)
        self.model_type = config.model
        self.num_of_uav = config.num_of_uav
        self.num_of_actions = config.num_of_actions
        self.epsilon = config.epsilon_start
        self.epsilon_end = config.epsilon_end
        self.epsilon_decay = config.epsilon_decay
        self.batch_size = config.batch_size
        self.learning_rate = config.learning_rate
        self.gamma = config.gamma

        self.set_model()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=self.learning_rate)
        self.criterion = nn.MSELoss()

    def set_model(self):
        if self.model_type == 'DEFAULT':
            self.model = SampleDQN(int(self.num_of_uav * 4),
                                   int(self.num_of_actions),
                                   int(self.num_of_uav)
                                   )
        # if you want, add models
        else:
            pass

    def get_action(self, states):
        state_tensor = torch.tensor(states, dtype=torch.float32)
        q_values = self.model(state_tensor)
        actions = []

        for i in range(0, self.num_of_uav):  # For each UAV
            if random.uniform(0, 1) < self.epsilon:
                actions.append(random.choice(range(self.num_of_actions)))
            else:
                start_idx = int(i * self.num_of_actions)
                end_idx = int(start_idx + self.num_of_actions)
                actions.append(torch.argmax(q_values[start_idx:end_idx]).item())

        return actions

    def update(self, memory_data):
        self.push(memory_data)
        if len(self.memory) > self.batch_size:
            transitions = self.memory.sample(self.batch_size)
            batch_state, batch_action, batch_reward, batch_next_state, batch_done = zip(*transitions)

            batch_state = torch.tensor(batch_state, dtype=torch.float32)
            batch_action = torch.tensor(batch_action, dtype=torch.long)
            batch_reward = torch.tensor(batch_reward, dtype=torch.float32)
            batch_next_state = torch.tensor(batch_next_state, dtype=torch.float32)
            batch_done = torch.tensor(batch_done, dtype=torch.bool)

            current_q_list = []
            target_q_list = []
            for i in range(0, self.num_of_uav):
                current_q_list.append(self.model(batch_state).narrow(1,i * self.num_of_actions, self.num_of_actions).gather(1,batch_action[:,i].unsqueeze(1)).squeeze(1))
                next_q = self.model(batch_next_state).narrow(1, i * self.num_of_actions, self.num_of_actions).max(1)[0]
                target_q_list.append(batch_reward[:, i] + self.gamma * next_q * (~batch_done[:, i]))

            current_qs = torch.stack(current_q_list).transpose(0, 1)
            target_qs = torch.stack(target_q_list).transpose(0, 1)
            loss = self.criterion(current_qs, target_qs.detach())
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

        pass

    def batch_memory(self):
        pass

    def push(self, memory_data: tuple):
        self.memory.push(memory_data)

    def get_memory_size(self):
        return len(self.memory)

    def update_epsilon(self):
        self.epsilon = max(self.epsilon_end, self.epsilon * self.epsilon_decay)