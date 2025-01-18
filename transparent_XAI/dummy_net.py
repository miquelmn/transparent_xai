""" Dummy PyTorch Module for to wrap a callable function.

Author: Miquel Miró Nicolau (UIB), 2025
"""

__version__ = '1.0.0'
__author__ = 'Miquel Miró Nicolau (UIB)'

from torch import nn
import torch


class Net(nn.Module):
    """ Dummy PyTorch Module for to wrap a callable function.

    Args:
        predict_fn: (callable) Function that predicts the output of the model.
    """

    def __init__(self, predict_fn = callable):
        super().__init__()

        self.predict_fn = predict_fn

    def forward(self, x):
        x = x.flatten().cpu().numpy()

        res = predict_fn(x)
        res = np.expand_dims(res, 0)

        res = torch.Tensor(res)

        return res