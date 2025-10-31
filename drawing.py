#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
drawing.py — Tasks 1 & 2

Source:
The Rectangle class is based on the example from Lecture 8 (INF201).
Extended here with info() and draw() methods, and a main section
that prints rectangle info and draws them using Matplotlib.
"""

from dataclasses import dataclass
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as MplRectangle


# ----------------------------
# Task 1 + Task 2: Rectangle
# ----------------------------
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

    def draw(self, turtle) -> None:
        """Draws the rectangle on a Matplotlib Axes object passed as `turtle`."""
        rect = MplRectangle(
            (self.x1, self.y1),
            self.x2 - self.x1,
            self.y2 - self.y1,
            fill=False,
            edgecolor="black",
            linewidth=1.5
        )
        turtle.add_patch(rect)


# ----------------------------
# Main section
# ----------------------------
if __name__ == "__main__":
    # Create a list of three rectangles
    rectangles = [
        Rectangle(0, 0, 2, 1),
        Rectangle(1, 2, 3, 4),
        Rectangle(-1, -2, 0, 1)
    ]

    # Task 1: Print info for each rectangle
    for rect in rectangles:
        rect.info()

    # Task 2: Draw all rectangles using a single turtle (Matplotlib Axes)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

    for rect in rectangles:
        rect.draw(ax)

    ax.autoscale_view()
    ax.set_title("Rectangles (Tasks 1 & 2)")
    plt.tight_layout()
    plt.show()
