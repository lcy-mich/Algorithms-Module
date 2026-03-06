class SparseMatrix:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = dict()
        return 
    
    def put(self, x, y, value):
        try: assert x >= 0 and x <= self.width and y >= 0 and y <= self.height
        except: print(f"({x},{y}) are not within bounds of an {self.width}x{self.height} matrix.")
        
        if not x in self.data.keys():
            self.data[x] = dict()

        self.data[x][y] = value

    def get(self, x, y):
        try: assert x >= 0 and x <= self.width and y >= 0 and y <= self.height
        except: print(f"({x},{y}) are not within bounds of an {self.width}x{self.height} matrix.")

        if not (x in self.data.keys() and y in self.data[x]):
            return 0
        return self.data[x][y]
    
matrix = SparseMatrix(10,10)
matrix.put(1,2, 5)
matrix.put(1,3, 10)
matrix.put(2,4, 20)

print(matrix.get(1, 2))
print(matrix.get(4,2))
print(matrix.data)
