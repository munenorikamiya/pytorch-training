import torch
from torch.nn import Module

class MyModel(Module):

    def __init__(self, mytensor: torch.Tensor, elem_add: int, elem_multiply: int):
        super().__init__()
        self.mytensor = mytensor
        self.elem_add = elem_add
        self.elem_multiply = elem_multiply


    def forward(self, x: torch.Tensor):
        
        result2 = x + self.mytensor

        result3 = result2 + self.elem_add

        result4 =  result3 * self.elem_multiply


        return result2, result3, result4

    if __name__=="__main__":
        mymodel = ExerciseModel(torch.ones((3,3)), 4, 6)

        p2out, p3out, p4out = mymodel(torch.full((3,3), 2))
        print("2. 入力とself.mytensorを足し合わせた結果:")
        print(repr(p2out))
        print("3. self.elem_addを加算した結果:")
        print(repr(p3out))
        print("4. self.elem_multiplyを乗算した結果:")
        print(repr(p4out))