"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, values: list[float]):
        self.values = values

    def __repr__(self) -> str:
        return f"Simpy({ self.values })"

    def fill(self, value: float, num: int) -> None:
        self.values = []

        for j in range(num):
            self.values.append(value)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        assert step != 0.0

        self.values = []

        hasEnded: bool = False
        
        while(hasEnded == False):
            self.values.append(start)
            start += step
            if (start >= stop):
                hasEnded = True
        
    def sum(self) -> float:
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:  # overloads summation operator
        addendum: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)  # make sure they're the same length
            for i in range(len(self.values)):  # have to do a range since rhs is a Simpy
                addendum.append(self.values[i] + rhs.values[i])  # have to index the values since we're iterating over a range
        elif isinstance(rhs, float):  # this one is easier
            for j in self.values:
                addendum.append(j + rhs)  # just add the rhs float to each element in self.values
        return Simpy(addendum)  # hand the list[float] into the Simpy constructor, return a new Simpy object

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:  # overloads summation operator
        addendum: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                addendum.append(self.values[i] ** rhs.values[i])
        elif isinstance(rhs, float):
            for j in self.values:
                addendum.append(j ** rhs)
        return Simpy(addendum)
    
    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:  # overloads summation operator
        addendum: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                addendum.append(self.values[i] % rhs.values[i])
        elif isinstance(rhs, float):
            for j in self.values:
                addendum.append(j % rhs)
        return Simpy(addendum)