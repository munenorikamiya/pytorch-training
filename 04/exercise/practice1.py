import torch 
from torch import nn

if __name__ == "__main__":
    my_tensor = torch.ones((32, 3, 128, 128))

    conv1 = nn.Conv2(in_channels=3, out_channels=64, kernel_size=3)