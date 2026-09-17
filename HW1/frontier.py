import state
#implements a priority queue
#[list of (priority,state), total num pushed, curr. num. of states, max. num. of states, total num popped, val_fn]
#
# The heap stores each state together with its priority, computed once when the state is
# pushed. The public interface is unchanged -- create/insert take a state, remove returns a
# state -- only the private storage inside h[0] holds the (priority,state) pairs. Without
# this, val() gets re-evaluated ~18 times per push (once per comparison as the state sifts
# through the heap), which makes the expensive heuristics far too slow at a large cap.
def create(s, val_fn=None):
    if val_fn is None:
        val_fn=lambda x: state.hdistance0(x)+state.path_len(x)   # default: uniform-cost search
    return [[(val_fn(s), s)], 0, 0, 0, 0, val_fn]

def is_empty(f):
    return f[0]==[]

def val(h, s):
    # The assignment asks to "change the code in frontier" to pick a heuristic, i.e. to swap
    # between lines like:
    #     return state.hdistance0(s)+state.path_len(s)   # for uniform-cost search
    #     return state.hdistance1(s)+state.path_len(s)   # for A*
    # Instead of editing this line for every run, the value function is passed to create()
    # so a single run can sweep every heuristic.
    return h[5](s)

def insert(h, s):
    #inserts state s to the frontier
    f=h[0]
    h[1]+=1
    h[2]+=1
    if h[2]>h[3]:
        h[3]=h[2]
    f.append((val(h,s), s))     # priority computed once, here
    i=len(f)-1
    # compare f[i][0] (the priority) only -- never the tuples themselves, or Python would
    # fall through to comparing the state lists on ties and change the tie-break order
    while i>0 and f[i][0]<f[(i-1)//2][0]:
        t=f[i]
        f[i]=f[(i-1)//2]
        f[(i-1)//2]=t
        i=(i-1)//2

def remove(h):
    if is_empty(h):
        return 0
    h[2]-=1
    h[4]+=1
    f=h[0]
    s=f[0][1]                  # unwrap: return the state, not the (priority,state) pair
    f[0]=f[len(f)-1]
    del f[-1]
    heapify(f,0)
    return s

def heapify(f,i):
    minSon=i
    if 2*i+1<len(f) and f[2*i+1][0]<f[minSon][0]:
        minSon=2*i+1
    if 2*i+2<len(f) and f[2*i+2][0]<f[minSon][0]:
        minSon=2*i+2
    if minSon!=i:
        t=f[minSon]
        f[minSon]=f[i]
        f[i]=t
        heapify(f, minSon)
