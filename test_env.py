from environment import *

grid = create_grid()

# اطبعي الخريطة
for row in grid:
    print(" ".join(str(x) for x in row))

print("Start neighbors:", get_neighbors(grid, START))
print("Danger cell cost:", get_cost(grid, (0, 10)))