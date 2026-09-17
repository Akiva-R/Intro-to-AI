#search
import state
import frontier

def search(n, val_fn=None, cap=1500, board=None):
    '''
    Best-first search (uniform-cost / greedy / A* / weighted A*, depending on val_fn).
    board, if given, is a starting nXn board (a plain list) so different heuristics can be
    compared on the exact same puzzle instance; otherwise a fresh random board is created.
    Returns (solved, pushed, popped, path_cost, path):
      - on success: solved=True, path_cost is the length of the solution path found
      - on hitting the cap (pushed > cap) or exhausting the frontier: solved=False,
        path_cost=100 (per the assignment's spec for a "stuck" run), path=None
    There is deliberately no closed/visited set here -- that matches the handed-out
    search.py and is why runs can get "stuck" and need the cap at all.
    '''
    s = state.fresh(board) if board is not None else state.create(n)
    f = frontier.create(s, val_fn)
    while not frontier.is_empty(f):
        if f[1] > cap:
            return (False, f[1], f[4], 100, None)
        s = frontier.remove(f)
        if state.is_target(s):
            return (True, f[1], f[4], state.path_len(s), s[1])
        ns = state.get_next(s)
        for i in ns:
            frontier.insert(f, i)
    return (False, f[1], f[4], 100, None)


def bfs(n, cap=1500, board=None):
    '''
    Breadth-first search: same board/move rules and the same reverse-move pruning as
    get_next, but explores in FIFO order (a plain queue) instead of a priority queue.
    Counts pushed/popped the same way search() does, and is subject to the same cap.
    '''
    s = state.fresh(board) if board is not None else state.create(n)
    queue = [s]
    pushed, popped = 0, 0
    head = 0
    while head < len(queue):
        if pushed > cap:
            return (False, pushed, popped, 100, None)
        s = queue[head]; head += 1
        popped += 1
        if state.is_target(s):
            return (True, pushed, popped, state.path_len(s), s[1])
        for i in state.get_next(s):
            pushed += 1
            queue.append(i)
    return (False, pushed, popped, 100, None)


def iddfs(n, cap=1500, board=None):
    '''
    Iterative-deepening DFS: repeated depth-limited DFS with an increasing path-length
    limit (0, 1, 2, ...) until the target is found. pushed/popped accumulate across all
    iterations, and the shared 1500 cap applies to that running total (an iteration is
    aborted as soon as the total crosses the cap, and no further iteration is started).
    '''
    root = state.fresh(board) if board is not None else state.create(n)
    counters = [0, 0]  # [pushed, popped], shared across the recursive calls / iterations

    def dls(s, limit):
        # returns the found state, or None, or the string "cap" if the cap was hit
        counters[1] += 1
        if state.is_target(s):
            return s
        if state.path_len(s) == limit:
            return None
        for child in state.get_next(s):
            if counters[0] > cap:
                return "cap"
            counters[0] += 1
            r = dls(child, limit)
            if r is not None:
                return r
        return None

    limit = 0
    while True:
        r = dls(root, limit)
        if counters[0] > cap:
            return (False, counters[0], counters[1], 100, None)
        if r is not None and r != "cap":
            return (True, counters[0], counters[1], state.path_len(r), r[1])
        limit += 1


if __name__ == "__main__":
    print(search(4))
