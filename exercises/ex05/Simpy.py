"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730324058"


class Simpy:
    """Epic Simpy class! Remember: no simping!"""
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, values: list[float]):
        """Here's a flippin docstring!"""
        self.values = values

    def __repr__(self) -> str:
        """Here's a flippin docstring!"""
        return f"Simpy({ self.values })"

    def fill(self, value: float, num: int) -> None:
        """Here's a flippin docstring!"""
        self.values = []

        for j in range(num):
            self.values.append(value)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Here's a flippin docstring!"""
        assert step != 0.0
        self.values = []
        if step < 0:  # step is negative -- going down
            while(start > stop):
                self.values.append(start)
                start += step
        else:  # step is positive -- going up
            while(start > stop):
                self.values.append(start)
                start += step
        
    def sum(self) -> float:
        """Here's a flippin docstring!"""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:  # overloads summation operator
        """Here's a flippin docstring!"""
        addendum: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)  # make sure they're the same length
            for i in range(len(self.values)):  # have to do a range since rhs is a Simpy
                addendum.append(self.values[i] + rhs.values[i])  # have to index the values (range)
        elif isinstance(rhs, float):  # this one is easier
            for j in self.values:
                addendum.append(j + rhs)  # just add the rhs float to each element in self.values
        return Simpy(addendum)  # hand the list[float] into the Simpy constructor, return a new Simpy object

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:  # overloads exponent operator
        """Here's a flippin docstring!"""
        exponentiatium: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                exponentiatium.append(self.values[i] ** rhs.values[i])
        elif isinstance(rhs, float):
            for j in self.values:
                exponentiatium.append(j ** rhs)
        return Simpy(exponentiatium)
    
    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:  # overloads modulo operator
        """Here's a flippin docstring!"""
        modularium: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                modularium.append(self.values[i] % rhs.values[i])
        elif isinstance(rhs, float):
            for j in self.values:
                modularium.append(j % rhs)
        return Simpy(modularium)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:  # overloads equality operator
        """Here's a flippin docstring!"""
        boolarama: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)  # True or False, baby
            for i in range(len(self.values)):
                boolarama.append(self.values[i] == rhs.values[i])
        elif isinstance(rhs, float):
            for j in self.values:
                boolarama.append(j == rhs)
        return boolarama
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:  # overloads greater than operator
        """Here's a flippin docstring!"""
        superiorium: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)  # True or False, baby
            for i in range(len(self.values)):
                superiorium.append(self.values[i] > rhs.values[i])
        elif isinstance(rhs, float):
            for j in self.values:
                superiorium.append(j > rhs)
        return superiorium

    def __getitem__(self, mask: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Here's a flippin docstring!"""
        # return list of only the values that match the mask, or a regular old float for those inclined
        if isinstance(mask, int):
            return self.values[mask]
        else:
            mask_on_values: list[float] = []
            for i in range(len(self.values)):
                if mask[i]:
                    mask_on_values.append(self.values[i])
            return Simpy(mask_on_values)