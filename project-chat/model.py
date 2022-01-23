import torch
import torch.nn as nn


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.k1 = nn.Linear(input_size, hidden_size) 
        self.k2 = nn.Linear(hidden_size, hidden_size) 
        self.k3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        out = self.k1(x)
        out = self.relu(out)
        out = self.k2(out)
        out = self.relu(out)
        out = self.k3(out)
        return out
