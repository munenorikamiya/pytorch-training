import torch 
from torch import nn

if __name__=="__main__":

    my_tensor = torch.ones((32, 1024))
    print(my_tensor.size())

    fc = nn.Linear(in_features=1024, out_features=256)
    out = fc(my_tensor)
    print(out.size())

    fc2 = nn.Linear(in_features=1024, out_features=2048)
    out2 = fc2(my_tensor)
    print(out2.size())