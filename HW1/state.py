'''
The state is a list of 2 items: the board, the path
The target for 8-puzzle is: (zero is the hole)
012
345
678
'''
import random
import math

#returns a random board nXn
def create(n):
    s=list(range(n*n))      # s is the board itself. a vector that represent a matrix. s=[0,1,2....n^2-1]
    m="<>v^"                # m is "<>v^" - for every possible move (left, right, down, up)
    for i in range(n**3):  # makes n^3 random moves to mix the tiles
        if_legal(s,m[random.randrange(4)])
    return [s,""]           # at the beginning "" is an empty path, later on path
                            # contains the path that leads from the initial state to the state

def fresh(board):           # wraps an existing board in a new state with an empty path,
    return [board[:],""]    # so every algorithm can start from the identical board

def get_next(x):            # returns a list of the children states of x
    ns=[]                   # the next state list
    for i in "<>v^":
        s=x[0][:]           # [:] - copies the board in x[0]
        if_legal(s,i)       # try to move in direction i
        # checks if the move was legal and...
        if s.index(0)!=x[0].index(0) and \
           (x[1]=="" or x[1][-1]!="><^v"["<>v^".index(i)]): # check if it's the first move or it's a reverse move
            ns.append([s,x[1]+i])   # appends the new state to ns
    return ns


def path_len(x):
    return len(x[1])

def is_target(x):
    n=len(x[0])                     # the size of the board
    return x[0]==list(range(n))     # list(range(n)) is the target state

#############################
def if_legal(x,m):                  # gets a board and a move and makes the move if it's legal
    n=int(math.sqrt(len(x)))        # the size of the board is nXn
    z=x.index(0)                    # z is the place of the empty tile (0)
    if z%n>0 and m=="<":            # checks if the empty tile is not in the first col and the move is to the left
        x[z]=x[z-1]                 # swap x[z] and x[z-1]...
        x[z-1]=0                    # ...and move the empty tile to the left
    elif z%n<n-1 and m==">":        # check if the empty tile is not in the n's col and the move is to the right
        x[z]=x[z+1]
        x[z+1]=0
    elif z>=n and m=="^":           # check if the empty tile is not in the first row and the move is up
        x[z]=x[z-n]
        x[z-n]=0
    elif z<n*n-n and m=="v":        # check if the empty tile is not in the n's row and the move is down
        x[z]=x[z+n]
        x[z+n]=0

# This is your HW
# In the goal board tile v sits at index v, so v's goal row is v//n and its goal col is v%n.
# The blank (0) is left out of every heuristic below: it is not a tile that has to be moved
# into place, and counting it would let the heuristic overestimate and stop being admissible.

def hdistance0(s):                   # the heuristic value of s -- uniform cost
    return 0

def hdistance1(s):                   # number of tiles out of place
    b=s[0]
    return sum(1 for i,v in enumerate(b) if v!=0 and v!=i)

def hdistance2(s):                   # sum of the Manhattan distances of the tiles from their targets
    b=s[0]
    n=int(math.sqrt(len(b)))
    d=0
    for i,v in enumerate(b):
        if v!=0:
            d+=abs(i//n-v//n)+abs(i%n-v%n)   # rows apart + cols apart
    return d

def linear_conflicts(s):             # takes a state, like every other heuristic here
    '''
    Counts the linear conflicts on the board of state s.
    Two tiles conflict when they are already in their goal line (row or column) but are
    in the wrong order relative to each other, so one has to step out of the line and back
    to let the other pass -- 2 moves the Manhattan distance never charges for.
    Returns the number of conflicts; the caller is the one that multiplies by 2.
    A row with k>2 mutually conflicting tiles does NOT need 2*C(k,2) extra moves, so
    counting every conflicting pair would overestimate. Instead we repeatedly drop the tile
    that takes part in the most conflicts and count 1 for it, which is the standard
    (admissible) way of resolving a line.
    '''
    b=s[0]                          # same unpacking as hdistance1 / hdistance2
    n=int(math.sqrt(len(b)))
    lc=0
    lines=[]
    for r in range(n):              # every row, as (position in line, goal position in line)
        lines.append([(c,b[r*n+c]%n) for c in range(n)
                      if b[r*n+c]!=0 and b[r*n+c]//n==r])   # keep the tiles whose goal row is r
    for c in range(n):              # every column, same idea with the roles swapped
        lines.append([(r,b[r*n+c]//n) for r in range(n)
                      if b[r*n+c]!=0 and b[r*n+c]%n==c])    # keep the tiles whose goal col is c
    for line in lines:
        t=line[:]                   # the tiles still left in this line
        while True:
            # count how many conflicts each remaining tile takes part in
            cnt=[0]*len(t)
            for i in range(len(t)):
                for j in range(i+1,len(t)):
                    if t[i][1]>t[j][1]:   # i is before j but belongs after it
                        cnt[i]+=1
                        cnt[j]+=1
            if not cnt or max(cnt)==0:
                break               # no conflicts left in this line
            lc+=1
            del t[cnt.index(max(cnt))]   # drop the most conflicted tile and count it once
    return lc

def hdistance3(s):                   # Manhattan distance + linear conflict
    return hdistance2(s)+2*linear_conflicts(s)

def weighted(s):                     # 4*Manhattan + tiles out of place
    return 4*hdistance2(s)+hdistance1(s)

def md_plus_k_lc(s,k):               # Manhattan distance + k*(linear conflicts), for question B
    return hdistance2(s)+k*linear_conflicts(s)
