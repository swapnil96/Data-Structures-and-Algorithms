import re
class AvoidRoads:
    
    def __init__( self, row, col, bad ):

        self.row = row
        self.col = col
        self.bad = bad 

    def find(self, x, y, a, b):

        for i in range(0, len(self.dont)):

            if ( x == self.dont[i][0] and y == self.dont[i][1] and a == self.dont[i][2] and b == self.dont[i][3]):
                return False
 
            if ( a == self.dont[i][0] and b == self.dont[i][1] and x == self.dont[i][2] and y == self.dont[i][3]):
                return False        

        return True

    def numWays( self ):

        self.dont = [[0 for i in range(4)] for i in range((len(bad))/4)]

        for i in range(0, (len(bad))/4):
            
            self.dont[i][0] = bad[i*4]
            self.dont[i][1] = bad[i*4+1]
            self.dont[i][2] = bad[i*4+2]
            self.dont[i][3] = bad[i*4+3]

        road = [[0 for i in range(col+1)] for i in range(row+1)] 
        
        road[0][0] = 1

        for x in range(1, col+1):
            
            road[0][x] = 0

            if self.find(0, x-1, 0, x) is True:
                road[0][x] = road[0][x-1]

        for y in range(1, row+1):
        
            road[y][0] = 0

            if self.find(y-1, 0, y, 0) is True:
                road[y][0] = road[y-1][0] 

        for x in range(1, row+1):

            for y in range(1, col+1):

                a = 0
                b = 0
                 
                if self.find(x-1, y, x, y) is False:
                    a = 1
                
                if self.find(x, y-1, x, y) is False:
                    b = 1

                if a == 0 and b == 0:
                    road[x][y] = road[x-1][y] + road[x][y-1] 
                
                elif a == 1 and b == 0:
                    road[x][y] = road[x][y-1]

                elif a == 0 and b == 1:
                    road[x][y] = road[x-1][y]
                    
                else:
                    road[x][y] = 0          

        print road[row][col]

row = int(raw_input())
col = int(raw_input())
a = raw_input()

array1 = re.findall( r'\b\d+\b', a)

bad = map(int, array1)

q = AvoidRoads(row, col, bad)
q.numWays()
