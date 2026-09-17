# HW1 — Solving the N-Puzzle with A*

Best-first search on the sliding-tile puzzle (3x3, 4x4, 5x5), comparing heuristics by
solution cost and by how many states each one pushes before it finds a goal.

## Layout

| File | What's in it |
| --- | --- |
| `state.py` | Board representation, move generation, and the heuristics — `hdistance0` (uniform cost), `hdistance1` (tiles out of place), `hdistance2` (Manhattan), `linear_conflicts`, `hdistance3` (Manhattan + linear conflict), `weighted`, `md_plus_k_lc` |
| `frontier.py` | Binary-heap priority queue. Takes the value function at `create()` time, so one run can sweep every heuristic without editing code |
| `search.py` | `search()` (best-first: uniform / greedy / A* / weighted A*), plus `bfs()` and `iddfs()` for comparison |
| `hw1.ipynb` | The submission — benchmark harness, the 3x3/4x4/5x5 summary tables, and the written answers |
| `exercise1.docx.md`, `Solving the 15 Puzzle.md` | The assignment handouts |

A board is `[tiles, path]`, where `tiles` is a flat list of length `n*n` with `0` as the blank,
and `path` is the move string (`<`, `>`, `^`, `v`) taken to reach it. The goal is
`list(range(n*n))`. There is deliberately no closed set, which is why runs can get stuck and
why every search takes a `cap` on states pushed.

## Setup

Requires Python 3.14 (developed against 3.14.7).

```
python -m venv .venv
.venv\Scripts\activate          # Windows;  source .venv/bin/activate on macOS/Linux
pip install -r requirements.txt
```

## Running

Open the notebook, which is where the results live:

```
jupyter lab hw1.ipynb
```

or open `hw1.ipynb` in VS Code and select the `.venv` interpreter as the kernel. The notebook
ships with its outputs saved, so the tables are readable without re-running; re-running all
cells takes a while, since it is 100 runs per heuristic per board size at `cap=50000`.

To just watch a single 4x4 solve from the command line:

```
python search.py
```
