import torch
import torch.nn as nn

class Mouse_net(nn.Module):
    def __init__(self):
        super(Mouse_net, self).__init__()
        self.fc1 = nn.Linear(10, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, 64)
        
        # Attention Mechanism
        self.attn = nn.MultiheadAttention(64, num_heads=4)  # 4 attention heads
        
        self.fc4 = nn.Linear(64, 2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        
        # Apply attention
        x, _ = self.attn(x, x, x)  # Self-attention
        
        x = self.fc4(x)
        return x