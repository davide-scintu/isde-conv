import numpy as np
from abc import ABC, abstractmethod


class CConvKernel(ABC):

    def __init__(self, kernel_size=3):
        self._mask = None
        self._kernel_size = kernel_size  # call setter (odd number)

    @property
    def kernel_size(self):
        return self._kernel_size

    @kernel_size.setter
    def kernel_size(self):
        pass

    @property
    def mask(self):
        return self._mask

    @mask.setter
    def mask(self):
        pass

    def kernel(self, x):
        xp = x


        return xp


