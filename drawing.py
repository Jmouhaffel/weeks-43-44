#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
drawing.py — Task 1: Rectangle class

Source:
The Rectangle class is based on the example from Lecture 8 (INF201).
Extended here with an info() method and a simple main section.
"""

from dataclasses import dataclass

@dataclass
class Rectangle:
    """Represents a rectangle defined by two corners: lower-left and upper-right."""
    x1: float
    y1: float
    x2: float
    y2: float

    def info(self) -> None:
        """Prints the coordinates of the lower-left and upper-right corners."""
        print(f"Rectangle: lower-left=({self.x1}, {self.y1}), upper-right=({self.x2}, {self.y2})")

# ----------------------
# Main section
# ----------------------
if __name__ == "__main__":
    # create a list of three rectangles
    rectangles = [
        Rectangle(0, 0, 2, 1),
        Rectangle(1, 2, 3, 4),
        Rectangle(-1, -2, 0, 1)
    ]

    # call info() for each
    for rect in rectangles:
        rect.info()
