import numpy as np
from scipy.interpolate import splprep, splev

def generate_dot_grid(n):
    return [(i, j) for i in range(n) for j in range(n)]

def loop_around_dot(x, y, r=0.4):
    return [
        (x + r, y),
        (x, y + r),
        (x - r, y),
        (x, y - r),
        (x + r, y)
    ]

def connect_dots(p1, p2, curve=0.3):
    x1, y1 = p1
    x2, y2 = p2

    mx, my = (x1 + x2)/2, (y1 + y2)/2

    dx, dy = x2 - x1, y2 - y1
    length = np.sqrt(dx**2 + dy**2)

    if length == 0:
        return []

    cx = mx - dy/length * curve
    cy = my + dx/length * curve

    t = np.linspace(0, 1, 20)
    path = []

    for tt in t:
        x = (1-tt)**2 * x1 + 2*(1-tt)*tt * cx + tt**2 * x2
        y = (1-tt)**2 * y1 + 2*(1-tt)*tt * cy + tt**2 * y2
        path.append((x, y))

    return path

def generate_kolam(dots):
    path = []

    for i, (x, y) in enumerate(dots):

        path.extend(loop_around_dot(x, y))

        for (nx, ny) in dots:
            if abs(nx - x) == 1 and ny == y:
                path.extend(connect_dots((x, y), (nx, ny)))

            if abs(ny - y) == 1 and nx == x:
                path.extend(connect_dots((x, y), (nx, ny)))

    return path


def smooth_path(path, points=400):
    if len(path) < 4:
        return [], []

    x = [p[0] for p in path]
    y = [p[1] for p in path]

    try:
        tck, _ = splprep([x, y], s=0.3)
        x_new, y_new = splev(np.linspace(0, 1, points), tck)
        return x_new, y_new
    except:
        return x, y