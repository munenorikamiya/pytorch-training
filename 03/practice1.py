import torch
import numpy as np


data = np.array([
[[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
[[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
[[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]])

# question1
tensor1 = torch.tensor(data)
# print(tensor1.size()) 

# question2
tensor2 = torch.permute(tensor1,(2,0,1))
# print(tensor2, "\n", tensor2.size())

# question3
tensor3 = tensor2.sum(dim = 0)
# print(tensor3)

# question4
tensor4 = tensor3.mean(dim = 1)
print(tensor4)


