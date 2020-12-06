class Matrix:
    
    
    
    def __init__(self, matrix_string):
        vectores = matrix_string.split('\n')
        self.matrix = []
        for i in vectores:
            self.matrix.append( list(map(int, i.split(' ')))  )

    def row(self, index):
        return self.matrix[index-1]
        

    def column(self, index):
        r = []
        for i in range(len(self.matrix)) :
            r.append( self.matrix[i][index-1] )
        
        return r
    
    