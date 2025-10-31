#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
drawing.py — Tasks 1, 2, 3

Source (Task 1 note):
- Rectangle class idea/structure based on Lecture 8 (INF201) notebook.
  Extended here with info() and draw(), and more shapes/colors for Task 3.
"""

from dataclasses import dataclass
from typing import Tuple, List
import math
import sys

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as MplRectangle
from matplotlib.patches import Polygon as MplPolygon


# ----------------------------
# Task 1 + 2 + 3: Rectangle
# ----------------------------
@dataclass
class Rectangle:
    """Axis-aligned rectangle given by lower-left (x1,y1) and upper-right (x2,y2)."""
    x1: float
    y1: float
    x2: float
    y2: float
    # Task 3: optional color & linewidth with defaults
    color: str = "black"
    linewidth: float = 1.5

    def __post_init__(self) -> None:
        # normalize so x1<=x2 and y1<=y2
        if self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1
        if self.y1 > self.y2:
            self.y1, self.y2 = self.y2, self.y1

    def info(self) -> None:
        print(f"Rectangle LL=({self.x1}, {self.y1}), UR=({self.x2}, {self.y2}), "
              f"color={self.color}, linewidth={self.linewidth}")

    def draw(self, turtle) -> None:
        rect = MplRectangle(
            (self.x1, self.y1),
            self.x2 - self.x1,
            self.y2 - self.y1,
            fill=False,
            edgecolor=self.color,
            linewidth=self.linewidth
        )
        turtle.add_patch(rect)


# ----------------------------
# Task 3: Triangle
# ----------------------------
@dataclass
class Triangle:
    """Triangle defined by three vertices."""
    p1: Tuple[float, float]
    p2: Tuple[float, float]
    p3: Tuple[float, float]
    color: str = "tab:blue"
    linewidth: float = 1.5

    def info(self) -> None:
        print(f"Triangle p1={self.p1}, p2={self.p2}, p3={self.p3}, "
              f"color={self.color}, linewidth={self.linewidth}")

    def area(self) -> float:
        # Shoelace formula
        (x1, y1), (x2, y2), (x3, y3) = self.p1, self.p2, self.p3
        return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0

    def draw(self, turtle) -> None:
        poly = MplPolygon(
            [self.p1, self.p2, self.p3],
            closed=True,
            fill=False,
            edgecolor=self.color,
            linewidth=self.linewidth
        )
        turtle.add_patch(poly)


# ----------------------------
# Task 3: Circle (as polygon)
# ----------------------------
@dataclass
class Circle:
    """Circle approximated by a many-sided polygon."""
    center: Tuple[float, float]
    radius: float
    color: str = "tab:red"
    linewidth: float = 1.8
    sides: int = 200

    def info(self) -> None:
        print(f"Circle center={self.center}, r={self.radius}, "
              f"color={self.color}, linewidth={self.linewidth}, sides={self.sides}")

    def draw(self, turtle) -> None:
        cx, cy = self.center
        pts: List[Tuple[float, float]] = []
        for k in range(self.sides):
            theta = 2.0 * math.pi * k / self.sides
            x = cx + self.radius * math.cos(theta)
            y = cy + self.radius * math.sin(theta)
            pts.append((x, y))
        poly = MplPolygon(
            pts,
            closed=True,
            fill=False,
            edgecolor=self.color,
            linewidth=self.linewidth
        )
        turtle.add_patch(poly)


# ----------------------------
# Main demo (Tasks 1, 2, 3)
# ----------------------------
if __name__ == "__main__":
    # Task 1: three rectangles + info()
    rects: List[Rectangle] = [
        Rectangle(0, 0, 2, 1, color="black", linewidth=1.5),
        Rectangle(2.5, 0.5, 5, 2.5, color="tab:green", linewidth=2.0),
        Rectangle(-1, -0.5, 1, 1.5, color="tab:purple", linewidth=1.0),
    ]

    # Task 3: triangles with colors + area(), and a circle
    tris: List[Triangle] = [
        Triangle((0, 0), (1.5, 2.0), (3.0, 0.2), color="tab:blue", linewidth=2.0),
        Triangle((4, 1), (5, 3), (6, 0.5), color="orange", linewidth=1.5),
    ]

    # Circle and a square that just fits it (box of size 2r x 2r around center)
    circ = Circle(center=(8, 1.5), radius=1.0, color="tab:red", linewidth=2.0)
    cx, cy, r = circ.center[0], circ.center[1], circ.radius
    circ_box = Rectangle(cx - r, cy - r, cx + r, cy + r, color="gray", linewidth=1.0)

    shapes = rects + tris + [circ, circ_box]

    # Print info (and triangle area)
    for s in shapes:
        s.info()
        if isinstance(s, Triangle):
            print(f"  area={s.area():.3f}")

    # Task 2+3: draw everything with a single turtle (Axes)
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

    for s in shapes:
        s.draw(ax)

    # Autoscale + small padding for nicer view
    ax.autoscale_view()
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    pad_x = (x1 - x0) * 0.05
    pad_y = (y1 - y0) * 0.05
    ax.set_xlim(x0 - pad_x, x1 + pad_x)
    ax.set_ylim(y0 - pad_y, y1 + pad_y)

    ax.set_title("Rectangles, Triangles, and Circles (single turtle / single axes)")
    plt.tight_layout()

    # Show; if backend fails, save PNG
    try:
        plt.show()
    except Exception as e:
        print(f"[WARN] Could not open window ({type(e).__name__}: {e}). Saving to shapes.png", file=sys.stderr)
        plt.savefig("shapes.png", dpi=150)
        print("Saved to shapes.png")
