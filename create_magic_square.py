#!/usr/bin/env python3


class MagicSquare:
    
    def __init__(self, size):
        """ Create magic Square """

        self.size = size
        self.mat = [[0 for i in range(self.size)] for j in range(self.size)]
        self.create_magic_square()
        #self.display_square()

    def display_square(self, mat=None):
        """ Print the magic square """
        if mat == None:
            for rows in self.mat:
                print(*rows)
        else:
            for rows in mat:
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
    
    def all_sqrs(self):
        square_one = self.mat
        if self.size == 3:
            all_comb = [square_one for i in range(8)]
            type_a, type_b = self.diagonal_rotation(square_one)
            type_aa, type_ab = self.half_rotation(type_a)
            type_ba, type_bb = self.half_rotation(type_b)
            a, b = self.mid_reflection(type_aa)
            c, d = self.mid_reflection(type_ab)
            e, f = self.mid_reflection(type_ba)
            g, h = self.mid_reflection(type_bb)
            all_comb[:] = a, b, c, d, e, f, g, h
            return all_comb
        else:
            print('Work in progress')
            print('Not Possible for squares other than that of dimension 3*3')

    def diagonal_rotation(self, template_sqr):
        new_sqr = [[template_sqr[i][j] for i in range(self.size)] for j in range(self.size)]
        return template_sqr, new_sqr
    
    def half_rotation(self, template_sqr):
        new_sqr = [[template_sqr[self.size - 1 - i][self.size - 1 - j] for j in range(self.size)] for i in range(self.size)]
        return template_sqr, new_sqr

    def mid_reflection(self, template_sqr):
        new_sqr = [[template_sqr[i][self.size - j - 1] for j in range(self.size)] for i in range(self.size)]
        return template_sqr, new_sqr
    
    def making_cost(self, given_mat):
        if len(given_mat) == 3:
            min_cost = None
            sqrs = self.all_sqrs()
            for sqr in sqrs:
                new_cost = self.cost_check(given_mat, sqr)
                if min_cost == None or min_cost > new_cost:
                    min_cost = new_cost
            
            return min_cost
        else:
            print('Work in progress!!')
    
    def cost_check(self, given_mat, template):
        total_cost = 0
        for i in range(self.size):
            for j in range(self.size):
                total_cost += abs(given_mat[i][j] - template[i][j])
        return total_cost

obj = MagicSquare(3)
mat = []
row = []
for i in range(3):
    row = list(map(int, input().split()))
    mat.append(row)
val = obj.making_cost(mat)
print(val)
