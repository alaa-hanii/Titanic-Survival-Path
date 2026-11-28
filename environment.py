# environment.py
# الخريطة وقواعدها: كل الخوارزميات بتعتمد على الملف ده

# ---------- 1) الثوابت ----------
ROWS = 15
COLS = 20

CALM = 0       # مياه هادية
ROUGH = 1      # مياه مضطربة
DANGER = 2     # مياه خطرة
ICEBERG = 3    # جبل ثلج (ممنوع)

COSTS = {
    CALM: 1,
    ROUGH: 3,
    DANGER: 8,
}

START = (0, 0)             # السفينة: أعلى الشمال (صف 0، عمود 0)
GOAL = (14, 19)            # الميناء: أسفل اليمين


# ---------- 2) بناء الخريطة ----------
def create_grid():
    """بترجّع الخريطة: قايمة صفوف، كل صف قايمة أرقام."""
    grid = [[CALM for _ in range(COLS)] for _ in range(ROWS)]

    # مياه مضطربة (مناطق)
    for r in range(3, 8):
        for c in range(4, 9):
            grid[r][c] = ROUGH
    for r in range(9, 13):
        for c in range(10, 16):
            grid[r][c] = ROUGH

    # مياه خطرة (مناطق)
    for r in range(0, 5):
        for c in range(9, 13):
            grid[r][c] = DANGER
    for r in range(8, 12):
        for c in range(15, 18):
            grid[r][c] = DANGER

    # جبال ثلج (حواجز)
    for r in range(5, 11):
        grid[r][9] = ICEBERG
    for c in range(2, 7):
        grid[10][c] = ICEBERG
    for r in range(11, 15):
        grid[r][12] = ICEBERG
    grid[2][15] = ICEBERG
    grid[3][15] = ICEBERG
    grid[6][14] = ICEBERG

    # تأكيد إن البداية والهدف مياه هادية
    grid[START[0]][START[1]] = CALM
    grid[GOAL[0]][GOAL[1]] = CALM

    return grid


# ---------- 3) الجيران ----------
def get_neighbors(grid, cell):
    """
    بترجّع الخلايا المسموح نروحلها من الخلية الحالية.
    4 اتجاهات: فوق، تحت، شمال، يمين.
    """
    r, c = cell
    neighbors = []

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        # جوه حدود الخريطة؟
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            # مش جبل ثلج؟
            if grid[nr][nc] != ICEBERG:
                neighbors.append((nr, nc))

    return neighbors


# ---------- 4) التكلفة ----------
def get_cost(grid, cell):
    """تكلفة دخول الخلية دي (هادية=1، مضطربة=3، خطرة=8)."""
    r, c = cell
    return COSTS[grid[r][c]]