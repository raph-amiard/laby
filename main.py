from __future__ import annotations 

from dataclasses import dataclass
from typing import List

@dataclass
class Cell:
    maze: Maze
    x: int
    y: int
    bottom: bool = False
    right: bool = False

@dataclass
class Maze:
    cells: List[List[Cell]]
    width: int
    height: int

    @staticmethod
    def create_maze(width: int, height: int):
        mz = Maze([], width, height)
        for y in range(height):
            row = []
            mz.cells.append(row)
            for x in range(width):
                row.append(Cell(mz, x, y))

    def connect(self, c1: Cell, c2: Cell):
        if c1.x == c2.x:
            if c1.y == c2.y - 1:
                c1.bottom = True
            else:
                assert c2.y == c1.y - 1
                c2.bottom = True
        else:
            assert c1.y == c2.y
            if c1.x == c2.x - 1:
                c1.right = True
            else:
                assert c2.x == c1.x - 1
                c2.right = True

    def init(self):
        