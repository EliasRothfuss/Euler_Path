import random
import copy

class pathfinder:
    def __init__(self, matrix):
        self.point_vis = list()
        self.matrix = copy.copy(matrix)
        #print(id(self.matrix), id(matrix))
        self.forbidden_nextpoint = None

    def restore_Cotent(self):
        self.matrix[self.point_vis[-1]][self.point_vis[-2]] = 1
        self.matrix[self.point_vis[-2]][self.point_vis[-1]] = 1

    def get_nextpoint(self, point):
        indices = list()
        for i,e in enumerate(self.matrix[point]):
            if e == 1 and i != self.forbidden_nextpoint:
                indices.append(i)
        print(point +1 , [i+1 for i in indices])
        if indices:
            #return random.choice(indices)
            return indices[-1]
        else:
            return None

    def get_startpoint(self):
        indices = list()
        for i, e in enumerate(self.matrix):
            if sum(e) % 2 == 1:
                indices.append(i)
        if indices:
            return indices[0]
        else:
            return 0

    def built_path_pre(self, point_ = None):
        if point_ is None:
            point_ = self.get_startpoint()

        self.point_vis = [point_]
        self.point = point_


    def built_path_sub(self):
        if any(max(self.matrix)):
            nextpoint = self.get_nextpoint(self.point)
            if nextpoint is not None:
                self.matrix[self.point][nextpoint] = 0
                self.matrix[nextpoint][self.point] = 0
                self.point_vis.append(nextpoint)
                #print(nextpoint)
                self.point = nextpoint
                self.forbidden_nextpoint = None
            else:
                self.point = self.point_vis[-2]
                self.restore_Cotent()
                self.forbidden_nextpoint = self.point_vis[-1]
                #print(f"Try point {self.point_vis[-2]}")
                del self.point_vis[-1]
        else:
            self.n = 0

        return self.point_vis

    def built_path(self, point_ = None):
        self.built_path_pre(point_)
        self.n = 1
        while self.n:
            self.built_path_sub()
            print (self.point_vis)
        return self.point_vis



matrix = [
    [0,1,0,1,1],
    [1,0,1,1,1],
    [0,1,0,1,0],
    [1,1,1,0,1],
    [1,1,0,1,0]
    ]

#path = pathfinder(matrix)
#print(path.built_path())

'''
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 1],y
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0]
'''
