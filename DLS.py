# algorithms/dls.py
# Depth-Limited Search: DFS بس بيوقف لما يوصل لعمق أقصى

from environment import get_neighbors, get_cost

DEPTH_LIMIT = 50   # أقصى عمق مسموح (أقصر مسار في الخريطة 33 خطوة)


def dls(grid, start, goal):
    explored = []         # الخلايا اللي زارتها بالترتيب
    nodes_expanded = 0    # الخلايا اللي فتحتها وجابت جيرانها
    best_depth = {start: 0}   # أقل عمق وصلنا بيه لكل خلية، عشان منلفش في دايرة

    def recurse(cell, depth, path):
        nonlocal nodes_expanded
        explored.append(cell)

        if cell == goal:
            return path
        if depth == DEPTH_LIMIT:
            return None   # وصلنا للحد الأقصى

        nodes_expanded += 1
        for nxt in get_neighbors(grid, cell):
            nd = depth + 1
            if nxt in best_depth and best_depth[nxt] <= nd:
                continue
            best_depth[nxt] = nd
            result = recurse(nxt, nd, path + [nxt])
            if result is not None:
                return result
        return None

    path = recurse(start, 0, [start])

    if path is None:
        return {"path": [], "explored": explored,
                "cost": 0, "nodes_expanded": nodes_expanded}

    cost = sum(get_cost(grid, cell) for cell in path[1:])
    return {"path": path, "explored": explored,
            "cost": cost, "nodes_expanded": nodes_expanded}