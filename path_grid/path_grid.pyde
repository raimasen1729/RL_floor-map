path_position = loadStrings("output.txt")
l = len(path_position)
location_to_state = {
    'L1' : 0,
    'L2' : 1,
    'L3' : 2,
    'L4' : 3,
    'L5' : 4,
    'L6' : 5,
    'L7' : 6,
    'L8' : 7,
    'L9' : 8
}

state_to_location = dict((state,location) for location,state in location_to_state.items())

grid = [[0,1,2],[3,4,5],[6,7,8]]

for i in range(3):
    for j in range(3):
        for k in range(l):
            if (grid[i][j]==location_to_state[path_position[0]]):
                grid[i][j]=-1
            elif (grid[i][j]==location_to_state[path_position[l-1]]):
                grid[i][j]=-2
            elif(grid[i][j]==location_to_state[path_position[k]]):
                grid[i][j]=-3                
print(grid)     
           
def setup():
    size(600,600) 
w = 200
    
def draw():
    x,y = 0,0
    for row in grid:
        for col in row:
           if col == -1:
             fill(220,0,0)
           elif col == -2:
             fill(0,180,0)
           elif col == -3:
             fill(255,244,79)
           else:
             fill(240)
           rect(x,y,w,w)
           textSize(32)
           fill(50)
           (m,n) = (0,0)
           for i in range(9):
                text(state_to_location[i],m+90,n+100)
                m = m+w
                if(m>490):
                    m = 0
                    n = n+w
                rect(0,200,200,10)
                rect(190,200,10,200)
                rect(400,200,10,200)
                rect(400,390,200,10)
           x = x + w
        y = y + w
        x = 0 
