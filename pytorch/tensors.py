# how to create tensors
import torch
scalar = torch.tensor(4)
print(scalar)
print(scalar.ndim) # <-- this print the dimensions of the tensor

vector = torch.tensor([7,7])
print(vector)
print(vector.ndim)# <-- for example this 1 dimensional tensor

matrix = torch.tensor([[1,2],[3,4]])
print(matrix)
print(matrix.ndim) # <-- this will print a 2 dimensional tensor
print(matrix.shape)# <-- this will print the size of the tensor

