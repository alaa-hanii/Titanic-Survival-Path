from environment import *
from DLS import dls

grid = create_grid()
result = dls(grid, START, GOAL)
print("path length:", len(result["path"]))
print("cost:", result["cost"])
print("nodes_expanded:", result["nodes_expanded"])
print("explored:", len(result["explored"]))