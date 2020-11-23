#!/usr/bin/env python3


class MagicSquare:
    
    def __init__(self, size):
        """ Create magic Square """

        self.size = size
        self.mat = [[0 for i in range(self.size)] for j in range(self.size)]
        self.create_magic_square()
        self.display_square()

    def display_square(self):
        """ Print the magic square """

        for rows in self.mat:
            print(*rows)

    def create_magic_square(self):
        """ Return's the magic square of dimension n """

        xidx = self.size // 2
        yidx = self.size - 1
        self.mat[xidx][yidx] = 1

        for i in range(2, self.size**2 + 1):
            xidx = xidx - 1
            yidx = yidx + 1
            
            if xidx < self.size and yidx < self.size and self.mat[xidx][yidx] != 0 :
                xidx = xidx + 1
                yidx = yidx - 2

            if xidx == -1 and yidx == self.size:
                xidx = 0
                yidx = self.size - 2

            if xidx == -1:
                xidx = self.size - 1
            if yidx == self.size:
                yidx = 0
            
            self.mat[xidx][yidx] = i

        return self.mat
    
m3 = MagicSquare(3)